+++
weight = 70500
title = 'UART/Serial Protocol'
+++

-   **Bus:** [UART](http://en.wikipedia.org/wiki/Serial_uart),
    [MIDI](http://en.wikipedia.org/wiki/Musical_Instrument_Digital_Interface)
    (universal asynchronous receiver transmitter)
-   **Connections:** two pins (RX/TX) and ground
-   **Output type:** 1.65-5volts. Powered by onboard supply or an external voltage on the VOUT/VREF pin
-   **Maximum Voltage:** 5volts

{{% alert context="info" %}}
UART is also known as the common PC serial port. The PC serial port
operates at full RS232 voltage levels (-13volts to +13volts) though,
which are not compatible with the Bus Pirate.
{{% /alert %}}

## Connections
| Bus Pirate | Direction                     | Circuit | Description   |
|------------|--------------------------|---------|---------------|
| TX       | <font size="+2">→</font> | RX    | Bus Pirate Transmit   |
| RX        | <font size="+2">←</font> | TX     | Bus Pirate Receive  |
| GND        | <font size="+2">⏚</font> | GND     | Signal Ground |

Connect the Bus Pirate transmit pin (TX) to the UART device receive
pin (RX). Connect the Bus Pirate receive pin (RX) to the UART
device transmit pin (TX).

## Configuration options

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#bfa530">UART speed</span>
 1200, 2400, 4800, 19200, 38400, 57600, 115200 etc
 x. <span style="color:#bfa530">Exit</span>
<span style="color:#96cb59">Baud (</span>115200*<span style="color:#96cb59">) ></span> 
<span style="color:#bfa530">Data bits</span>
 5 to 8 bits
 x. <span style="color:#bfa530">Exit</span>
<span style="color:#96cb59">Bits (</span>8*<span style="color:#96cb59">) ></span> 
<span style="color:#bfa530">Parity</span>
 1. <span style="color:#bfa530">None*</span>
 2. <span style="color:#bfa530">Even</span>
 3. <span style="color:#bfa530">Odd</span>
 x. <span style="color:#bfa530">Exit</span>
<span style="color:#96cb59">Parity (</span>1<span style="color:#96cb59">) ></span> 
<span style="color:#bfa530">Stop bits</span>
 1. <span style="color:#bfa530">1*</span>
 2. <span style="color:#bfa530">2</span>
 x. <span style="color:#bfa530">Exit</span>
<span style="color:#96cb59">Bits (</span>1<span style="color:#96cb59">) ></span> 
<span style="color:#bfa530">Actual speed: 115207 baud</span>
<span style="color:#bfa530">Mode:</span> UART
<span style="color:#96cb59">UART></span> 
{{< /term >}}

## Syntax

|Command| Description  |
|---------|-------|
| [      | Open UART, use ```r``` to read bytes. |
| \{       | Open UART, display data as it arrives asynchronously. |
| \] or } | Close UART.  |
| r       | Check UART for byte, or fail if empty. (r:1…255 for bulk reads) |
| 0b      | Write this binary value. Format is 0b00000000 for a byte, but partial bytes are also fine: 0b1001.|
| 0x      | Write this HEX value. Format is 0x01. Partial bytes are fine: 0xA. A-F can be lower-case or capital letters. |
| 0-255   | Write this decimal value. Any number not preceded by 0x or 0b is interpreted as a decimal value. |
| ```space```| Value delimiter. Use a space to separate numbers. No delimiter is required between non-number values: \{0xa6 0 0 16 5 0b111 0xaF rrrr}. |
| \(#\)   | Run macro, (0) for macro list. |


## Commands

Bus Pirate 5 has global commands available everywhere, and mode commands specific to the currently selected mode. Type ```help``` to see all commands in every mode, or ```help mode``` for the currently available mode commands.

{{% alert context="info" %}}
Most Bus Pirate commands have help. Add the ```-h``` flag to any command to see the latest available options and usage examples. 
{{% /alert %}}

### bridge

Transparent UART ```bridge```. Bidirectional UART pass-through to interact with other serial devices from inside the Bus Pirate terminal. Press the Bus Pirate button to exit.

#### Help

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">UART></span> bridge -h
usage:
<span style="color:#bfa530">bridge	[-h(elp)] [-t(oolbar)]</span>
<span style="color:#bfa530">Transparent UART bridge: bridge</span>
<span style="color:#bfa530">Exit: press Bus Pirate button</span>

<span style="color:#bfa530">open UART with raw data IO, usb to serial bridge mode</span>
<span style="color:#96cb59">-t</span>	<span style="color:#bfa530">ENABLE toolbar while bridge is active (default: disabled)</span>
<span style="color:#96cb59">-h</span>	<span style="color:#bfa530">Get additional help</span>

<span style="color:#96cb59">UART></span> 
{{< /term >}} 
 

{{% alert context="info" %}}
Use ```bridge -h``` to see the latest options and features.
{{% /alert %}}

### gps 
Most GPS modules output [NMEA sentences](https://gpsd.gitlab.io/gpsd/NMEA.html) through a serial UART. The ```gps``` command decodes common sentences using [minmea](https://github.com/kosma/minmea). The raw data and decoded data are printed in the terminal. Press any key to exit.

#### Help

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">UART></span> gps -h
usage:
<span style="color:#bfa530">gps	[-h(elp)]</span>
<span style="color:#bfa530">Decode GPS NMEA packets: gps</span>
<span style="color:#bfa530">Exit: press any key</span>

<span style="color:#bfa530">parse NMEA GPS data</span>
<span style="color:#96cb59">-h</span>	<span style="color:#bfa530">Get additional help</span>

<span style="color:#96cb59">UART></span> 
{{< /term >}}

{{% alert context="info" %}}
Use ```gps -h``` to see the latest options and features.
{{% /alert %}}

<!--

                                                             |
| 2   | Live raw UART monitor. Any key exits. [More](http://dangerousprototypes.com/2009/10/19/uart-mode-updates/) |
| 3   | Transparent UART bridge with flow control.                                                                 |



### Live UART monitor

UART>(2)**<<<macro 2, UART monitor** Raw UART input. Space to
exit. UART> The UART monitor macro (2) shows a live display of
UART input as raw byte values without any type of formatting. Press any
key to exit the live monitor. This mode works best with a terminal that
can display raw byte values in a variety of formats.

This macro is like the transparent UART macro (1) but without
transmission abilities, and it can be exited with a key press. It’s
useful for monitoring high-speed UART input that causes buffer overrun
errors in other modes.
-->
## MIDI

[MIDI](http://en.wikipedia.org/wiki/Musical_Instrument_Digital_Interface)
is a command set used by electronic (music) instruments. It travels over
a standard serial UART configured for 31250bps/8/n/1.

MIDI is a ring network, each node has an input and output socket. Each
node passes messages to the next in the ring. The input and outputs are
opto-isolated. The signaling is at 5volts, 5ma (current-based
signaling). An adapter is required: [example
1](https://www.compuphase.com/electronics/midi_rs232.htm), [example
2](https://midi.org/specs).



<!--

For macros and modes with flow control: CTS is on the CS pin (PIC input
from external circuit is passed to FTDI USB->serial chip). RTS is on the
CLOCK pin (PIC output mirrors output from FTDI chip).
-->
