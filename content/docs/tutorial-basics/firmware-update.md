+++
weight = 30200
title = 'Upgrade Firmware'
+++
<p></p>
{{% alert context="danger" %}}
**Don't skip this step!** We're adding features and squashing bugs daily. Things will be much easier with the latest and greatest firmware installed in your Bus Pirate. ***Don't worry, it's so very easy!***
{{% /alert %}}

## Download the latest firmware

<p></p>
{{% btn icon="📁" context="danger" href="https://forum.buspirate.com/t/bus-pirate-5-auto-build-main-branch/20/999999" %}}
Download Firmware
{{% /btn %}}
<p></p>

Pirate-Bot compiles the latest code and uploads it to the forum every time there's a push to the git repository. Don't wait for lazy devs to prepare a release package.

## Extract your firmware

![](/images/docs/fw/firmware-archive.png)

Open the firmware .zip archive and find the right file for your Bus Pirate:
- ```bus_pirate5_rev10.uf2``` - Bus Pirate 5 revision 10 is by far the most common hardware. **Most people should use this one**
- ```bus_pirate6_rev2.uf2``` - The latest limited edition Bus Pirate 6 revision 2 with an RP2350 chip.

{{% alert context="info" %}}
There are a small number (<100) of Bus Pirate 5 revision 8 engineering samples, developer boards and preview boards. **All shipped without a case**. This version uses the ```bus_pirate5_rev8.uf2``` firmware found in the ```/attic/``` folder.

If the Bus Pirate blinks a menacing red, you've used the wrong firmware. Don't worry, [manually activate the bootloader]({{< relref "#manually" >}}) and try the other firmware file.
{{% /alert %}}


## Activate the bootloader

The Raspberry Pi chip in the Bus Pirate has a hardware bootloader that appears as a USB drive. Upgrade with confidence because the bootloader is fixed in hardware, it can't be corrupted or overwritten. There's two ways to put the Bus Pirate in bootloader mode.

### From the terminal

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">HiZ></span> $
Jump to bootloader for firmware upgrades

Bus Pirate 5 REV10
Firmware download:
https://forum.buspirate.com/t/bus-pirate-5-auto-build-main-branch/20/999999
Hardware revision: 10
Firmware file: bus_pirate5_rev10.uf2
A USB disk named "RPI-RP2" will appear
Drag a firmware file to the disk to upgrade
Later Alligator!
{{< /term >}}

In the Bus Pirate terminal type ```$``` and then press ```enter```. 
- The Bus Pirate will display the firmware file name to load, such as ```bus_pirate5_rev10.uf2``` or ```bus_pirate6_rev2.uf2```.
- A USB disk drive named **RPI-RP2** (v5), **RP2350** (v6) or **BP__BOOT** (v6) will connect to your computer.

{{% alert context="info" %}}
If the firmware update is interrupted and you find yourself locked out of the Bus Pirate terminal don't panic. Follow the instructions in the next step to enter bootloader mode without the terminal.
{{% /alert %}}

### Manually

![](/images/docs/fw/boot-loader.jpg)

Something went wrong and you can't access the Bus Pirate? Just not in the mood to fire up a terminal? No problem, we've got you covered!

- Unplug the Bus Pirate USB cable.
- Use the 2mm hex wrench that accompanied your Bus Pirate to press the button on the bottom of the PCB/enclosure. Lost your hex wrench? A paper clip, toothpick or multimeter probe will all work just as well.
- Plug in the USB cable **while still pressing and holding the button**.
- Now you can release the button.

A USB disk drive named **RPI-RP2** (v5), **RP2350** (v6) or **BP__BOOT** (v6) will connect to your computer.

## Drag and drop the firmware

![](/images/docs/fw/bootload-drive.png)

Drag the firmware file into the USB disk drive. The update will take a few seconds.

- The Bus Pirate will reset and connect to your computer when the firmware update completes.

## Done!
{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">HiZ></span> i

Bus Pirate 5 REV10
https://BusPirate.com/
Firmware <span style="color:#53a6e6">main branch</span> @ a36975d (<span style="color:#53a6e6">Apr 15 2025 09:59:50</span>)
<span style="color:#53a6e6">RP2040</span> with <span style="color:#53a6e6">264KB</span> RAM, <span style="color:#53a6e6">128Mbit</span> FLASH
S/N: <span style="color:#53a6e6">3317570B33CC62E4</span>
Storage: <span style="color:#53a6e6">  0.10GB</span> (FAT16 File System)
{{< /term >}}

You can verify the firmware version using the ```i``` command in the Bus Pirate terminal.

Congratulations, you now have the latest and greatest firmware! Happy hacking!