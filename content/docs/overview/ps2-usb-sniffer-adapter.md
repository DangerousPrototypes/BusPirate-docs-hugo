+++
weight = 20905
title = 'PS/2 & USB Keyboard Sniffer Adapter'
+++

![](/images/docs/fw/plank-ps2usb.jpg)

The PS/2 & USB Sniffer adapter plank sits inline between a keyboard and a computer and passively records everything that crosses the wire. [PS/2 and low speed USB are decoded live]({{<relref "/docs/devices/ps2-usb-keyboard/">}}): raw packets scroll past as they happen, and a **key tracker** rebuilds the typed text right next to them, so you read words instead of scan codes.

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

## Connectors

The keyboard plugs into a **DEVICE** connector, and the cable to the PC into the **HOST** connector of the same kind: **PS/2 DEVICE** and **PS/2 HOST** for a PS/2 keyboard, the USB-A **DEVICE** socket and the USB-C **HOST** socket for a USB keyboard. Each pair is wired straight through, data and power, and the Bus Pirate listens on the data lines.

## Trigger

The **TRIGGER** header has two pins, **TRG** and **GND**. TRG is the Bus Pirate **TRIG** pin (IO0), pulled up to the Bus Pirate **VOUT** pin by a 2K resistor. When the USB sniffer's capture trigger is enabled, a capture starts as soon as TRG goes low: connect it to GND with a button or a jumper wire, or pull it low with a signal from your circuit.

## Power switch

![](/images/docs/fw/ps2usb-pwr-switch.jpg)

**SW1** selects where the sniffed bus takes its power from. Slide it to **VOUT** to power the bus from the Bus Pirate supply, or to **EXT** to let the PC power it, exactly as it would without the plank in the way. A backflow prevention circuit between the Bus Pirate **VOUT** pin and the switch keeps the PC supply out of the Bus Pirate.

The **PWR** LED lights when the bus has power. On the **VIN** header, **+** is the bus supply that the four connectors share and **-** is ground.

{{% alert context="danger" %}}
The [PS/2 and USB sniffer setups]({{<relref "/docs/devices/ps2-usb-keyboard/">}}) need the **PWR SWITCH** in the **EXT** position, as in the photo. The keyboard is powered by the PC through the pass-through cables, not by the Bus Pirate.
{{% /alert %}}

## Schematic

![](/images/docs/fw/ps2usb-schematic.png)

PS/2 & USB Keyboard Sniffer adapter [schematic and PCB](https://github.com/DangerousPrototypes/BusPirate5-hardware/tree/main/development/adapter-kaybee-plank-1REV1) are available in the Bus Pirate 5 hardware repository.

## BOM

| Item | Quantity | Reference(s) | Value | Footprint |
|------|----------|--------------|-------|-----------|
| 1 | 3 | C1, C2, C3 | 47uF/CL21A226MAYNNNE | Capacitor_SMD:C_0805_2012Metric |
| 2 | 1 | D2 | LED | LED_SMD:LED_0805_2012Metric |
| 3 | 1 | D401 | 1N4148WT | Diode_SMD:D_SOD-523 |
| 4 | 2 | J1, J4 | Mini-DIN-6 | connector-mini-din-6:Connector_Mini-DIN_Female_6Pin_2rows |
| 5 | 1 | J2 | Conn_01x10 | Connector_PinSocket_2.54mm:PinSocket_1x10_P2.54mm_Horizontal |
| 6 | 1 | J5 | USB_A | Connector_USB:USB_A_CONNFLY_DS1095-WNR0 |
| 7 | 1 | J7 | TYPE-C-31-M-12 | TYPE-C-31-M-12:HRO_TYPE-C-31-M-12 |
| 8 | 2 | J8, J9 | Conn_01x02_Pin | Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical |
| 9 | 4 | L1, L2, L4, L5 | CBW201209U300T | Inductor_SMD:L_0805_2012Metric |
| 10 | 1 | Q401 | BCM857BS-7-F | Package_TO_SOT_SMD:SOT-363_SC-70-6 |
| 11 | 1 | Q402 | BC2301T 2.8A | Package_TO_SOT_SMD:SOT-523 |
| 12 | 2 | R1, R5 | 5.1K | Resistor_SMD:R_0805_2012Metric |
| 13 | 2 | R2, R3 | 2K | Resistor_SMD:R_0805_2012Metric |
| 14 | 1 | R408 | 68K | Resistor_SMD:R_0805_2012Metric |
| 15 | 1 | R410 | 10K | Resistor_SMD:R_0805_2012Metric |
| 16 | 1 | R412 | 100K | Resistor_SMD:R_0805_2012Metric |
| 17 | 1 | SW1 | SW_SPDT | Button_Switch_SMD:SW_SPDT_PCM12 |

## Resources
- [PS/2 & USB Keyboard Sniffer demo]({{<relref "/docs/devices/ps2-usb-keyboard/">}})
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
