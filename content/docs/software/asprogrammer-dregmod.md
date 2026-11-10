+++
weight = 60500
title = 'AsProgrammer dregmod'
+++

![](/images/docs/fw/asprogrammer-spi-read-done.png)

[AsProgrammer dregmod](https://github.com/therealdreg/asprogrammer-dregmod) is a free and open source Windows program that reads, writes, erases and verifies SPI flash and I2C EEPROM chips. It's a fork of [AsProgrammer](https://github.com/nofeletru/UsbAsp-flash) with support for the Bus Pirate, which it drives through the [BPIO2 binmode]({{< relref "/docs/binmode-reference/protocol-bpio2" >}}).

- [Download AsProgrammer dregmod](https://github.com/therealdreg/asprogrammer-dregmod/releases/latest)
- [AsProgrammer dregmod user guide](https://github.com/therealdreg/asprogrammer-dregmod)

In this demo we'll read an SST25VF080B SPI flash and an AT24C256 I2C EEPROM with a Bus Pirate 6.

## Connections

### SPI flash

![](/images/docs/fw/asprogrammer-spi-flash-wiring.jpg)

|Bus Pirate|SST25VF080B board|Description|
|-|-|-|
|VOUT|+3V3|Power supply (3.3 volts)|
|IO4|MISO|Master In Slave Out|
|IO5|CS|Chip Select|
|IO6|SCK|Clock|
|IO7|MOSI|Master Out Slave In|
|GND|GND|Ground|

On a bare chip, tie WP and HOLD to VCC: AsProgrammer doesn't drive them.

### I2C EEPROM

![](/images/docs/fw/asprogrammer-i2c-eeprom-wiring.jpg)

|Bus Pirate|AT24C256 board|Description|
|-|-|-|
|VOUT|+5v|Power supply|
|IO0|SDA|Data|
|IO1|SCL|Clock|
|GND|GND|Ground|

I2C needs pull-up resistors on SDA and SCL. This board has them, so the Bus Pirate pull-up resistors stay off.

## Bus Pirate setup

Update the Bus Pirate to the [latest firmware]({{< relref "/docs/tutorial-basics/firmware-update" >}}) first.

{{< termfile source="static/snippets/cmdref-binmode.html" >}}

In the Bus Pirate terminal use the ```binmode``` command and choose **BPIO2 flatbuffer interface**. Answer y to **Save setting?** and the Bus Pirate keeps BPIO2 after a restart. To check, type ```i```: the **Active binmode** line shows **BPIO2 flatbuffer interface**. PulseView, Flashrom and AVRDUDE use other binmodes: select theirs again with ```binmode``` when you go back to them.

## AsProgrammer setup

1. Open the **Hardware** menu and choose **BusPirateV5+**.

   ![](/images/docs/fw/asprogrammer-hardware-menu.png)

2. In the **BusPirateV5+** menu, open **COM port** and choose the port marked **BPIO2**. The other port of the pair is the terminal. If the ports have no labels, see [find the binmode port]({{< relref "/docs/software/analysir#find-the-binmode-port" >}}).

   ![](/images/docs/fw/asprogrammer-bpio2-com-port.png)

3. In the same menu, set **Voltage** to the voltage of your chip: 1.8, 2.5, 3.3 or 5.0 volts.

   ![](/images/docs/fw/asprogrammer-voltage-menu.png)

4. Set **Current limit**. The power supply turns off if the chip draws more. 100mA is a good value for a flash or EEPROM chip.

   ![](/images/docs/fw/asprogrammer-current-limit-menu.png)

5. Leave **Power ON** checked, so the Bus Pirate powers the chip from VOUT. Check **Pull UPs ON** only for an I2C chip on a board without pull-up resistors.

   ![](/images/docs/fw/asprogrammer-power-on-menu.png)

6. Set the SPI clock in **SPI**, **Clock**. Start at 125kHz and raise it once two reads give the same CRC32.

   ![](/images/docs/fw/asprogrammer-spi-clock-menu.png)

7. Set the I2C clock in **I2C**, **Clock**. Start at 50kHz.

   ![](/images/docs/fw/asprogrammer-i2c-clock-menu.png)

Two more commands in the same menu:

- **Device info / voltages** shows the Bus Pirate model, its firmware, and the power supply settings and measurements. It doesn't turn the power supply on, so it's a safe first check.

  ![](/images/docs/fw/asprogrammer-device-info.png)

- **Disconnect (HiZ, supply off)** turns off the power supply and the pull-up resistors, puts the pins in HiZ and closes the COM port. Use it before you unplug the chip or open the port with another program. If the log says **the target may still be powered**, unplug the Bus Pirate.

  ![](/images/docs/fw/asprogrammer-disconnect-log.png)

{{% alert context="warning" %}}
AsProgrammer keeps the settings of the last session, voltage included. With **Power ON** checked, it turns on the power supply at the first operation on the chip, for example **Read ID** or **Scan the I2C bus...**, and leaves it on until you choose **Disconnect (HiZ, supply off)** or close AsProgrammer. Wire the chip and check the voltage first: 3.3 volts can destroy a 1.8 volt chip.
{{% /alert %}}

## The toolbar

![](/images/docs/fw/asprogrammer-toolbar-buttons.png)

The toolbar buttons have no labels: hold the pointer over one to see its name.

|#|Button|What it does|
|-|-|-|
|1|**Open file**|Loads a file into the hex editor|
|2|**Save file**|Saves the hex editor to a file|
|3|**Read IC**|Reads the chip into the hex editor|
|4|**Program IC**|Writes the hex editor to the chip|
|5|**Erase IC**|Erases the chip|
|6|**Verify IC**|Compares the chip with the hex editor|
|7|**Read ID**|Reads the ID of an SPI flash and lists the chips that match|
|8|**Unprotect**|Clears the write protection bits of an SPI flash|
|9|**Cancel**|Stops the operation that is running|

Buttons 4, 6 and 8 have a small arrow on their right. Click the arrow, not the button, for more commands:

- **Program IC**: its menu has one command. It asks once, then runs **Unprotect**, **Erase IC**, **Program IC** and **Verify IC** in a row.

  ![](/images/docs/fw/asprogrammer-program-ic-menu.png)

- **Verify IC**: **Blank check** checks that the chip is erased.

  ![](/images/docs/fw/asprogrammer-verify-ic-menu.png)

- **Unprotect**: **Set the protection bits** writes the status register at once, without asking. **Read SREG** shows the status registers in the log, and **Edit SREG** opens an editor for them.

  ![](/images/docs/fw/asprogrammer-unprotect-menu.png)

## Read an SPI flash

1. Choose **SPI** with the radio buttons. Do it before you choose the chip: changing the bus clears the chip size and page size.

   ![](/images/docs/fw/asprogrammer-spi-radio.png)

2. Click **Read ID**. The **Find IC** window lists the chips with that ID. Choose yours and click **Select IC**. If the window doesn't open, the log shows the ID with **(Unknown)**. FFFFFF or 000000 means the chip didn't answer: check the wiring and the voltage. Any other ID is a chip that isn't in the list: see the [user guide](https://github.com/therealdreg/asprogrammer-dregmod) to add it.

   ![](/images/docs/fw/asprogrammer-read-id-find-ic.png)

3. Click **Read IC**.

   ![](/images/docs/fw/asprogrammer-read-ic-button.png)

4. The progress bar at the bottom moves while AsProgrammer reads the chip.

   ![](/images/docs/fw/asprogrammer-spi-reading.png)

5. When the log says **Done**, click **Save file** to keep the dump. Reading only fills the hex editor.

   ![](/images/docs/fw/asprogrammer-spi-read-done.png)

The log also shows a CRC32 of what was read. Read the chip again and compare: the same CRC32 twice means both reads returned the same data. If the two reads differ, use shorter wires, and go back to a lower SPI clock if you raised it.

## Read an I2C EEPROM

1. Choose **I2C** with the radio buttons. **Device address** holds the 7-bit address of the chip: 1010000 (0x50) for a 24 series EEPROM with A0, A1 and A2 tied to ground.

   ![](/images/docs/fw/asprogrammer-i2c-device-address.png)

2. Open **BusPirateV5+**, **I2C**, **Scan the I2C bus...** to check the address.

   ![](/images/docs/fw/asprogrammer-i2c-scan-menu.png)

   The scan lists the addresses that answer: 0x50 is the AT24C256. Select its row and click **Use this address** to copy it to **Device address**.

   ![](/images/docs/fw/asprogrammer-i2c-bus-scan.png)

3. An I2C EEPROM has no ID to read. Open the **IC** menu, the first in the menu bar, and choose **I2C**, **_24Cxxx**, **_24C256**. AsProgrammer fills in the size, the page size and the address type from its chip list.

   ![](/images/docs/fw/asprogrammer-i2c-chip-menu.png)

4. Click **Read IC**. When the log says **Done**, click **Save file**.

   ![](/images/docs/fw/asprogrammer-i2c-read-done.png)

If the log says **IC not responding**, check the pull-up resistors and the wiring: SDA on IO0, SCL on IO1.

## Write a chip

Read the chip and save the file before you write anything: it's your backup.

1. Click **Open file** and choose the file to write. **Program IC** writes what the hex editor holds.

   ![](/images/docs/fw/asprogrammer-write-open-file.png)

2. On an SPI flash click **Erase IC**, because **Program IC** doesn't erase the chip first. If the chip is write protected, click **Unprotect** before you erase: SST chips like the SST25VF080B power up that way. An I2C EEPROM needs no erase.

   ![](/images/docs/fw/asprogrammer-write-erase.png)

3. Click **Program IC**, then **Verify IC**.

   ![](/images/docs/fw/asprogrammer-write-program-verify.png)

The command under the arrow of **Program IC** does steps 2 and 3 in one go, after one question.

An I2C EEPROM ignores writes while its WP pin is high: tie WP to ground.

## Troubleshooting

**AsProgrammer can't reach the Bus Pirate**
- Check that BPIO2 is the binmode, see [Bus Pirate setup](#bus-pirate-setup).
- Choose the BPIO2 port, not the terminal port.
- Only one program at a time can open the binmode port. Close anything else using it.

**The Bus Pirate stops answering.** Unplug it and plug it back in, then close AsProgrammer and open it again. A big chip at a low clock takes a while to read: the 1MB SST25VF080B took 1 minute 23 seconds in this demo.

For more detail in the log, check **Verbose log** in the **BusPirateV5+** menu. Report problems on the [AsProgrammer dregmod issues](https://github.com/therealdreg/asprogrammer-dregmod/issues) page.
