+++
weight = 40997
title = 'PS/2 & USB Keyboard Sniffer'
+++

![](/images/docs/fw/plank-ps2usb.jpg)

The Bus Pirate can passively decode PS/2 and USB keyboard signals. PS/2 and low speed USB are decoded live: raw packets scroll past as they happen, and a **key tracker** rebuilds the typed text right next to them, so you read words instead of scan codes.

To make life easier, we've whipped up a [PS/2 & USB Keyboard Sniffer adapter plank]({{<relref "/docs/overview/ps2-usb-sniffer-adapter/">}}) that sits inline between a keyboard and a computer. It has two PS/2 (mini-DIN 6P) connectors and two USB connectors, wired as pass-throughs so the keyboard keeps working while you capture.

PS/2 & USB Sniffer plank features:
- Two PS/2 (mini-DIN 6P) connectors and two USB connectors, wired as pass-throughs so the keyboard keeps working while you capture
- PS/2 scan code set 2 decoded to keystrokes, and the commands the PC sends to the keyboard
- Bus syntax commands to a PS/2 keyboard, with the Bus Pirate as its host: LEDs, ID, reset, keys
- Low speed USB HID boot protocol decoded to keystrokes
- A key tracker in each mode that reconstructs the typed text as a plain string
- **TRIGGER** input to start a USB capture with a button or an external signal
- **PWR SWITCH** to take bus power from the Bus Pirate **VOUT** supply or from the PC (**EXT**)

<!-- -->

{{% readfile "/_common/_footer/_footer-cart.md" %}}

## Adapter pinout

|Bus Pirate pin|Label|Description|
|-|-|-|
|1|VOUT|Bus power, when the PWR SWITCH is in the VOUT position|
|2|TRIG|Trigger input: with the trigger on, a low level starts a USB capture|
|3|D+|USB D+|
|4|D-|USB D-|
|5|RESV|Reserved|
|6|DAT|PS/2 data|
|7|CLK|PS/2 clock|
|8|RESV|Reserved|
|9|RESV|Reserved|
|10|GND|Common ground with the keyboard and the PC|

The Bus Pirate shows these same labels under the pin numbers in the status bar, so you can confirm the plank is wired the right way round at a glance.

## Power switch

![](/images/docs/fw/ps2usb-pwr-switch.jpg)

**SW1** selects where the sniffed bus takes its power from. Slide it to **VOUT** to power the bus from the Bus Pirate supply, or to **EXT** to let the PC power it, exactly as it would without the plank in the way.

{{% alert context="danger" %}}
The sniffer setups below need the **PWR SWITCH** in the **EXT** position, as in the photo. The keyboard is powered by the PC through the pass-through cables, not by the Bus Pirate.
{{% /alert %}}

## PS/2 Keyboard Sniffer

### See it in action

{{< asciicast src="/screencast/ps2-keyboard-cast.json" poster="npt:0:19" idleTimeLimit=2 >}}

### Connections

![](/images/docs/fw/ps2usb-ps2-setup.jpg)

What you need:

- A PS/2 keyboard
- A PS/2 male to PS/2 male cable (MINI-DIN 6P)
- A PS/2 to USB adapter

Plug the keyboard into **PS/2 DEVICE**, and the cable to the PS/2 to USB adapter into **PS/2 HOST**. Plug all **3 USB male** connectors straight into the PC, exactly as shown in the photo. This arrangement is what makes the capture work reliably, so copy it as closely as you can. Don't forget the **PWR SWITCH** in the **EXT** position.

### Setup

{{< termfile source="static/snippets/ps2-keyboard-setup.html" >}}

- Use the **[m]({{< relref "/docs/command-reference/#m-set-bus-mode" >}})** mode command and select **PS2**, or ```m ps2``` to skip the menu.

### Sniffing a PS/2 keyboard

{{< termfile source="static/snippets/ps2-keyboard-sniff.html" >}}

- ```sniff``` - start the sniffer, press **q** to exit.

```sniff``` turns on the 5 volt power supply and starts listening. Each byte on the bus is one line: the byte number, the time in milliseconds (in hex), **D** for a byte from the keyboard (device) or **H** for a byte from the PC (host), and the byte. When a byte completes a key, a reply or a command, the line under it names it.

Above, the word **Hi** was typed. Shift went down (**MAKE_SHIFT_LEFT**), then the H key (**MAKE_H**), and the tracker line shows a capital **H**. A key that comes back up sends ```0xF0``` and its code again (**BREAK_H**).

Press **q** to stop. The sniffer prints the captured text and the number of bytes from the keyboard and from the PC. **bytes dropped** counts bytes that arrived faster than the Bus Pirate could print them, and it should be 0.

