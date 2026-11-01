+++
weight = 60400
title = 'Bus Pirate v3 Unbrick'
+++

![](/images/docs/fw/bpv3-unbrick-setup.jpg)

A Bus Pirate v3 loads new firmware over USB through its bootloader. When the flash is blank or broken, or the PIC was replaced, there is no bootloader to talk to, and getting it back used to take a PIC programmer like a PICkit.

The "Bus Pirate v3 unbrick" binmode writes bootloader v4.6 to the PIC24FJ64GA002 of the Bus Pirate v3 through its ICSP header. Then pirate-loader loads the firmware over the Bus Pirate v3's own USB port.

## Connections

|Bus Pirate|Bus Pirate v3|Description|
|-|-|-|
|IO7|JP2-1 (PGC)|Programming clock|
|IO6|JP2-2 (PGD)|Programming data|
|GND|JP2-3 (GND)|Ground|
|VOUT|JP2-4 (3V3)|Optional, reference for the IO pins|
|IO5|JP2-5 (MCLR)|Reset|

Connect the Bus Pirate to the ICSP header JP2 of the Bus Pirate v3 according to the table above. The Bus Pirate v3 runs from its own USB cable the whole time.

JP2 pin 4 can stay unconnected. The Bus Pirate power supply then puts 3.3 volts on VOUT, with a 50 mA limit, for its own IO pins only. With pin 4 wired to VOUT, the 3.3 volts of the Bus Pirate v3 are the reference for the IO pins and the power supply stays off.

{{% alert context="warning" %}}
JP2 pin 4 is the 3.3 volt rail of the Bus Pirate v3. While it is wired to VOUT, do not turn on the Bus Pirate power supply yourself.
{{% /alert %}}

## Write the bootloader

{{< asciicast src="/screencast/bpv3-unbrick-cast.json" poster="npt:0:19"  idleTimeLimit=2 >}}

In the Bus Pirate terminal use the ```binmode``` command and choose **8. Bus Pirate v3 unbrick: bootloader v4.6 (ICSP)**.

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">HiZ&gt;</span> binmode

 1. SUMP logic analyzer
 2. BPIO2 flatbuffer interface
 3. Arduino CH32V003 SWIO
 4. Follow along logic analyzer
 5. Legacy Binary Mode for Flashrom and AVRdude
 6. IRMAN IR decoder (LIRC, etc)
 7. AIR capture (AnalysIR, etc)
 8. Bus Pirate v3 unbrick: bootloader v4.6 (ICSP)
<span style="color:#bfa530">Select binary mode</span>
<span style="color:#96cb59">x to exit (1) &gt;</span> 8


<span style="color:#bfa530">Binmode selected:</span> Bus Pirate v3 unbrick: bootloader v4.6 (ICSP)

Writes bootloader v4.6 to a Bus Pirate v3, through its ICSP header JP2:

  <span style="color:#bfa530">JP2 pin</span>     <span style="color:#bfa530">this Bus Pirate</span>
  1 PGC       IO7
  2 PGD       IO6
  3 GND       GND
  4 3V3       VOUT, or not connected
  5 MCLR      IO5

The Bus Pirate v3 runs from its own USB cable.

Power supply: <span style="color:#53a6e6">3.30</span>V on VOUT for the IO pins
MCLR: <span style="color:#53a6e6">3.26</span>V, pulled up: the Bus Pirate v3 is powered
Lines: MCLR, PGC and PGD follow this Bus Pirate
PIC: PIC24FJ64GA002 rev B8 (DEVID 0x0447, DEVREV 0x3046)

This erases the Bus Pirate v3 flash and writes bootloader v4.6 alone: it has
no firmware afterwards, until pirate-loader loads one.
Continue?
<span style="color:#96cb59">y/n &gt;</span> y

