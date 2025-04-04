
+++
weight = 70400
title = '2-Wire Protocol'
+++

-   **Bus:** 2 wire bus with bidirectional data (SDA) line and a clock (SCL) line
-   **Connections:** two pins (SDA/SCL) and ground. An additional pin is reserved for RESET, and is controlled by the ```{```/```}``` commands.
-   **Output type:** open drain/open collector
-   **Pull-up resistors:** always required (2K - 10K ohms)
-   **Maximum voltage:** 5volts

2-wire is a generic 8bit protocol mode with a bidirectional data line (SDA) and a clock line (SCL). 2-wire can be used to interface with SLE4442 smart cards, half-duplex SPI devices and other 2 wire busses that don't use a full I2C implementation.

## Connections

| Bus Pirate | Direction                     | Circuit | Description   |
|------------|--------------------------|---------|---------------|
| SDA       | <font size="+2">↔</font> | SDA     | Serial Data   |
| SCL        | <font size="+2">→</font> | SCL     | Serial Clock  |
| RST        | <font size="+2">→</font> | RST     | Reset signal for some devices  |
| GND        | <font size="+2">⏚</font> | GND     | Signal Ground |

## Configuration options

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#bfa530">2WIRE speed</span>
 1kHz to 1000kHz
 x. <span style="color:#bfa530">Exit</span>
<span style="color:#96cb59">kHz (</span>400kHz*<span style="color:#96cb59">) ></span> 20
<span style="color:#bfa530">Mode:</span> 2WIRE
<span style="color:#96cb59">2WIRE></span> 
{{< /term >}}

**Pull-up resistors**

2-Wire is an open-collector bus, it requires pull-up resistors to hold the
clock and data lines high and create the data '1'. In 2-Wire mode, the Bus Pirate doesn't
output high, it only pulls low. Without pull-up resistors there can
never be a '1'. 

Enable the Bus Pirate onboard pull-up resistors with the ```P``` command.

{{% alert context="info" %}}
- 2-Wire requires pull-up resistors to hold the clock and data lines high.
- Without pull-up resistors there can never be a '1'. 
- Enable the Bus Pirate onboard pull-up resistors with the ```P``` command.
{{% /alert %}}

## Syntax

|Command|Description|
|-------|-----------|
| [ | Issue I2C-style start condition. Some devices don't follow the I2C standard, but still use a similar START condition. |
| ] | Issue I2C-style stop condition. Some devices don't follow the I2C standard, but still use a similar STOP condition.|
| \{ | RST/reset pin **high** |
| } | RST/reset pin **low** |
| r       | Read one byte, send ACK. (r:1…255 for bulk reads)|
| 0b      | Write this binary value, check ACK. Format is 0b00000000 for a byte, but partial bytes are also fine: 0b1001.|
| 0x      | Write this HEX value, check ACK. Format is 0x01. Partial bytes are fine: 0xA. A-F can be lower-case or capital letters. |
| 0-255   | Write this decimal value, check ACK. Any number not preceded by 0x or 0b is interpreted as a decimal value. |
| ```space```| Value delimiter. Use a space to separate numbers. No delimiter is required between non-number values: \{0xa6 0 0 16 5 0b111 0xaF rrrr}. |





## Commands

Bus Pirate 5 has global commands available everywhere, and mode commands specific to the currently selected mode. Type ```help``` to see all commands in every mode, or ```help mode``` for the currently available mode commands.

### sle4442

The ```sle4442``` command in the Bus Pirate's 2-WIRE mode automates the process of reading, writing and unlocking a [SLE4442 smart card](/devices/sle4442).

