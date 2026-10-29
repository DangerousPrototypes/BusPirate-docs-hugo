+++
weight = 60300
title = 'AnalysIR Infrared RX/TX'
+++

![](/images/docs/fw/analysir-annotation.png)

[AnalysIR](https://www.analysir.com/blog/get-analysir/) is a Windows program that captures, decodes and analyzes infrared (IR) remote control signals. With the [IR Toy plank]({{< relref "/docs/overview/infrared-toy-v3" >}}), the Bus Pirate works as an AnalysIR capture device. Point a remote at the plank, press a button, and AnalysIR draws the signal, shows its carrier frequency and tells you the protocol and the code. It can also send captured signals back out through the plank's IR LEDs, so you can check that a capture really controls the device it came from.

{{% alert context="warning" %}}
AnalysIR is paid software. We strive to provide free and open source alternatives whenever possible, but AnalysIR has been updated continuously for many years and an Educational & MakerSpaces license is available for $20. Demo mode can't connect to capture hardware, so you need a license to use it with the Bus Pirate. Sending signals is one of the **Power Tools**, and not every license includes all of them, so check before you buy.
{{% /alert %}}

- [Get AnalysIR](https://www.analysir.com/blog/get-analysir/)
- [IR Toy v3 plank]({{< relref "/docs/overview/infrared-toy-v3" >}})
- [aIR binmode protocol]({{< relref "/docs/binmode-reference/protocol-air" >}})

## What you need

- A Bus Pirate 5, 5XL or 6
- The [IR Toy v3 plank]({{< relref "/docs/overview/infrared-toy-v3" >}})
- A Windows PC with AnalysIR and a license. We used version 1.19.200.9446.
- Something that sends infrared signals

The examples in this guide use two TV remotes, because there's one in almost every home: a cheap universal remote that sends RC6, the Philips protocol, and a Samsung TV remote. The steps are the same for other things that talk infrared, like set-top boxes, fans and toys. AnalysIR decodes more than 100 protocols, and for the ones it doesn't know it still shows you every mark and space.

Most of these devices use a 36 to 40kHz carrier, like the remotes here, and that's what AIR mode listens for. For a 56kHz device, see [capture in the terminal](#capture-in-the-terminal).

## Infrared remote basics

An infrared remote talks to the device it controls by blinking an infrared LED. Three ideas are enough to read everything AnalysIR shows you.

- **Carrier**: the LED doesn't just turn on. It flashes very fast, usually 36,000 to 40,000 times a second (36-40kHz), so the receiver can tell the remote apart from sunlight and lamps.
- **Mark and space**: a burst of carrier is a **mark**, a pause is a **space**. The message is in their lengths, measured in microseconds (µs, millionths of a second).
- **Protocol**: the rules that turn marks and spaces into bits. Manufacturers use different ones: NEC, RC5, RC6 (Philips), Samsung, Sony and many more. AnalysIR recognizes over 100 of them.

## How it works

AnalysIR needs capture hardware, like its own A.IR Shield Nano. In the AIR binary mode the Bus Pirate speaks the same serial protocol on its second USB serial port, so AnalysIR sees it as an A.IR Shield Nano.

The IR Toy plank has four receivers and two IR LEDs. AIR mode uses three parts of it:

- The **36-40kHz demodulator** removes the carrier and outputs just the marks and spaces. The Bus Pirate times them with 1µs resolution.
- The **20-60kHz learner** passes the raw carrier through, so the Bus Pirate can measure its frequency.
- The **IR LEDs** send signals back out.

When the remote has been quiet for 65.5 milliseconds, the signal is complete and the Bus Pirate sends it to AnalysIR.

## Connections

![](/images/docs/fw/plank-irtoy.jpg)

Plug the IR Toy plank into the Bus Pirate. AIR mode uses these pins:

|Bus Pirate|Label|IR Toy plank|Description|
|-|-|-|-|
|VOUT| |Power|5 volt supply for the receivers and LEDs, turned on automatically|
|IO1|LERN|20-60kHz learner|Carrier frequency|
|IO4|IRTX|IR LEDs|Transmit|
|IO5|38k|36-40kHz demodulator|Marks and spaces|
|GND| |Ground|Ground|

## Bus Pirate setup

{{< asciicast src="/screencast/analysir-binmode-cast.json" poster="npt:0:07"  idleTimeLimit=2 >}}

In the Bus Pirate terminal use the ```binmode``` command and choose **7. AIR capture (AnalysIR, etc)**.

- The Bus Pirate switches to HiZ mode and turns on the 5 volt power supply for the plank. The status bar shows **Vout: 5.0V** and the pin labels **LERN**, **IRTX** and **38k**.
- The terminal is locked. You can leave the terminal window open, but it won't take commands.
- To leave AIR mode, unplug the Bus Pirate and plug it back in.

### Find the binmode port

The Bus Pirate shows up as two USB serial ports, one for the terminal and one for binmode. AnalysIR needs the binmode port, **not** the terminal port.

On Windows, open **Device Manager** and expand **Ports (COM & LPT)**. Both ports are called **USB Serial Device**, and the binmode port is usually the higher number. In this guide COM18 is the terminal and COM19 is binmode. To be sure, open the port's **Properties**, go to the **Details** tab and choose **Hardware Ids**: the terminal port ends in **MI_00**, the binmode port in **MI_02**.

## AnalysIR setup

### The main window

![](/images/docs/fw/analysir-main-window-areas.png)

|Area|What it shows|
|-|-|
|1. Traces|The signal drawn as a square wave, Channel 1 on top and Channel 2 below. The gray bar under each trace is a timeline, with a small tick every 1,000µs and a big tick every 10,000µs. Hover over a trace to see the time offset.|
|2. Channel 1, Channel 2, Rules|Every mark and space of the signal as a table. **Rules** shows the timings AnalysIR uses to recognize each protocol.|
|3. Channel settings|Zoom, measurement and decoding options for each channel.|
|4. Session History|One row for every signal received, with its protocol and code.|
|5. About, Log, Details|**Log** shows the raw data received from the capture device, handy when something doesn't work. **Details** breaks some protocols down field by field.|
|6. Status bar|The capture source, the active channel, the serial port and the carrier frequency of the selected signal.|

AnalysIR has two channels, one above the other, so you can compare two signals. New captures go to the active channel, shown in the status bar.

### Connect to the Bus Pirate

1. In the status bar, pick the Bus Pirate binmode port from the COM drop-down.
2. Open the **Source** menu and choose **A.IR Shield Nano** (Ctrl+Alt+2).

![](/images/docs/fw/analysir-source-air-shield-nano.png)

Don't choose **USB IR Toy**: that's a different device. The IR Toy plank works through the Bus Pirate as an A.IR Shield Nano.

Select the port first, then the source. Whenever AnalysIR detects a fault or a reset of the capture device, it sets the source back to **Arduino**, so check the source again if captures stop, for example after you unplug the Bus Pirate.

![](/images/docs/fw/analysir-status-bar-connected.png)

Check the status bar:

- The source is **A.IR Shield Nano**.
- The square next to the COM port is green: AnalysIR has the port open. Red means it can't open it.
- **115,200 bps** is just AnalysIR's default. The Bus Pirate's USB serial port ignores the baud rate.
- The dot at the far right flashes red every time data arrives from the Bus Pirate.

## Capture a signal

Point the remote at the plank and press a button. We pressed **3** on the universal remote.

![](/images/docs/fw/analysir-capture-rc6.png)

- The **trace** shows the signal in green. High is a mark (IR on), low is a space.
- The **colored bar** under the trace marks the decoded parts of the signal. It only appears when AnalysIR recognizes the protocol.
- The **Channel 1** table lists every mark and space. **Seq** numbers them, **Time µS** is when each one starts, counted from the beginning of the signal, **Duration** is its length and **State** is 1 for a mark, 0 for a space.
- **Session History** gets a new row: type **RC6**, value **00003**, 20 bits.
- The status bar shows **Carrier Frequency: 35,710 Hz**. RC6 uses a 36kHz carrier, so a small difference is normal.

RC6 is the Philips protocol. The last four digits of the value are two bytes: an address that says which kind of device the code is for (00 is a TV) and a command (03 is the 3 key).

Many remotes repeat the signal while you hold a button, and some send it twice even for a short press. That's the second burst on the right of the trace. The 65,535µs space in row 42 isn't the real gap between them: it's the longest pause the Bus Pirate reports, and it means no IR for 65.5ms or more. AnalysIR keeps signals that arrive close together in one row. With **Discrete** checked, it tries to split them into separate rows.

### Zoom in

![](/images/docs/fw/analysir-scale.png)

**Scale** zooms the trace in and out, from 1 to 100 (default 10). At 47 the first signal fills the window. The mouse wheel works too, with the pointer over the channel settings. Double-click the **Scale** label to reset it.

### Show the decoded bits

![](/images/docs/fw/analysir-annotation.png)

Check **Annotation** to label the trace.

- **H** marks the header. The first one is the leader, a long mark and a space that give the receiver time to adjust, and the second is the start bit.
- **0** and **1** are the mode, address and command bits.
- **T** is the toggle bit, which the RC6 standard calls the trailer bit. More on it below.

After the header come three mode bits (000), the toggle bit, then 16 bits: the address (00000000) and the command (00000011, which is 3).

RC6 uses Manchester coding. Every bit is a mark and a space of the same length, about 444µs each (twice that for the toggle bit), and their order gives the value: a 1 is a mark then a space, a 0 is a space then a mark. When two halves of the same kind meet, they merge into one longer mark or space. That's why the trace mixes short and long marks and spaces. [Decode a signal by hand](#decode-a-signal-by-hand) goes through every bit.

### The toggle bit

![](/images/docs/fw/analysir-toggle-bit.png)

Press a different key. We pressed **7**: the new row has value **00007**, a **T** in the **Toggle** column, and its type is underlined.

The remote flips the toggle bit every time you press a key, and keeps it while you hold one down. That's how a TV can tell two presses of the 1 key, for channel 11, from one long press. Not every protocol has a toggle bit.

The **Data** column holds the raw signal: every mark and space as **Seq;Time;Duration;State**, separated by **\|**. The **Carrier** column stores the carrier frequency in Hz.

### Inspect a mark or a space

![](/images/docs/fw/analysir-cursor-tooltip.png)

Hover the mouse over the trace. The matching row is highlighted in the **Channel 1** table, and a tooltip shows:

- **Offset**: the time from the start of the signal.
- **Seq**: the row number in the table.
- **Space** or **Mark**: the length of the space or mark under the pointer.
- **Measure**: the last measurement, see below.
- **Pulse Pair**: a mark plus the space that follows it. Here it's 909µs, the 493µs space under the pointer plus the mark before it. That's as long as one RC6 bit, close to the 889µs of the standard, although this pair straddles two bits.

### Measure a time span

![](/images/docs/fw/analysir-measure.png)

Check the box next to **Measure**, then drag the mouse across the trace or click two points. AnalysIR draws a box over the span and shows its length: 3,638µs here, the length of four bits of about 909µs.

**Cursor** is the other option: a vertical line that follows the mouse along the timeline and shows its position in µs. Only one of the two can be on at a time.

### Session History columns

|Column|What it shows|
|-|-|
|CH|The channel the signal went to|
|Time|When it arrived|
|Type|The protocol, or RAW if AnalysIR doesn't recognize it. Underlined when the toggle bit is set|
|Button|Your own label for the button, like Vol+. Type it in|
|Value|The decoded code in hex. Click it to see it in binary too|
|Value2|A second value that some protocols use|
|Bits|The number of data bits|
|Date|The capture date|
|Data|The raw marks and spaces|
|Toggle|**T** when the toggle bit is set|
|Carrier|The carrier frequency in Hz|

Use **File**, **Save Session** (Ctrl+S) to keep everything you captured.

## Send a signal

![](/images/docs/fw/analysir-send-selected-ir.png)

1. Point the plank's IR LEDs at the device.
2. Click the signal in **Session History**.
3. Open **Power Tools** and choose **Send Selected IR** (Ctrl+Alt+T).

Here we captured **Vol+** from a Samsung TV remote: type **SAMSUNG**, value **E0E0E01F**, 32 bits, 38,170Hz carrier. Sending it back turned the TV volume up. Read the way AnalysIR shows it, **E0E0** is the address, **E0** is the command and **1F** is the command with every bit flipped (E0 + 1F = FF), a simple check that the code arrived intact.

AnalysIR passes the frequency from the **Carrier** column to the Bus Pirate in whole kHz, so this signal goes out at 38kHz. **Power Tools**, **Send IR** (Alt+I) opens a window that sends up to six signals in a row, with optional delays and its own carrier setting.

The range depends on the LED current, which a jumper on the plank sets. Read the [IR Toy plank transmitter notes]({{< relref "/docs/overview/infrared-toy-v3#transmitters" >}}) before you raise it.

## Capture in the terminal

You don't need AnalysIR running to capture a signal. In INFRARED mode with the RAW protocol, the Bus Pirate prints every signal it receives as a line of **aIR** text, and AnalysIR can import it later. This is handy to:

- capture with any serial terminal and analyze on another computer
- share a signal in a forum post or a bug report
- use the **56kHz demodulator** or the **38kHz barrier** receiver, because AIR mode listens with the 36-40kHz demodulator

If the Bus Pirate is in AIR mode, unplug it and plug it back in first.

{{< asciicast src="/screencast/analysir-raw-capture-cast.json" poster="npt:0:20"  idleTimeLimit=2 >}}

### Setup

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">HiZ></span> m

<span style="color:#bfa530">Mode selection</span>
 1. <span style="color:#bfa530">HiZ</span>
 2. <span style="color:#bfa530">1WIRE</span>
 3. <span style="color:#bfa530">UART</span>
 4. <span style="color:#bfa530">HDUART</span>
 5. <span style="color:#bfa530">I2C</span>
 6. <span style="color:#bfa530">SPI</span>
 7. <span style="color:#bfa530">2WIRE</span>
 8. <span style="color:#bfa530">3WIRE</span>
 9. <span style="color:#bfa530">DIO</span>
 10. <span style="color:#bfa530">LED</span>
 11. <span style="color:#bfa530">INFRARED</span>
 12. <span style="color:#bfa530">JTAG</span>
 13. <span style="color:#bfa530">PS2</span>
 14. <span style="color:#bfa530">USB</span>

<span style="color:#96cb59">x to exit ></span> 11

<span style="color:#bfa530">Mode:</span> INFRARED
<span style="color:#bfa530">Protocol</span>
 1. <span style="color:#bfa530">RAW (aIR format)*</span>
 2. <span style="color:#bfa530">NEC</span>
 3. <span style="color:#bfa530">RC5</span>
<span style="color:#96cb59">x to exit (1) ></span> 1

<span style="color:#bfa530">TX modulation</span>
 <span style="color:#bfa530">20kHz to 60kHz</span>
<span style="color:#96cb59">x to exit (38) ></span>

<span style="color:#bfa530">RX sensor</span>
 1. <span style="color:#bfa530">38kHz barrier</span>
 2. <span style="color:#bfa530">36-40kHz demodulator*</span>
 3. <span style="color:#bfa530">56kHz demodulator</span>
<span style="color:#96cb59">x to exit (2) ></span>


<span style="color:#96cb59">INFRARED-(RAW)></span>
{{< /term >}}

- Use the ```m``` command and choose **INFRARED**, or type ```m infrared``` to skip the list.
- **Protocol**: choose **1. RAW (aIR format)**.
- **TX modulation**: press Enter for 38kHz. Receiving doesn't use it.
- **RX sensor**: press Enter for the **36-40kHz demodulator**, or pick another receiver.

If you've used INFRARED mode before, it first asks **Use previous settings?** and lists them. Answer y if they show RAW and the 36-40kHz demodulator, or n to choose again.

### Capture

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">INFRARED-(RAW)></span> W 5

<span style="color:#53a6e6">5.00</span>V<span style="color:#bfa530"> requested, closest value: </span><span style="color:#53a6e6">5.00</span>V
<span style="color:#53a6e6">300.0</span>mA<span style="color:#bfa530"> requested, closest value: </span><span style="color:#53a6e6">300.0</span>mA
<span style="color:#bfa530">Undervoltage limit: </span><span style="color:#53a6e6">4.50</span>V (10%)

<span style="color:#bfa530">Power supply:  </span>Enabled
<span style="color:#bfa530">Vreg output: </span><span style="color:#53a6e6">4.9</span>V<span style="color:#bfa530">, Vref/Vout pin: </span><span style="color:#53a6e6">4.9</span>V<span style="color:#bfa530">, Current: </span><span style="color:#53a6e6">8.2</span>mA

<span style="color:#96cb59">INFRARED-(RAW)></span> $0:271,65535,;
$36:2658,902,443,871,443,466,443,467,1312,1337,443,467,443,466,443,466,443,466,443,466,444,465,444,466,443,466,443,467,443,467,443,466,892,870,443,466,891,65535,;
$36:2655,902,443,870,443,466,444,466,1312,1338,443,466,443,467,443,466,443,466,444,466,443,466,443,467,443,466,444,466,443,466,443,467,891,871,443,466,892,65535,;
$38:4509,4527,526,1711,526,1711,526,1711,526,593,526,593,526,593,526,593,526,593,526,1711,526,1711,526,1711,526,593,526,592,526,593,526,593,526,593,526,1711,525,1712,526,1711,526,593,526,592,526,593,526,593,526,593,526,593,526,593,526,592,526,1711,526,1711,526,1711,525,1712,525,1712,526,48580,262,987,262,435,262,711,262,65535,;
{{< /term >}}

- ```W 5``` turns on the 5 volt power supply for the plank.
- Press buttons on the remote. Every signal prints as one line that starts with **$**.

If a line like ```$0:271,65535,;``` shows up when you turn on the power supply, it isn't a remote. Just a couple of values, here with a carrier of **0**, give it away, so ignore lines like that.

Then come the 9 key of our RC6 remote, sent twice, and the Samsung **Vol+** key at 38kHz.

### The aIR format

This line is the 9 key from another capture, the one imported below:

```
$36:2634,929,416,898,416,494,416,494,415,964,836,494,416,494,416,494,416,494,416,493,416,494,416,493,416,494,416,494,416,493,416,493,416,494,865,897,441,469,864,65535,;
```

|Part|Meaning|
|-|-|
|```$```|Start of the signal|
|```36```|Carrier frequency in kHz|
|```:```|The timings start here|
|```2634,929,416,898,...```|Mark, space, mark, space... in µs, always starting with a mark|
|```65535```|The final space: no IR for 65.5ms, so the signal is over|
|```;```|End of the signal|

Every capture comes out a few tens of microseconds different, and receivers tend to shorten marks and stretch spaces, so your numbers won't match ours or the standard exactly. The same text works the other way too: the [```irtx```]({{< relref "/docs/command-reference#irtx" >}}) command in INFRARED mode transmits aIR text, typed in or read from a file on the Bus Pirate.

### Import into AnalysIR

1. Copy the line from the terminal, from the **$** to the **;**.
2. In AnalysIR open **File**, **Import IR Signal** (Ctrl+I).

   ![](/images/docs/fw/analysir-import-menu.png)

3. Paste the line into the big box on the left.

   ![](/images/docs/fw/analysir-import-paste.png)

4. Click ```>>>>``` for a preview. AnalysIR detects the **A.IR Shield** format and lists every mark and space on the right. It adds a 1,000µs space at the start, row 1.

   ![](/images/docs/fw/analysir-import-preview.png)

5. Click **Import into Channel 1**.

   ![](/images/docs/fw/analysir-import-channel1.png)

![](/images/docs/fw/analysir-imported-signal.png)

It decodes just like a live capture: RC6, value **00009**, the 9 key. The carrier reads 36,000Hz because aIR text only stores whole kHz.

To import several signals at once, put a line with ```$$$``` between them and click **Bulk Import**. To name the button of a single signal, type it in **Key ID** before you import.

{{% alert context="info" %}}
Importing aIR text needs a recent AnalysIR. If ```>>>>``` doesn't recognize the line, check for a newer version with **Help**, **Check on-line for Update now**. We used version 1.19.200.9446.
{{% /alert %}}

## Decode a signal by hand

AnalysIR decodes signals for you, but working one out by hand is the best way to see what a remote really sends. All you need is the aIR text and the rules of the protocol.

### RC6

![](/images/docs/fw/analysir-rc6-bits.png)

This is the 9 key from the aIR line above, with every mark and space rounded to whole 444µs units. The red blocks are marks, the gaps between them are spaces.

**1. Find the unit.** RC6 measures time in units of 444µs, 16 cycles of its 36kHz carrier. Divide every value by 444 and round it: 2634 is 6 units, 929 is 2, 416 is 1, 898 is 2, 494 is 1, and so on.

**2. Write it out.** Use one letter per unit, **M** for mark and **S** for space. The leader comes out as MMMMMMSS, and the whole signal is 52 units long, counting the last S, which hides in the final 65535 space.

**3. Split it into fields.** After the leader every bit is two units: **MS** is a 1 and **SM** is a 0. The toggle bit is twice as long: **MMSS** is a 1 and **SSMM** is a 0.

|Field|Units|Bits|Meaning|
|-|-|-|-|
|Leader|MMMMMM SS| |Gets the receiver ready|
|Start|MS|1|Always 1|
|Mode|SM SM SM|000|Mode 0, consumer electronics|
|Toggle|SSMM|0|Flips on every key press|
|Address|SM SM SM SM SM SM SM SM|00000000|0x00, a TV|
|Command|SM SM SM SM MS SM SM MS|00001001|0x09, the 9 key|

Address 0x00 and command 0x09: the same 00009 that AnalysIR showed.

Now look at the second space, 898µs. It's two units: the S that ends the start bit and the S that begins the first mode bit. When a bit ends the way the next one begins, the LED just stays on, or stays off, and the two halves come out as one longer mark or space. The 865, 897 and 864 near the end are merged halves too.

The 9 key in the [terminal capture](#capture) is another press of the same key, and its toggle bit is 1, **MMSS**. That replaces 415,964,836,494 with 1312,1337: the toggle mark merges with the M before it and the toggle space with the S after it, three units each. The rest of the line is the same, so it's two values shorter.

### Samsung

Samsung uses a different trick called pulse distance coding. Every bit starts with the same short mark of about 560µs, and the space after it gives the value: a short space of about 560µs is a 0, a long space of about 1,690µs is a 1.

Here is the Vol+ key from the terminal capture. The leader is a 4509µs mark and a 4527µs space, then come 32 bits:

|Spaces after each mark (µs)|Bits|Hex|
|-|-|-|
|1711 1711 1711 593 593 593 593 593|11100000|E0|
|1711 1711 1711 593 592 593 593 593|11100000|E0|
|1711 1712 1711 593 592 593 593 593|11100000|E0|
|593 593 592 1711 1711 1711 1712 1712|00011111|1F|

That's E0E0E01F, the code AnalysIR showed. One last 526µs mark follows the 32 bits, because without it there would be no way to measure the space of the last bit. The short marks after the 48.6ms gap aren't part of the code.

AnalysIR reads the first bit of a code as the most significant one, like we did here. **Power Tools**, **LSB** reverses that. Samsung actually sends each byte low bit first, so tools that read it that way show this key as 07 07 07 F8: address 0707 and command 07.

## Going further

This guide covers the basics. AnalysIR does a lot more, for example:

- **Copy to CH2** puts a signal in Channel 2, so you can line up two captures and spot the differences.
- Signals can be exported to other formats, like Arduino IRremote code, Pronto or LIRC.
- **Pulse Analytics** groups the marks and spaces of a signal by length. The **Checksum Calculator** and the **Reverse Engineering Tool** help you work out air conditioner codes. All three are in the **Power Tools** menu.

The **User Guide** in the **Help** menu covers these and much more.

## Troubleshooting

**Nothing shows up in AnalysIR**
- The square next to the COM port must be green, and the source must be **A.IR Shield Nano**. If you unplugged the Bus Pirate, check the source again.
- Use the binmode port, not the terminal port.
- Check that the Bus Pirate is in AIR mode: the terminal says **Binmode active. Terminal locked**. If it doesn't, select the binmode again.
- Only one program at a time can open the binmode port. Close anything else using it, like PulseView.

**The type is RAW.** AnalysIR doesn't know the protocol, or the capture is noisy. Move the remote closer and try again. You can also move the **Tolerance** slider to make decoding more or less strict, then click **Analyse** to decode the signal again.

**The carrier frequency looks wrong.** The carrier is measured by the learner, a different receiver from the one that captures the marks and spaces. Hold the remote closer to the plank and try again.

**A 56kHz remote doesn't show up.** AIR mode only listens with the 36-40kHz demodulator. [Capture it in the terminal](#capture-in-the-terminal) with the 56kHz demodulator and import it.

**The device ignores a signal you send.** Point the LEDs straight at it and get closer. Check the frequency in the **Carrier** column.

## Resources

- [aIR binmode protocol]({{< relref "/docs/binmode-reference/protocol-air" >}})
- [IR Toy v3 plank]({{< relref "/docs/overview/infrared-toy-v3" >}})
- [INFRARED mode]({{< relref "/docs/command-reference#infrared---raw" >}})
- [AnalysIR](https://www.analysir.com/blog/get-analysir/)
- [Development thread](https://forum.buspirate.com/t/infrared-binary-mode-analysir-irman/890)