### Commands from the PC

{{< termfile source="static/snippets/ps2-keyboard-bat.html" >}}

PS/2 is a two-way bus: the PC sends commands to the keyboard, and the sniffer decodes them too. A keyboard sends **BAT OK** (```0xAA```) when it powers up and passes its self-test. Above, the PS/2 to USB adapter answered by asking for the keyboard ID (**HOST READ ID**), and the keyboard replied with **ACK** and its ID, ```0xAB 0x83```. Then the adapter set the keyboard LEDs (**HOST SET LEDS**, then the LED byte ```0x00```, all off). Press Caps Lock and you'll see another **HOST SET LEDS** as the PC turns the Caps Lock LED on.

### Talk to a PS/2 keyboard

{{< asciicast src="/screencast/ps2-host-cast.json" poster="npt:0:34" idleTimeLimit=2 >}}

The Bus Pirate can also take the place of the PC. Plug the keyboard into **PS/2 DEVICE**, leave **PS/2 HOST** empty, and keep the plank's USB-C cable in the PC: it powers the keyboard, with the **PWR SWITCH** in **EXT**. [Bus syntax]({{< relref "/docs/command-reference/#ps2" >}}) then sends commands to the keyboard and reads what it sends back.

{{% alert context="warning" %}}
Leave **PS/2 HOST** empty. With a PC on the other connector, the Bus Pirate and the PC both talk to the keyboard.
{{% /alert %}}

{{< termfile source="static/snippets/ps2-host-power.html" >}}

- ```W 5``` - turn on the 5 volt power supply. The Bus Pirate IO pins work at this voltage.

{{< termfile source="static/snippets/ps2-host-leds.html" >}}

- ```[0xED 0x07]``` - turn on the three keyboard LEDs. **0xED** is the SET LEDS command, and the byte after it has Scroll Lock in bit 0, Num Lock in bit 1 and Caps Lock in bit 2.
- ```[0xED 0x00]``` - turn the LEDs off.

Each byte the Bus Pirate sends shows the keyboard's answer in parentheses. **0xFA** (ACK) means the keyboard took the byte.

{{< termfile source="static/snippets/ps2-host-id.html" >}}

- ```[0xEE]``` - echo, the keyboard sends **0xEE** back.
- ```[0xF2 r r]``` - read the keyboard ID. The keyboard answers **0xFA**, then sends its two ID bytes, read with ```r```: **0xAB 0x83** on this keyboard.
- ```[0xF0 0x00 r]``` - ask for the scan code set in use: set 2 (**0x02**).

{{< termfile source="static/snippets/ps2-host-reset.html" >}}

- ```[0xFF r]``` - reset the keyboard. It answers **0xFA** right away and sends **0xAA** (BAT OK) when its self-test is done. ```r``` waits up to one second for a byte.

{{< termfile source="static/snippets/ps2-host-keys.html" >}}

- ```[``` - hold the keyboard. The Bus Pirate keeps CLK low, and the keyboard keeps the keys you press.
- ```> r:8``` - read eight bytes: **A** went down and up (**0x1C**, then **0xF0 0x1C**), then the up arrow, an extended key with **0xE0** in front.
- ```]``` - let the keyboard go.

The keys above were pressed between ```[``` and ```r```. After ```[```, and after each byte it sends or reads, the Bus Pirate holds the keyboard until ```]```, so the keyboard keeps the keys you press until the next ```r```, as many as its buffer holds. ```]``` lets it go, and so does ```sniff```.

|Command|Name|The keyboard answers|
|-|-|-|
|```0xED <leds>```|SET LEDS|**0xFA** after each byte|
|```0xEE```|ECHO|**0xEE**|
|```0xF0 0x00```|SCAN CODE SET|**0xFA** after each byte, then the set in use|
|```0xF2```|READ ID|**0xFA**, then the two ID bytes|
|```0xF3 <rate>```|SET TYPEMATIC|**0xFA** after each byte|
|```0xF4```|ENABLE|**0xFA**|
|```0xF5```|DISABLE|**0xFA**|
|```0xF6```|SET DEFAULT|**0xFA**|
|```0xFE```|RESEND|its last byte again|
|```0xFF```|RESET|**0xFA**, then **0xAA** after the self-test|

The keyboard in this demo pulls CLK and DAT up itself, a job the PC normally does. If the Bus Pirate answers **CLK or DAT low: no keyboard, or no pull-ups**, nothing holds the lines high: check that the keyboard is in **PS/2 DEVICE** and has power. A keyboard without pull-ups of its own needs the Bus Pirate pull-ups, ```P```. They pull up every IO pin, D+ and D- too, so take the plank's USB-C cable out of the PC first, or the PC sees an unknown USB device. The keyboard then takes its power from the Bus Pirate: slide the **PWR SWITCH** to **VOUT**.

