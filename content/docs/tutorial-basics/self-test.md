+++
weight = 30700
title = 'Self-test Procedure'
+++

Every Bus Pirate is lovingly tested by our crack team before it ships, but problems can always occur in transit or over time. The firmware self-test can help determine if your Bus Pirate is in good working order. 

The detailed self-test is primarily useful in three situations:
- For prototype testing. We may have done a poor job solder paste stenciling or the Neoden 4 did its flick and chase thing. 
- Production testing. We need to make sure no failed components are on the board before we ship.
- Disaster assessment. Something went wrong while hacking and now a pin doesn't work.

## Overview

|Command | Description |
|---|---|
|```~```|Start the self-test.|

## Setup the self-test

- Disconnect any devices from the Bus Pirate. An external device will interfere with the test and could be damaged by the voltage used on the pins.

{{% alert context="danger" %}}
Disconnect any devices before performing the self-test.
{{% /alert %}}

## Start the self-test

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">SPI></span> m
<span style="color:#bfa530">
<span style="color:#bfa530">Mode selection</span></span>
 1. <span style="color:#bfa530">HiZ</span>
 2. <span style="color:#bfa530">UART</span>
 3. <span style="color:#bfa530">I2C</span>
 4. <span style="color:#bfa530">SPI</span>
 5. <span style="color:#bfa530">LED</span>
 6. <span style="color:#bfa530">DUMMY1</span>
 x. <span style="color:#bfa530">Exit</span>
<span style="color:#96cb59">Mode ></span> 1
<span style="color:#bfa530">Mode:</span> HiZ
<span style="color:#96cb59">HiZ></span> ~
<span style="color:#bfa530">SELF TEST STARTING</span>
{{< /term >}}

{{% alert context="warning" %}}
Ensure the Bus Pirate is in HiZ mode before starting the self-test.
{{% /alert %}}

- Ensure the Bus Pirate is in HiZ mode. Type ```m``` and press ```enter```. Select option ```1``` to enter HiZ mode.
- Begin the self-test. Type ```~``` followed by ```enter``` in the terminal. Self-test is available in HiZ mode only.
- Press the Bus Pirate button when prompted.

## Results

### Success

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#bfa530">PASS :)</span>
<span style="color:#96cb59">HiZ></span> 
{{< /term >}}

Hopefully you see a happy Bus Pirate with no errors. Your hardware seems to be in working order. 

{{% alert context="info" %}}
If you're still having a problem, could it be a firmware bug? Please let us know [in the forum](https://forum.buspirate.com/).
{{% /alert %}}

