+++
weight = 60100
title = 'AVRDUDE Programmer'
+++

![](/images/docs/fw/leonardo-icsp-bp-connected.png)

The Bus Pirate can serve as a programmer and dumper for AVR chips, using the command-line utility AVRDUDE. 

- [AVRDUDE command line programmer](https://github.com/avrdudes/avrdude)
- [AVRDUDESS graphical user interface](https://github.com/ZakKemble/AVRDUDESS)

For those who prefer a graphical user interface, AVRDUDESS offers a user-friendly front-end for AVRDUDE. Both tools together provide a powerful setup for working with AVR chips.

In this demo we'll program the ATmega32U4 chip found on the Arduino Leonardo through the ICSP header. 

{{% alert context="warning" %}}
Always power the AVR target board externally (e.g., via USB). It usually works better than powering it only from the Bus Pirate.
{{% /alert %}}

{{% alert context="warning" %}}
Use AVRDUDE newer than 8.3. Older versions can lose EEPROM data when writing, and can fail with "initialization failed" when the board runs a sketch that uses the SCK pin (D13 on an Arduino Uno), like Blink. Both are fixed by [#2219](https://github.com/avrdudes/avrdude/pull/2219) and [#2222](https://github.com/avrdudes/avrdude/pull/2222).
{{% /alert %}}

## Connections

![](/images/docs/fw/leonardo-icsp-pinout.png)

|Bus Pirate|Arduino Leonardo|Description|
|-|-|-|
|MISO|ICSP-1|Master In Slave Out|
|VOUT|ICSP-2|Power Supply (5 volts)|
|CLK|ICSP-3|Clock|
|MOSI|ICSP-4|Master Out Slave In|
|CS|ICSP-5(RST/RESET)|Chip Select|
|GND|ICSP-6|Ground|

Connect the Bus Pirate to the ICSP header according to the table above.

{{% alert context="info" %}}
RESET is connected to the CS pin on the Bus Pirate. The CS pin is used to reset the AVR chip.
{{% /alert %}}

## Setup
{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">HiZ></span> binmode

 1. SUMP logic analyzer
 2. BPIO2 flatbuffer interface
 3. Arduino CH32V003 SWIO
 4. Follow along logic analyzer
 5. Legacy Binary Mode for Flashrom and AVRdude
 6. IRMAN IR decoder (LIRC, etc)
 7. AIR capture (AnalysIR, etc)
<span style="color:#bfa530">Select binary mode</span>
<span style="color:#96cb59">x to exit (1) ></span> 5

<span style="color:#bfa530">Binmode selected:</span> Legacy Binary Mode for Flashrom and AVRdude
<span style="color:#bfa530">Binmode active. Terminal locked</span>
{{< /term >}}

In the Bus Pirate terminal use the ```binmode``` command to select the "Legacy Binary Mode for Flashrom and AVRdude".

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#bfa530">Set OUTPUT HOLD(IO2) &amp; WP(IO3) pins? (no=INPUT)</span>
<span style="color:#96cb59">y/n, x to exit (Y) ></span> n

<span style="color:#bfa530">Power supply
Volts (0.80V-5.00V)</span>
<span style="color:#96cb59">x to exit (3.30) ></span> 5

<span style="color:#bfa530">Maximum current (0mA-500mA)</span>
<span style="color:#96cb59">x to exit (200.00) ></span> 150

<span style="color:#bfa530">Power supply set to 5.00V, 150mA</span>

Done! Just execute flashrom or avrdude using the binary com port
To exit: press the button, or type 'q' here and confirm with 'y'.
Either way the Bus Pirate resets on exit.
{{< /term >}}

First it asks about the HOLD and WP pins: answer n, they are not used here. Then select 5 volts and a current limit of 150 mA.

The terminal is locked in this mode. To exit, press the button, or type q and confirm with y.

{{% alert context="warning" %}} 
Arduino Leonardo runs at 5 volts. Make sure the Bus Pirate power supply is set to 5 volts.
{{% /alert %}}

## Dumping Flash memory

### Command Line

```bash
avrdude -c buspirate -P COM5 -p m32u4 -U flash:r:dump.bin:r
```
This command uses avrdude to read the flash memory of the ATmega32U4 and saves it to a file named `dump.bin`.

- The correct COM/serial port is the Bus Pirate binary interface, this **is not the same** as the terminal serial port used to enter binmode.
- For Linux, the serial port usually starts with `/dev/ttyUSB`

```bash
attempting to initiate BusPirate binary mode ...
avrdude: paged flash write enabled
avrdude: AVR device initialized and ready to accept instructions
avrdude: device signature = 0x1e9587 (probably m32u4)

avrdude: processing -U flash:r:dump.bin:r
avrdude: reading flash memory ...
Reading | ################################################## | 100% 42.14 s
avrdude: writing output file dump.bin

avrdude done.  Thank you.
```
### AVRDUDESS

![](/images/docs/fw/avrdudess.png)

Using AVRDUDESS is easy and straightforward. Just select:

- "The Bus Pirate" as the programmer
- ATmega32U4 as the target (MCU)
- Port COM (the port where the Bus Pirate binmode is connected)
- Baud rate: 115200

Select "Read" and click "Go" button to dump the flash memory.

{{% alert context="warning" %}} 
Never select "The Bus Pirate bitbang interface, supports TPI" as the programmer. It will not work.
{{% /alert %}}




