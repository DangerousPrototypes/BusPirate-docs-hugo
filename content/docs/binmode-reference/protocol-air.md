+++
title = "aIR AnalysIR RX/TX"
description = "AnalysIR Infrared RX/TX"
icon = "article"
date = "2023-05-22T00:27:57+01:00"
lastmod = "2023-05-22T00:27:57+01:00"
draft = false
toc = true
weight = 80500
+++

The AIR binary mode turns the Bus Pirate and the [IR Toy plank]({{< relref "/docs/overview/infrared-toy-v3" >}}) into an infrared capture and transmit device for [AnalysIR]({{< relref "/docs/software/analysir" >}}). It speaks the serial protocol of the A.IR Shield Nano, AnalysIR's own hardware, so in AnalysIR choose **Source**, **A.IR Shield Nano**.

This page documents the protocol for anyone writing their own software. To capture signals with AnalysIR, follow the [AnalysIR guide]({{< relref "/docs/software/analysir" >}}).

## Capabilities

- Receive: marks and spaces in µs, up to 65,535µs each
- The carrier frequency of each signal, measured with the learner receiver
- Transmit: signals sent as aIR text, each with its own carrier frequency

## Enable AIR mode

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
<span style="color:#96cb59">x to exit (1) ></span> 7


<span style="color:#bfa530">Binmode selected:</span> AIR capture (AnalysIR, etc)

<span style="color:#bfa530">Binmode active. Terminal locked</span>
{{< /term >}}

Use the ```binmode``` command and choose **7. AIR capture (AnalysIR, etc)**. The Bus Pirate:

- switches to HiZ mode
- turns on the 5 volt power supply
- sets up the pins below
- locks the terminal

To leave AIR mode, unplug the Bus Pirate and plug it back in.

|Pin|Label|Direction|Use|
|-|-|-|-|
|IO0| |Output|Used internally. Leave it unconnected|
|IO1|LERN|Input|20-60kHz learner, measures the carrier frequency|
|IO4|IRTX|Output|IR LEDs, carrier modulated|
|IO5|38k|Input|36-40kHz demodulator, low while IR is received|

AIR mode listens with the 36-40kHz demodulator. For the 56kHz demodulator or the barrier receiver, use INFRARED mode.

The protocol runs on the Bus Pirate's binmode serial port. The baud rate setting is ignored.

## Connect

When software opens the binmode port, the Bus Pirate sends an ID string:

```
\n!BP V310!\n
0a 21 42 50 20 56 33 31 30 21 0a
```

**BP** identifies the Bus Pirate, and AnalysIR only reads the characters between the first ```!``` and the space. The digits after the **V** are version numbers.

## Receive

Each signal reaches the host as a list of 5 byte records: one for every mark and every space, in order, then a modulation record with the carrier period if the learner measured one. The Bus Pirate sends the signal once the remote has been quiet for 65,535µs.

### Pulse record

|Byte|Content|
|-|-|
|0|```+``` (0x2B) for a mark, ```-``` (0x2D) for a space|
|1|Record counter. Starts at 0 for every signal and wraps after 255|
|2|Duration in µs, low byte|
|3|Duration in µs, high byte|
|4|```\n``` (0x0A)|

Marks and spaces alternate, starting with a mark. A signal ends with a space of 65,535µs (0xFFFF): no IR for 65.5ms, the signal is over.

### Modulation record

|Byte|Content|
|-|-|
|0|```M``` (0x4D)|
|1|Number of periods measured|
|2|Carrier period in ns, low byte|
|3|Carrier period in ns, high byte|
|4|```\n``` (0x0A)|

Carrier frequency in Hz = 1,000,000,000 / period. For example, 28,000ns is 35,714Hz.

### Example

The 9 key of an RC6 remote, 40 pulse records and the modulation record:

```
2b 00 62 0a 0a    +  #0     2658µs  mark
2d 01 86 03 0a    -  #1      902µs  space
2b 02 bb 01 0a    +  #2      443µs  mark
2d 03 66 03 0a    -  #3      870µs  space
...
2b 26 7c 03 0a    +  #38     892µs  mark
2d 27 ff ff 0a    -  #39   65535µs  space, end of the signal
4d 01 60 6d 0a    M        28000ns  carrier period, 35,714Hz
```

{{% alert context="warning" %}}
Don't split the stream on newlines. The duration bytes can be 0x0A too: the first record above is 2658µs, 0x0A62, so its high byte is a newline. Read the ID string first, then 5 bytes at a time.
{{% /alert %}}

## Transmit

To transmit, send the signal as aIR text. The Bus Pirate sends it out through the IR LEDs on IO4.

```
$38:900,1800,900,65535,;
```

|Part|Meaning|
|-|-|
|```$```|Start of the signal|
|```38```|Carrier frequency in whole kHz|
|```:```|The timings start here|
|```900,1800,900,65535,```|Mark, space, mark, space... in µs, from 1 to 65535, starting with a mark. Every value ends with a comma, the last one too|
|```;```|End of the signal. The Bus Pirate transmits it now|

- The final space can be left out.
- No spaces or line breaks between the ```$``` and the ```;```.
- The receiver is paused while the Bus Pirate transmits, so it doesn't capture its own signal.
- There is no reply.

INFRARED mode uses the same aIR text: the RAW protocol prints received signals in this format and the [```irtx```]({{< relref "/docs/command-reference#irtx" >}}) command transmits it. AnalysIR can import it too, see [capture in the terminal]({{< relref "/docs/software/analysir#capture-in-the-terminal" >}}).