## USB Keyboard Sniffer

### See it in action

{{< asciicast src="/screencast/usb-keyboard-cast.json" poster="npt:0:22" idleTimeLimit=2 >}}

### Connections

![](/images/docs/fw/ps2usb-usb-setup.jpg)

What you need:

- A low speed USB keyboard

Plug the keyboard into the USB-A **DEVICE** socket, and a cable from the USB-C **HOST** socket to the PC. Plug both **USB male** connectors straight into the PC, exactly as shown in the photo. This arrangement is what makes the capture work reliably, so copy it as closely as you can. Don't forget the **PWR SWITCH** in the **EXT** position.

{{% alert context="danger" %}}
The keylogger reads only **USB low speed** (1.5Mbit/s) keyboards. **Full speed** (12Mbit/s) devices can only be captured packet by packet, and **high speed** (480Mbit/s) devices can't be sniffed at all, so check what your keyboard is before wiring anything up.
{{% /alert %}}

### Setup

{{< termfile source="static/snippets/usb-keyboard-setup.html" >}}

- Use the **[m]({{< relref "/docs/command-reference/#m-set-bus-mode" >}})** mode command and select **USB**, or ```m usb``` to skip the menu.

### The USB sniffer

{{< termfile source="static/snippets/usb-keyboard-sniff.html" >}}

- ```sniff``` - open the USB sniffer, press **x** to leave it.

```sniff``` turns on the 3.3 volt power supply and shows the sniffer's settings and commands, each one a single key. The **usb bus** line says what is on the bus: here a low speed device, the kind the keylogger reads.

### Keylogger

{{< termfile source="static/snippets/usb-keyboard-keylog.html" >}}

- ```k``` - start the low speed keylogger, press **q** to stop it.

Each line is one 8-byte HID report from the keyboard. **IN 0x2F/1** is the keyboard's address on the bus and its endpoint. Byte 0 holds the modifiers, **0x02** is the left Shift, and bytes 2 to 7 hold the keys that are down. Above, **Hi** was typed: Shift went down, then **0x0B** (h), and the tracker added a capital **H**, then **0x0C** (i). A report with nothing held down is all zeros.

**q** prints the captured text and the keylogger's counters. **repeats held back** counts reports identical to the previous one, which a keyboard sends again at its idle rate and which hold no new key. **words lost** and the error counters should be 0.

### Capture packets

{{< termfile source="static/snippets/usb-keyboard-capture.html" >}}

- ```s``` - capture packets until the limit (```l```, 5000 packets) or **p**.
- ```b``` - show the captured packets.

A capture shows the packets themselves. The PC sends a keep-alive (**LS SOF**) every millisecond and polls the keyboard for a report (**IN**). The keyboard answers with the report (**DATA0** or **DATA1**), and the PC acknowledges it (**ACK**). The number in front of each packet is the time in microseconds since the keep-alive. Frames with nothing but the keep-alive, or a poll the keyboard answered with **NAK**, are folded into one **Folded** line (setting ```f```). Above, the **a** key went down (**00 00 04 00 00 00 00 00**) and came back up.

### Trigger

{{< termfile source="static/snippets/usb-keyboard-trigger.html" >}}

- ```g``` - turn the capture trigger on, and off again.
- ```s``` - the capture waits for the **TRIG** pin to go low, **p** stops the wait.

With the trigger on, a capture starts when **TRIG** goes low, so a button or a signal from your circuit decides when. Above, the **TRG** pin of the plank's [**TRIGGER** header]({{< relref "/docs/overview/ps2-usb-sniffer-adapter/#trigger" >}}) was connected to **GND** for a moment.

### Full speed devices

{{< termfile source="static/snippets/usb-keyboard-fullspeed.html" >}}

The keylogger reads only low speed keyboards. With a full speed keyboard it says so and decodes nothing: **packets: 0**.

{{< termfile source="static/snippets/usb-keyboard-fullspeed-capture.html" >}}

- ```e``` - set the capture speed to Full, and back to Low.

