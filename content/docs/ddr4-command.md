+++
weight = 10010
title = 'ddr4 command'
+++

### ```ddr4``` Probe, read, write, unlock DDR4 SDRAM modules

{{< asciicast src="/screencast/ddr4-command-cast.json" poster="npt:0:22"  idleTimeLimit=2 >}} 
<br/>
The ```ddr4``` command can probe, read, write, and unlock the SPD hub chip in [DDR4 SDRAM computer memory modules]({{< relref "/docs/devices/ddr4">}}) (UDIMM, SODIMM). 
- Unlock SPD chips, backup SPD data and restore corrupted SPD tables. 
- Search for, and replicate, hidden entries unscrupulous manufacturers use to lock equipment to proprietary RAM modules.

DDR4 SPD dumps can be edited with a HEX editor or a dedicated SPD editor GUI like [DDR4XMPEditor](https://github.com/integralfx/DDR4XMPEditor).

{{% alert context="info" %}}
The [DDR4 SPD I2C adapter plank]({{< relref "/docs/overview/ddr-ram-i2c-adapter/" >}}) has everything you need to play with DDR4 without soldering. The plank provides the correct voltage levels and pinouts to interface with a DDR4 SPD chip in offline mode.
{{% /alert %}}

#### DDR4 probe

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:rgb(150,203,89)">I2C></span>&nbsp;ddr4&nbsp;probe
...

DDR4&nbsp;SPD&nbsp;General&nbsp;Section&nbsp;Information:
=====================================
SPD&nbsp;Bytes&nbsp;Used:&nbsp;384
SPD&nbsp;Bytes&nbsp;Total:&nbsp;512
SPD&nbsp;Revision:&nbsp;1.1
DRAM&nbsp;Device&nbsp;Type:&nbsp;DDR4&nbsp;SDRAM
Module&nbsp;Type:&nbsp;UDIMM&nbsp;(0x2)
...

DDR4&nbsp;SPD&nbsp;Manufacturing&nbsp;Information:
==================================
Module&nbsp;Manufacturer&nbsp;ID:&nbsp;0xCE80&nbsp;(Samsung)
Manufacturing&nbsp;Location:&nbsp;0x03
Manufacturing&nbsp;Date:&nbsp;Year&nbsp;17,&nbsp;Week&nbsp;41&nbsp;(2017-W41)
Module&nbsp;Serial&nbsp;Number:&nbsp;0xD647B920&nbsp;(3595024672)
Module&nbsp;Part&nbsp;Number:&nbsp;"M378A5244CB0-CRC"
Module&nbsp;Revision:&nbsp;0.0
DRAM&nbsp;Manufacturer&nbsp;ID:&nbsp;0xCE80&nbsp;(Samsung)
{{< /term >}}

```ddr4 probe``` identifies the DDR4 SPD chip and displays its type, revision, vendor ID, and write protection status. It also reads the JEDEC manufacturing information blocks to display stored information about the memory configure and manufacturer. 

The probe command also searches the Manufacture Specific Data block and End User Programmable blocks for hidden information. This will discover EXPO (AMD) and XMP (Intel) overclock profiles, as well as hidden information that unscrupulous manufacturers use to lock equipment to proprietary RAM modules.

#### DDR4 dump
{{< termfile source="static/snippets/ddr4-command-dump-partial.html" >}}

The ```ddr4 dump``` command displays the contents of a DDR4 SPD chip EEPROM/non-volatile memory in the terminal. It reads the chip and prints the contents of each 64-byte block.
- ```ddr4 dump``` - display the contents of the DDR4 SPD chip in the terminal
- ```ddr4 dump -s <start>``` - display the contents of the DDR4 SPD chip, starting at address `<start>`
- ```ddr4 dump -s <start> -b <bytes>``` - display a specific range of bytes, starting at address `<start>` and reading `<bytes>` bytes

#### DDR4 read to file

{{< termfile source="static/snippets/ddr4-command-read.html" >}}

Read the contents of a DDR4 SPD chip and save to a file with the ```ddr4 read``` command. The file name is specified with the ```-f``` flag.
- ```ddr4 read -f <file>``` - read the contents of the DDR4 SPD chip to file `<file>`

#### DDR4 verify against file

{{< termfile source="static/snippets/ddr4-command-verify.html" >}}

Verify the contents of a DDR4 SPD chip against a file with the ```ddr4 verify``` command. The file name is specified with the ```-f``` flag. This command reads the chip and compares it to the file, reporting the location of any differences.

- ```ddr4 verify -f <file>``` - verify the contents of the DDR4 SPD chip against the file `<file>`

#### DDR4 lock/unlock block

{{< termfile source="static/snippets/ddr4-command-lock.html" >}}

Lock or unlock a block in the DDR4 SPD chip with the ```ddr4 lock``` and ```ddr4 unlock``` commands. The block number is specified with the ```-b``` flag (0-15). Each block is 64 bytes in size.
- ```ddr4 lock -b <block>``` - lock the specified block in the DDR4 SPD chip
- ```ddr4 unlock -b <block>``` - unlock the specified block in the DDR4 SPD chip

{{% alert context="info" %}}
In order to unlock blocks the module's HSA pin **must** be connected to ground. This is required to unlock the block protection bits in the DDR4 SPD chip. See the [DDR4 SPD demo]({{% relref "/docs/devices/ddr4/#connections" %}}) for more details.
{{% /alert %}}

#### DDR4 write from file

{{< termfile source="static/snippets/ddr4-command-write.html" >}}

Write a file to a DDR4 SPD chip with the ```ddr4 write``` command. The file name is specified with the ```-f``` flag. 
- ```ddr4 write -f <file>``` - write the contents of `<file>` to the DDR4 SPD chip

{{% alert context="info" %}}
During write the command will unlock the block protection bits. When the write is complete, the write protection bits will be restored to the original state.  
{{% /alert %}}

{{% alert context="danger" %}}
The ```ddr4 write``` command will overwrite the contents of the DDR4 SPD EEPROM. Use with caution, as it can corrupt the SPD data and render the RAM module unusable. Always make a backup with the ```ddr4 read``` command before writing to the chip.
{{% /alert %}}


#### DDR4 crc check
{{< termfile source="static/snippets/ddr4-command-crc.html" >}}

Calculate or verify the CRC of the JEDEC blocks 0-7 in a DDR4 SPD dump file with the ```ddr4 crc``` command. The file name is specified with the ```-f``` flag. This command reads the specified file and calculates the CRC for the first 8 blocks, reporting any discrepancies.
- ```ddr4 crc -f <file>``` - calculate CRC for the first 8 blocks of the DDR4 SPD chip dump file `<file>`

{{% alert context="info" %}}
To verify the CRC on a DDR4 SPD chip instead of a file, use the ```ddr4 probe``` command. It will automatically calculate and verify the CRC for the first 8 blocks of the SPD chip.
{{% /alert %}}

#### DDR4 crc patch

{{< termfile source="static/snippets/ddr4-command-patch.html" >}}

To update the CRC of a DDR4 SPD dump file, say after making modifications in a HEX editor, use the ```ddr4 patch``` command. This command reads the specified file, calculates the correct CRC for the first 8 blocks, and updates the stored CRC in the file. The file name is specified with the ```-f``` flag.
- ```ddr4 patch -f <file>``` - update the CRC for the first 8 blocks of the DDR4 SPD chip dump file `<file>`

{{% alert context="info" %}}
The ```ddr4 patch``` command does not modify the contents of the DDR4 SPD chip, it only updates the CRC in the specified file.
{{% /alert %}}

#### DDR4 Options and flags
{{< termfile source="static/snippets/ddr4-command-help.html" >}}

{{% alert context="info" %}}
Use ```ddr4 -h``` to see the latest options and features.
{{% /alert %}}

|Option|Description|
|------|-----------|
|```ddr4 probe```|Probe DDR4 SPD chip for ID and NVM/EEPROM status.|
|```ddr4 dump```|Display DDR4 SPD NVM contents in the terminal.|
|```ddr4 read```|Read DDR4 SPD NVM to a file. Specify file with -f flag.|
|```ddr4 write```|Write file to DDR4 SPD NVM. Specify file with -f flag.|
|```ddr4 verify```|Verify DDR4 SPD NVM against file. Specify file with -f flag.|
|```ddr4 lock```|Lock DDR4 SPD NVM block (128 bytes per block). Specify block with -b flag.|
|```ddr4 unlock```|Unlock all DDR4 EEPROM protection blocks.|
|```ddr4 crc```|Calculate/verify CRC of JEDEC blocks 0-7 in a file. Specify file with -f flag.|
|```ddr4 patch```|Update the CRC of JEDEC blocks 0-7 in a file. Specify file with -f flag.|

Options tell the flash command what to do.

|Flag|Description|
|-----|-----------|
|```-f```|File flag. Specify a file to write, read, verify, check or patch CRC|
|```-b```|Block flag. Specify a DDR4 protection block to lock (0 - 3)|
|```-s```|Start address flag. Specify the dump start address|
|```-b```|Bytes flag. Specify the number of bytes to dump|
|```-q```|Dump quiet mode, no address or ASCII columns. Useful for copying HEX values to a HEX editor.|
|```-h```|Show help for Bus Pirate commands and modes|

Flags pass file names and other settings.