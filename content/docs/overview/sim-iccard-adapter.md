+++
weight = 20700
title = 'IC Card and SIM Adapter'
+++

![](../devices/img/sle4442-adapter.jpg)

The IC card and SIM adapter for Bus Pirate 5 has sockets for mini, micro and nano SIM cards. Everything is connected and ready to go - get started right away.

![](../devices/img/ic-card-pinout.png)

Common IC cards usually follow the [ISO 7816-3 standard](https://en.wikipedia.org/wiki/ISO/IEC_7816) and have the same pinout and contact shape. [Image source](https://commons.wikimedia.org/wiki/File:SmartCardPinout.svg).



{{% readfile "/_common/_footer/_footer-cart.md" %}}

![](/images/docs/fw/sim-iccard-all.jpg)
## mini, micro, and nano SIM cards

The top of the adapter has sockets for mini, micro, and nano SIM cards. Most [mobile phone SIM cards]({{< relref "/docs/devices/sim-bank-ic-cards" >}}) use a half-duplex serial UART interface, such as the Bus Pirate [HDPLXUART mode]({{< relref "/docs/command-reference/#hduart" >}}). 

| Socket | Description |
|--------|-------------|
| U1 | 6 pin mini SIM card socket |
| U2 | 8 pin micro SIM card socket |
| U3 | 6 pin nano SIM card socket |

We looked at a lot of sockets and decided these were the best bet. Complex sockets with springs, hinges and slides are prone to break. These simple sockets should hold up better with repeated use.


## Smart IC cards

A KF-011C socket on the reverse accepts most ISO 7816-3 smart cards:
- [SLE4442 IC cards]({{< relref "/docs/devices/sle4442" >}}) with passcode protection, supported by [2-Wire protocol mode]({{< relref "/docs/command-reference/#2-wire" >}})
- [24C02/24C04/24C08/24C16 EEPROM cards]({{< relref "/docs/devices/24c02" >}}), supported by [I2C protocol mode]({{< relref "/docs/command-reference/#i2c" >}})
- [Bank cards, ID cards, and other smart cards]({{< relref "/docs/devices/sim-bank-ic-cards" >}}), supported by [HDPLXUART mode]({{< relref "/docs/command-reference/#hduart" >}})

A card detect switch is connected to an LED on the top of the board. _CARD LED_ will light when a card is inserted.

## Power and Ground Selection

| Switch | Normal | IO pin | Description |
|--------|-----|-----|-------------|
| VCC   | VOUT | IO4 | Connect VCC pin of the socket to VOUT or IO4|
| GND   | GND | IO5 | Connect GND pin of the socket to GND or IO5|

SW1 and SW2 along the side of the adapter select the power (VCC) and ground (GND) connection to the card socket. For normal use select VCC:VOUT and GND:GND. Found a non-standard pinout? Flip the switches to connect the VCC and GND pins of the socket to Bus Pirate pins IO4 and IO5.

## Pin Connections

|Bus Pirate|IC Card/SIM|Adapter|Description|
|-|-|-|-|
|Vout|C1|VCC|Bus Pirate power supply to socket VCC|
|IO0|C7|I/O| I/O data pin|
|IO1|C3|CLK| Clock pin|
|IO2|C2| RST| Reset pin|
|IO3|C6| VPP| Programming voltage pin|
|IO4|C1|IOVCC|IO4 connection to socket VCC |
|IO5|C5|IOGND|IO5 connection to socket GND|
|IO6|C8|N/A|C8 unused pad. _micro SIM and IC card only_|
|IO7|C4|N/A|C4 unused pad. _micro SIM and IC card only_|
|GND|C5|GND|Bus Pirate ground to socket ground|

## Resources

- IC Card and SIM adapter [schematic and PCB](https://github.com/DangerousPrototypes/BusPirate5-hardware/tree/main/)
- [How to interface SLE4442 IC cards]({{< relref "/docs/devices/sle4442" >}})
- [How to interface 24C02 EEPROM cards]({{< relref "/docs/devices/24c02" >}})
- [How to interface SIM and bank cards]({{< relref "/docs/devices/sim-bank-ic-cards" >}})
- [Half-duplex UART mode documentation]({{< relref "/docs/command-reference/#hduart" >}})
- [2-Wire mode documentation]({{< relref "/docs/command-reference/#2-wire" >}})
- [I2C mode documentation]({{< relref "/docs/command-reference/#i2c" >}})
- [sle4442 command documentation]({{< relref "/docs/command-reference/#sle4442" >}})

## Get a Bus Pirate


{{% readfile "/_common/_footer/_footer-get.md" %}}

### Community


{{% readfile "/_common/_footer/_footer-community.md" %}}

### Documentation
 

{{% readfile "/_common/_footer/_footer-docs.md" %}}