A full speed device can still be captured packet by packet. At full speed the PC sends a start of frame packet with its number (**SOF #576**) where a low speed bus has a keep-alive.

## How the key trackers work

Both sniffers decode raw bus traffic into keystrokes, but reading a scrolling dump of packets is not how you find out what somebody typed. The **key tracker** solves that: it is a running reconstruction of the typed text, rebuilt from the wire and reprinted every time a new key is resolved, so the transcript is always on screen next to the raw traffic that produced it.

Each mode keeps its own tracker buffer. Characters are appended to it as they are decoded, and the whole buffer is reprinted as a plain string, set apart from the packet log so it is easy to pick out.

The two implementations share that idea but arrive at it from opposite directions, because PS/2 and USB describe a keyboard in fundamentally different ways.

### The PS/2 key tracker

A PS/2 keyboard is event-driven. It transmits a **make code** when a key goes down and a **break code** when it comes back up: the byte ```0xF0``` followed by the make code, with ```0xE0``` in front of both for extended keys such as the arrows. The sniffer decodes the bytes one at a time with a scan code set 2 table, and keeps the ```0xE0``` and ```0xF0``` prefixes until the byte that completes the key arrives.

The tracker adds a character when a key goes down. A key held down sends its make code again and again (typematic auto-repeat), but the tracker adds the character only once and marks the repeats **(repeat)** in the log, so each press gives one character no matter how long the key was held.

Shift and Caps Lock are tracked the way the PC tracks them. Either Shift key gives capitals and the shifted symbols, Caps Lock gives capitals until it is pressed again, and Shift with Caps Lock on gives lower case letters. Only keys with a printable character reach the buffer. Enter, Tab, Backspace, modifiers, function keys and navigation keys are shown in the packet log but left out of the transcript, and so are the keyboard's replies, the PC's commands and the extra Shift codes some keyboards send around the arrow keys (**FAKE SHIFT**).

### The USB key tracker

A low speed USB keyboard does not announce events at all. The host polls it on a fixed interval, and the keyboard answers each poll with an 8-byte HID boot protocol report that is a **snapshot of the current state**: byte 0 is a modifier bitmap, byte 1 is reserved, and bytes 2 through 7 hold the usage IDs of up to six keys being held down at that instant. Nothing in the report says "this key was just pressed".

So the tracker derives events by **comparing each report against the previous one** from the same endpoint. A usage ID that appears in the new report but was absent from the last one is a newly pressed key; anything present in both is simply still held, and is ignored. This is the exact mirror image of the PS/2 approach: USB gives you state and you compute the transitions, PS/2 gives you the transitions directly.

A report identical to the previous one is held back: the keyboard sends it again at its idle rate, or again after a lost ACK, and it holds no new key. Endpoint 0 carries the enumeration, so its data is counted and never decoded. A report that can't come from a boot keyboard (the reserved byte not 0, an error code, a modifier in the key array, the same key twice) is shown with **\<IGNORED\>** or **\<ROLLOVER\>** and not decoded.

Characters are resolved from the HID Usage Tables, a different numbering scheme from PS/2 scan codes: usage `0x04` is `a` on USB, `0x1C` is `a` on PS/2. Shift is read from the modifier bitmap (either the left or the right bit), Caps Lock is tracked as a toggle when usage `0x39` is pressed, and the two combine the way a real keyboard does: letters are uppercased when shift and caps disagree, while non-letters take their shifted symbol only when shift is held. Named keys such as Enter, F5 or the arrows are printed in the packet log but, as on the PS/2 side, kept out of the transcript.

### Limits

The tracker buffer is **circular**. Once it fills up it wraps and begins overwriting from the start without clearing, so a long session shows newer text spliced over older text rather than a clean truncation. Treat the tracker as a live window on recent typing, and the raw packet log as the authoritative record.

Both trackers assume a **US English layout**, since they map codes straight to ASCII with no national keymap in between. A keyboard set to another layout produces a transcript in which the letters are broadly right but the punctuation and symbols are not.

The USB tracker also needs a **low speed keyboard that sends HID boot protocol reports**. A full speed device can only be captured packet by packet, a high speed device not at all, and reports that don't look like a boot keyboard report are shown but not decoded into text.

## Resources

- [PS/2 & USB Keyboard Sniffer adapter]({{< relref "/docs/overview/ps2-usb-sniffer-adapter" >}})
- [PS2 mode documentation]({{< relref "/docs/command-reference/#ps2" >}})
- [USB mode documentation]({{< relref "/docs/command-reference/#usb" >}})
- [Development thread](https://forum.buspirate.com/t/usb-sniffer-ps2-sniffer-plank-firmware-for-bp/1055)
- [Schematic and PCB](https://github.com/DangerousPrototypes/BusPirate5-hardware/tree/main/development/adapter-kaybee-plank-1REV1)


## Get a Bus Pirate

{{% readfile "/_common/_footer/_footer-get.md" %}}

### Community 

{{% readfile "/_common/_footer/_footer-community.md" %}}

### Documentation

{{% readfile "/_common/_footer/_footer-docs.md" %}}
