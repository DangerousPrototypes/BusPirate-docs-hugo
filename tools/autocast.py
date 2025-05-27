# This is a python script that generates asciinema screencast documentation for the Bus Pirate terminal interface.
# Loads a list of commands to run in the Bus Pirate terminal over a serial connection.
# Input commands are one per lines, and are read from a file.
#    # tut-self-test.json
#    m # m - change to HiZ mode
#    1
#    ~ # ~ - start self-test
#    # stop
# Example script. # <filename> begins a new asciinema file, and # stop closes it.
# Other lines are commands to be sent to the Bus Pirate terminal, text after # is inserted as a marker in the asciinema file.
#
# The script uses the pyserial library to communicate with the Bus Pirate over a serial port.
# It sends the commands to the Bus Pirate and captures the output.
# The next command is sent after the previous command has completed when the >\r\n prompt is received.
#
# Captures the VT100 output to asciinema formatted text files:
# [ <timestamp>, "o", data]
# data is a string containing the data that was printed. 
# It must be valid, UTF-8 encoded JSON string as described in JSON RFC section 2.5, 
# with any non-printable Unicode codepoints encoded as \uXXXX
import argparse
from serial import Serial
import json
import time
import re
import random  # For simulating human typing
from collections import deque  # For managing the send queue

def parse_arguments():
    parser = argparse.ArgumentParser(description="Generate asciinema screencast documentation for the Bus Pirate terminal interface.")
    parser.add_argument("-p", "--port", default="/dev/ttyUSB0", help="The serial port to use (default: /dev/ttyUSB0)")
    parser.add_argument("-b", "--baudrate", type=int, default=115200, help="The baud rate to use (default: 115200)")
    parser.add_argument("-i", "--input", default="commands.txt", help="The input file containing the commands to run (default: commands.txt)")
    parser.add_argument("-o", "--output", default="../static/screencast/", help="Where to save the asciinema json files (default: ../static/screencast/)")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode (default: False)")
    return parser.parse_args()

def read_commands(input_file):
    with open(input_file, "r") as file:
        return [line.strip() for line in file] # if line.strip()