Erasing... OK
Writing 8 rows... OK
Verifying 22016 words
<span style="color:#96cb59">[--------------------</span><span style="color:#ffee00">c</span>

<span style="color:#bfa530">Bootloader v4.6 written and verified</span> in 9.2s: 339 words, all others erased.
The Bus Pirate v3 has no firmware yet: load one with pirate-loader, over its
own USB port.
{{< /term >}}

The binmode checks the setup before it erases anything. IO5 to IO7 must be free, and the pull-up resistors are turned off. The power supply only turns on once MCLR reads high, which means the Bus Pirate v3 has power. MCLR, PGC and PGD must follow the Bus Pirate, and the PIC must answer over ICSP as a PIC24FJ64GA002.

Answer y to go on. It erases the user memory, writes the 8 rows of the bootloader and verifies all 22016 words of the flash. A failed attempt is tried again at half and then a quarter of the clock speed.

While it runs, the Bus Pirate screen labels IO5, IO6 and IO7 as MCLR, PGD and PGC, as in the photo above. Each selection does the job once and then gives the binary port back to the default binmode, so select it again for the next Bus Pirate v3.

## Load the firmware

{{< term "Bus Pirate [/dev/ttyS0]" >}}
Hold the Bus Pirate v3 in its bootloader for pirate-loader now?
This Bus Pirate keeps PGC low, as the PGC-PGD jumper does.
<span style="color:#96cb59">y/n, x to exit (Y) &gt;</span> y

The Bus Pirate v3 waits in its bootloader, with its MODE LED on.
On its serial port, run:

  pirate-loader --dev=PORT --hex=FIRMWARE.hex

With a v7.1 file pirate-loader ends with ERROR [50] at page 42: that is
expected, the firmware is complete. Press any key or the button when
pirate-loader is done.
PGC released and the Bus Pirate v3 reset: it starts its firmware, if it has one.

<span style="color:#bfa530">Active binmode:</span> SUMP logic analyzer

<span style="color:#96cb59">HiZ&gt;</span>
{{< /term >}}

Answer y and the Bus Pirate resets the Bus Pirate v3 with PGC low, so it stays in its bootloader. Run pirate-loader on the PC with the serial port of the Bus Pirate v3, not one of the Bus Pirate ports:

```bash
pirate-loader --dev=COM22 --hex=BPCOMPBZ-firmware-v7.1.12.hex
```

On Linux the port is usually `/dev/ttyUSB0`, and the program is `pirate-loader_lnx`. It is a 32-bit build, so it may need the 32-bit C library (`libc6:i386` on Debian and Ubuntu).

With a v7.1 firmware file pirate-loader writes 41 pages and ends like this:

```bash
+++++++++++++++++++++++++++++++++++++++++++
  Pirate-Loader for BP with Bootloader v4+
  Loader version: 1.0.2  OS: WINDOWS
+++++++++++++++++++++++++++++++++++++++++++

Parsing HEX file [BPCOMPBZ-firmware-v7.1.12.hex]
Found 20162 words (60486 bytes)
Fixing bootloader/userprogram jumps
Opening serial device COM22...OK
Configuring serial port settings...OK
Sending Hello to the Bootloader...OK

Device ID: PIC24FJ64GA002 [d4]
Bootloader version: 1,02
Erasing page 0, 0000...OK
Writing page 0 row 0, 0000...OK
...
Writing page 41 row 335, a780...OK
Erasing page 42, a800...ERROR [50]

Error updating firmware :(
```

The v7.1 files also carry the configuration words, in page 42, and the bootloader does not erase its own page. Every firmware page is written by then, so the error is expected.

When pirate-loader is done, press any key in the Bus Pirate terminal or the Bus Pirate button. The Bus Pirate releases PGC and resets the Bus Pirate v3, which starts its new firmware.

To load the firmware later, answer n. With no firmware the Bus Pirate v3 waits in its bootloader, so pirate-loader can load one at any time.

## Errors

{{< asciicast src="/screencast/bpv3-unbrick-error-cast.json" poster="npt:0:07"  idleTimeLimit=2 >}}

Here the Bus Pirate power supply was still on at 5 volts:

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#bf3030">Error:</span> the power supply is on at <span style="color:#53a6e6">5.00</span>V, VOUT <span style="color:#53a6e6">4.86</span>V, and the Bus Pirate v3
runs at 3.3V. Turn it off with 'm hiz' and select this binmode again.

<span style="color:#bfa530">Active binmode:</span> SUMP logic analyzer

<span style="color:#96cb59">HiZ&gt;</span>
{{< /term >}}

Problems with the setup stop the binmode before the erase, so nothing is written. Fix the cause and answer y to try again, or select the binmode again.

|Error|Cause|
|-|-|
|no target, MCLR (IO5) is at...|The Bus Pirate v3 has no power, or the MCLR wire is loose|
|IO6 is in use by...|Another mode or command uses the pin|
|the power supply is on at...|The power supply was already on at another voltage. Turn it off with ```m hiz```|
|PGC (IO7) is at... while driven low|A short, or another programmer still connected to JP2|
|the PIC does not answer over ICSP|PGC and PGD are swapped, loose or too long|

When an attempt fails after the erase, the flash of the Bus Pirate v3 is not complete. The binmode keeps the Bus Pirate v3 in reset and asks to try again. If you answer n, select the binmode again before you use the Bus Pirate v3.