### Errors

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#bfa530">PSU ENABLE: CODE 3. ERROR!
...
ERRORS: 1
FAIL! :(</span>
{{< /term >}}

If your self-test reports errors, we are eager to know. Please [post the full self-test results in the forum](https://forum.buspirate.com/) and we'll have a look.

## Self-test steps

Let's break down the self-test step by step.

### Verify NAND flash

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">HiZ></span> ~
No file system!
Format the Bus Pirate NAND flash?
ALL DATA WILL BE DESTROYED!
 y/n> y
Format succeeded! 
Storage mounted: 0.10 GB FAT16
FORMAT NAND FLASH: OK
{{< /term >}}

First the Bus Pirate checks the connection and health of the onboard NAND flash storage.
- If the NAND flash is blank or corrupted, you will be prompted to format the chip

{{% alert context="danger" %}}
You should not normally see this message. Formatting is performed during production testing. Answering yes will destroy all data on the NAND flash. Please [post a bug report in the forum](https://forum.buspirate.com/) if you see this message.
{{% /alert %}}

### System tests

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#bfa530">SELF TEST STARTING
DISABLE IRQ: OK
ADC SUBSYSTEM: VUSB  5.03V OK
FLASH STORAGE: OK
PSU ENABLE: OK</span>
{{< /term >}}

- **DISABLE IRQ** - The Bus Pirate disables all interrupts during the test.
- **ADC SUBSYSTEM** - A test of the analog voltage measurement system and the IO expanders. Can the Bus Pirate change between analog inputs, and does the USB voltage measurement make sense? VUSB should be somewhere between 4.75 and 5.25 volts. Components include the RPi chip connections, 595 IO expander chips, 245 level translator, 4067 analog mux, an op-amp and various passive component connections.
- **FLASH STORAGE** - Try to mount the onboard storage. 
- **PSU ENABLE** - Test the programmable power supply unit. Output is set to 3.3volts with a 50mA current limit, after a delay the voltage is measured. Tests op-amps, comparator, transistors, FETs and several other components in the PPSU.

{{% alert context="warning" %}}
Prototype boards (REV8 and below) use a TF flash card for storage. If a formatted flash card isn't installed the flash storage section of the self-test will fail.
{{% /alert %}}

### BIO float
{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#bfa530">BIO FLOAT TEST (SHOULD BE 0/&lt;0.2V)
BIO0 FLOAT: 0/0.03V OK
BIO1 FLOAT: 0/0.03V OK
BIO2 FLOAT: 0/0.03V OK
BIO3 FLOAT: 0/0.03V OK
BIO4 FLOAT: 0/0.03V OK
BIO5 FLOAT: 0/0.03V OK
BIO6 FLOAT: 0/0.03V OK
BIO7 FLOAT: 0/0.04V OK</span>
{{< /term >}}

- **BIOx FLOAT** - The buffered IO pins are set as floating inputs. 
- The 1M ohm pull-down resistors should hold the pins close to ground (logic value 0, \<0.2volts). 
- Tests the RPi chip, IO buffers, pull-down resistors, and the analog connection to the IO pins. 
- If two adjacent pins are stuck, for example by a solder bridge, the self-test will attempt to determine which pins are effected.

### BIO high
{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#bfa530">BIO HIGH TEST (SHOULD BE >3.0V)
BIO0 HIGH: 3.29V OK
BIO1 HIGH: 3.29V OK
BIO2 HIGH: 3.29V OK
BIO3 HIGH: 3.29V OK
BIO4 HIGH: 3.29V OK
BIO5 HIGH: 3.29V OK
BIO6 HIGH: 3.29V OK
BIO7 HIGH: 3.29V OK</span>
{{< /term >}}

- **BIOx HIGH** - The buffered IO pins are set as high outputs. 
- The voltage should be close to the PPSU output (logic value 1, >3.0volts). 
- Tests the RPi chip, IO buffers and the analog connection to the IO pins. 
- If two adjacent pins are stuck, for example by a solder bridge, the self-test will attempt to determine which pins are effected.

### BIO low
{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#bfa530">BIO LOW TEST (SHOULD BE &lt;0.2V)
BIO0 LOW: 0.03V OK
BIO1 LOW: 0.03V OK
BIO2 LOW: 0.03V OK
BIO3 LOW: 0.03V OK
BIO4 LOW: 0.03V OK
BIO5 LOW: 0.03V OK
BIO6 LOW: 0.03V OK
BIO7 LOW: 0.03V OK</span>
{{< /term >}}

- **BIOx LOW** - The buffered IO pins are set as low outputs. 
- The voltage should be close to ground (logic value 0, \<0.2volts). 
- Tests the RPi chip, IO buffers and the analog connection to the IO pins.
- If two adjacent pins are stuck, for example by a solder bridge, the self-test will attempt to determine which pins are effected.

### BIO pull-up high
{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#bfa530">BIO PULL-UP HIGH TEST (SHOULD BE >3.0V)
BIO0 PU-HIGH: 1/3.22V OK
BIO1 PU-HIGH: 1/3.22V OK
BIO2 PU-HIGH: 1/3.23V OK
BIO3 PU-HIGH: 1/3.26V OK
BIO4 PU-HIGH: 1/3.26V OK
BIO5 PU-HIGH: 1/3.22V OK
BIO6 PU-HIGH: 1/3.25V OK
BIO7 PU-HIGH: 1/3.25V OK</span>
{{< /term >}}

- **BIOx PU-HIGH** - The pull-up resistors are enabled and the buffered IO pins are set as inputs. 
- The voltage should be close to the PPSU output (logic value 1, >3.0volts). 
- Tests the RPi chip, pull-up resistors, 4066, IO buffers and the analog connection to the IO pins.
- If two adjacent pins are stuck, for example by a solder bridge, the self-test will attempt to determine which pins are effected.

### BIO pull-up low
{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#bfa530">BIO PULL-UP LOW TEST (SHOULD BE &lt;0.5V)
BIO0 PU-LOW: 0.13V OK
BIO1 PU-LOW: 0.14V OK
BIO2 PU-LOW: 0.14V OK
BIO3 PU-LOW: 0.14V OK
BIO4 PU-LOW: 0.14V OK
BIO5 PU-LOW: 0.13V OK
BIO6 PU-LOW: 0.14V OK
BIO7 PU-LOW: 0.14V OK</span>
{{< /term >}}

- **BIOx PU-LOW** - The pull-up resistors are enabled and the buffered IO pins are set to output/ground. 
- The voltage should be close to ground (logic value 0, \<0.5volts). 
- Tests the RPi chip, pull-up resistors, 4066, IO buffers and the analog connection to the IO pins.
- If two adjacent pins are stuck, for example by a solder bridge, the self-test will attempt to determine which pins are effected.

### Current override
{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#bfa530">CURRENT OVERRIDE: OK</span>
{{< /term >}}

- **CURRENT OVERRIDE** - Tests the pin for overriding the current limit digital fuse. Current limit override is enabled. A very low current limit is set with the pull-ups enabled and the BIO pins grounded. The Bus Pirate checks that the power supply is still on, despite the blown fuse.
- Tests the PPSU, comparator, transistors, fets, etc.


### Current limit
{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#bfa530">CURRENT LIMIT TEST: OK</span>
{{< /term >}}

- **CURRENT LIMIT TEST** - A very low current limit is set with the pull-ups enabled and the BIO pins grounded. The Bus Pirate waits up to 2 seconds for the digital fuse to blow.
- Tests the PPSU, comparator, transistors, fets, etc.

### Just one button
{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#bfa530">PUSH BUTTON TO COMPLETE: OK
</span>
{{< /term >}}

- **PUSH BUTTON TO COMPLETE** - Press the Bus Pirate button to complete the test. The Bus Pirate will pause and wait indefinitely. 
- Tests RPi chip, switch.