def main():
    args = parse_arguments()
    commands = read_commands(args.input)
    asciinema_file = None
    start_time = None
    timestamp = 0
    
    # States
    STATE_IDLE = 0
    STATE_SEND_COMMAND = 1
    STATE_EXECUTE_COMMAND = 2
    STATE_WAIT_FOR_PROMPT = 3
    STATE_ADDITIONAL_DELAY = 4
    STATE_END = 5

    state = STATE_IDLE  # Initial state
    send_queue = deque()
    delay_time = 0

    vt100_query = "\0337\033[999;999H\033[6n\0338"
    vt100_reply = "[24;80R"   
    vt100_data_last = "" 

    with Serial(args.port, args.baudrate, timeout=1) as serial_conn:
        if args.debug:
            print(f"Connected to {args.port} at {args.baudrate} baud.")

        output = ""            
        html_output = ""
        current_command = None  # Track the current command being processed

        while state != STATE_END:
            
            # Read data from the serial connection
            data = serial_conn.read(serial_conn.in_waiting).decode("utf-8", errors="ignore")
            if data:
                if args.debug:
                    print(data, end="")
                
                # create a timestamp for the data
                if start_time is None:
                    start_time = time.time()
                    timestamp = 0
                else:
                    timestamp = round(time.time() - start_time, 6)

                # write the data to the asciinema file
                if asciinema_file:
                    asciinema_entry = [f"{timestamp:.6f}", "o", data]
                    json.dump(asciinema_entry, asciinema_file)
                    asciinema_file.write("\n")

                # Handle VT100 query
                vt100_search = vt100_data_last + data # combine the last data with the current data to find the VT100 query
                if vt100_query in vt100_search:
                    serial_conn.write(vt100_reply.encode("utf-8"))
                    vt100_data_last = "" # reset the last data
                    if args.debug:
                        print(f"VT100 query detected")
                        print(f"Sent VT100 reply")
                else: # save the previous data to find VT100 query split over multiple reads
                    vt100_data_last = data # save the current data to find the VT100 query
                
            current_time = time.time()
            # State machine
            if(state == STATE_IDLE):
                if commands:
                    # get next line, split on # to get the command and comment
                    line = commands.pop(0)
                    if "#" in line:
                        current_command = line.split("#")[0].strip()
                        current_comment = line.split("#")[1].strip()

                        # handle control actions if command is empty
                        if current_command == "": #this is a control action
                            if current_comment == "stop":
                                
                                if asciinema_file is None:
                                    print("No asciinema file to close.")
                                    quit(1)

                                # close the asciinema file
                                try:
                                    asciinema_file.write('[' + str(round(time.time() - start_time, 6)+2) + ', "o", ""]\n')
                                    asciinema_file.close()
                                    asciinema_file = None
                                    if args.debug:
                                        print(f"Closed file.")
                                except Exception as e:
                                    print(f"Error closing file: {e}")
                                    quit(1)
                                    
                            else:
                                # create a new save file
                                if asciinema_file is not None:
                                    print("Asciinema file already open. Closing it first.")
                                    try:
                                        asciinema_file.write('[' + str(round(time.time() - start_time, 6)+2) + ', "o", ""]\n')
                                        asciinema_file.close()
                                        asciinema_file = None
                                    except Exception as e:
                                        print(f"Error closing file: {e}")
                                        quit(1)
                                try:
                                    asciinema_file = open(args.output + current_comment.strip()+'.json', "w")
                                    start_time = None
                                    timestamp = 0
                                    asciinema_file.write('{"version": 2, "width": 80, "height": 24, "timestamp": ' + str(time.time()) + ', "env": {"SHELL": "/bin/bash", "TERM": "xterm-256color"}}\n')
                                    char = "\x02"
                                    serial_conn.write(char.encode("utf-8"))
                                    state = STATE_ADDITIONAL_DELAY
                                    delay_time = current_time + 1.0
                                    if args.debug:
                                        print(f"Saving output to {current_comment}.")
                                except Exception as e:
                                    print(f"Error opening {current_comment}: {e}")
                                    quit(1)
                            continue

                        # insert the comment in ansiinema file as marker
                        # create a timestamp for the data
                        if start_time is None:
                            start_time = time.time()
                            timestamp = 0
                        else:
                            timestamp = round(time.time() - start_time, 6)

                        # write the data to the asciinema file
                        asciinema_entry = [f"{timestamp:.6f}", "m", current_comment]
                        json.dump(asciinema_entry, asciinema_file)
                        asciinema_file.write("\n")                            
                    else:
                        current_command = line

                    if current_command != "":
                        send_queue.extend(current_command.strip())
                        state = STATE_SEND_COMMAND
                        delay_time = 0
                    else:
                        state = STATE_EXECUTE_COMMAND
                        delay_time = current_time + 1.0

                    if args.debug:
                        print(f"Queueing command: '{current_command}'")
                else:
                    state = STATE_END

            elif(state == STATE_SEND_COMMAND):
                if send_queue and current_time >= delay_time:
                    char = send_queue.popleft()
                    serial_conn.write(char.encode("utf-8"))
                    delay_time = current_time + random.uniform(0.05, 0.2)

                    if not send_queue:
                        state = STATE_EXECUTE_COMMAND
                        delay_time = current_time + .5

            elif(state == STATE_EXECUTE_COMMAND):
                # Check if the newline is scheduled and the time has passed
                if current_time >= delay_time:
                    serial_conn.write("\r\n".encode("utf-8"))
                    #if args.debug:
                        #print("Sent: \\r\\n")
                    delay_time = 0
                    state = STATE_WAIT_FOR_PROMPT

            elif(state == STATE_WAIT_FOR_PROMPT):
                # Handle prompt detection
                if "\x03" in data:
                    if args.debug:
                        print(f"Prompt detected")
                    state = STATE_ADDITIONAL_DELAY
                    delay_time = current_time + .5
                    if args.debug:
                        print(f"Scheduled additional delay of 1 second after prompt detection.")
            
            elif(state == STATE_ADDITIONAL_DELAY):
                # Check if the additional delay is active and skip queuing the next command until it ends
                if current_time >= delay_time:
                    delay_time = 0
                    state = STATE_IDLE
                    if args.debug:
                        print(f"Additional delay completed.")

            elif(state == STATE_END):
                if args.debug:
                    print(f"End of commands reached.")


if __name__ == "__main__":
    main()