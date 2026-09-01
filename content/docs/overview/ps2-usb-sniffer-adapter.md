+++
weight = 20905
title = 'PS/2 & USB Keyboard Sniffer Adapter'
+++

![](/images/docs/fw/plank-ps2usb.jpg)

The PS/2 & USB Sniffer adapter plank sits inline between a keyboard and a computer and passively records everything that crosses the wire. [PS/2 and low speed USB are decoded live]({{<relref "/docs/devices/ps2-usb-keyboard/">}}): raw packets scroll past as they happen, and a **key tracker** rebuilds the typed text right next to them, so you read words instead of scan codes.

PS/2 & USB Sniffer plank features:
- Two PS/2 (mini-DIN 6P) connectors and two USB connectors, wired as pass-throughs so the keyboard keeps working while you capture
- PS/2 scan code set 2 decoded to keystrokes
- Low speed USB HID boot protocol decoded to keystrokes
- A key tracker in each mode that reconstructs the typed text as a plain string
- **TRIGGER** output to sync an external logic analyzer to the capture
- **PWR SWITCH** to take bus power from the Bus Pirate **VOUT** supply or from the PC (**EXT**)

<!-- -->

{{% readfile "/_common/_footer/_footer-cart.md" %}}

## Adapter pinout

|Bus Pirate pin|Label|Description|
|-|-|-|
|1|VOUT|Bus power, when the PWR SWITCH is in the VOUT position|
|2|TRIG|Trigger output to sync an external logic analyzer|
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
Both of the setups below need the **PWR SWITCH** in the **EXT** position, as in the photo. The keyboard is powered by the PC through the pass-through cables, not by the Bus Pirate.
{{% /alert %}}

## Resources
- [PS/2 & USB Keyboard Sniffer demo]({{<relref "/docs/devices/ps2-usb-keyboard/">}})
- [Development thread](https://forum.buspirate.com/t/usb-sniffer-ps2-sniffer-plank-firmware-for-bp/1055)
- [pico-ps2-sniffer](https://github.com/therealdreg/pico-ps2-sniffer)
- [Schematic and PCB](https://github.com/DangerousPrototypes/BusPirate5-hardware/tree/main/development/adapter-kaybee-plank-1REV1)

## Get a Bus Pirate

{{% readfile "/_common/_footer/_footer-get.md" %}}

### Community 

{{% readfile "/_common/_footer/_footer-community.md" %}}

### Documentation

{{% readfile "/_common/_footer/_footer-docs.md" %}}