#### Help

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">2WIRE></span> sle4442 -h
usage:
<span style="color:#bfa530">sle4442 [init|dump|unlock|write|erase|psc]
	[-a &#x003c;address&#x003e;] [-v &#x003c;value&#x003e;] [-p &#x003c;current psc&#x003e;] [-n &#x003c;new psc&#x003e;] [-h(elp)]</span>
<span style="color:#bfa530">Initialize and probe: sle4442 init</span>
<span style="color:#bfa530">Dump contents: sle4442 dump</span>
<span style="color:#bfa530">Unlock card: sle4442 unlock -p 0xffffff</span>
<span style="color:#bfa530">Write a value: sle4442 write -a 0xff -v 0x55</span>
<span style="color:#bfa530">Erase memory: sle4442 erase</span>
<span style="color:#bfa530">Update PSC: sle4442 psc -p 0xffffff -n 0x000000</span>

<span style="color:#bfa530">SLE4442 smart card interface</span>
<span style="color:#96cb59">init</span>	<span style="color:#bfa530">Initialize card with ISO7816-3 ATR. Default action</span>
<span style="color:#96cb59">dump</span>	<span style="color:#bfa530">Display main, security and protect memory</span>
<span style="color:#96cb59">unlock</span>	<span style="color:#bfa530">Unlock card with Programmable Security Code (PSC)</span>
<span style="color:#96cb59">write</span>	<span style="color:#bfa530">Write data to card (requires unlock)</span>
<span style="color:#96cb59">erase</span>	<span style="color:#bfa530">Erase data from range 0x32-0x255 (requires unlock)</span>
<span style="color:#96cb59">psc</span>	<span style="color:#bfa530">Change Programmable Security Code (PSC)</span>
<span style="color:#96cb59">-a</span>	<span style="color:#bfa530">Write address flag</span>
<span style="color:#96cb59">-v</span>	<span style="color:#bfa530">Write value flag</span>
<span style="color:#96cb59">-p</span>	<span style="color:#bfa530">Current Programmable Security Code (PSC) flag</span>
<span style="color:#96cb59">-n</span>	<span style="color:#bfa530">New Programmable Security Code (PSC) flag</span>

<span style="color:#96cb59">2WIRE></span> 
{{< /term >}} 
 

{{% alert context="info" %}}
Use ```sle4442 -h``` to see the latest options and features.
{{% /alert %}}

Most Bus Pirate commands have help and usage examples. Add the -h flag to any command to see the available options and examples.

#### Options and flags

|Option|Description|
|------|-----------|
|sle4442 init|Initialize and probe the card Answer To Reset|
|sle4442 dump|Display main, security and protect memory|
|sle4442 unlock|Unlock card with Programmable Security Code (PSC)|
|sle4442 write|Write data to card (requires unlock)|
|sle4442 erase|Erase data from range 0x32-0x255 (requires unlock)|
|sle4442 psc|Change Programmable Security Code (PSC)|

|Flag|Description|
|------|-----------|
|-a|Write address flag|
|-v|Write value flag|
|-p|Current Programmable Security Code (PSC) flag|
|-n|New Programmable Security Code (PSC) flag|

#### Reset SLE4442 card, decode ATR response
{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">2WIRE></span> sle4442 init
--SLE44xx decoder--
ATR: 0xa2 0x13 0x10 0x91
Protocol Type: S 10
Structure Identifier: General Purpose (Structure 1)
Read: Read to end
Data Units: 256
Data Units Bits: 8
Security memory: 0x07 0x00 0x00 0x00
Remaining attempts: 3 (0x7)

{{< /term >}}

```sle4442``` and ```sle4442 init``` reset the card and decodes the Answer To Reset (ATR) response.

#### Dump SLE4442 card memory
{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">2WIRE></span> sle4442 dump
--SLE44xx decoder--
ATR: 0xa2 0x13 0x10 0x91
Protocol Type: S 10
Structure Identifier: General Purpose (Structure 1)
Read: Read to end
Data Units: 256
Data Units Bits: 8
Security memory: 0x07 0x00 0x00 0x00
Remaining attempts: 3 (0x7)
Protection memory: 0xff 0xff 0xff 0xff
Memory:
0xa2 0x13 0x10 0x91 0xff 0xff 0x81 0x15 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xd2 0x76 0x00 0x00 0x04 0x00 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 
{{< /term >}}

```sle4442 dump``` reads and displays the main, security and protection memory areas.

#### Unlock SLE4442 card with passcode

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">2WIRE></span> sle4442 unlock -p 0x123456
--SLE44xx decoder--
ATR: 0xa2 0x13 0x10 0x91
Protocol Type: S 10
Structure Identifier: General Purpose (Structure 1)
Read: Read to end
Data Units: 256
Data Units Bits: 8
Security memory: 0x07 0x12 0x34 0x56
Remaining attempts: 3 (0x7)
Unlocking with PSC: 0x123456
Using free security bit: 0x03
Card unlocked, security bits reset
Security memory: 0x07 0x12 0x34 0x56
Remaining attempts: 3 (0x7)

{{< /term >}}

```sle4442 unlock``` unlocks the card using the Programmable Security Code (PSC). Use the ```-p``` flag to specify the PSC. 

{{% alert context="info" %}}
New cards usually have a default PSC of 0xffffff.
{{% /alert %}}

#### Write data to SLE4442 card

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">2WIRE></span> sle4442 write -a 0xff -v 0x88
--SLE44xx decoder--
ATR: 0xa2 0x13 0x10 0x91
Protocol Type: S 10
Structure Identifier: General Purpose (Structure 1)
Read: Read to end
Data Units: 256
Data Units Bits: 8
Security memory: 0x07 0x12 0x34 0x56
Remaining attempts: 3 (0x7)
Writing 0x88 to 0xff

{{< /term >}}

```sle4442 write``` writes a single byte of data to the card. Specify the address with the ```-a``` flag and the data value with the ```-v``` flag.

{{% alert context="warning" %}}
The card must be unlocked before writing data.
{{% /alert %}}

#### Change SLE4442 passcode/PSC

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">2WIRE></span> sle4442 psc -p 0x123456 -n 0xffffff
--SLE44xx decoder--
ATR: 0xa2 0x13 0x10 0x91
Protocol Type: S 10
Structure Identifier: General Purpose (Structure 1)
Read: Read to end
Data Units: 256
Data Units Bits: 8
Security memory: 0x07 0x12 0x34 0x56
Remaining attempts: 3 (0x7)
Unlocking with PSC: 0x123456
Using free security bit: 0x03
Card unlocked, security bits reset
Security memory: 0x07 0x12 0x34 0x56
Remaining attempts: 3 (0x7)
Updating with PSC: 0xFFFFFF
PSC updated to: 0xFFFFFF
Security memory: 0x07 0xff 0xff 0xff
Remaining attempts: 3 (0x7)

{{< /term >}}

```sle4442 psc``` changes the Programmable Security Code (PSC). Use the ```-p``` flag to specify the current PSC and the ```-n``` flag to specify the new PSC.
