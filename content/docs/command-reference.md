+++
weight = 10010
title = 'Command Reference'
+++

{{< asciicast src="/sizzle/sizzle-cast.json" poster="npt:1:23"  idleTimeLimit=2 >}}

The Bus Pirate is a versatile debugging and development tool for working with various communication protocols like I2C, SPI, UART, and more. It acts as a bridge between a computer and embedded devices, allowing users to talk to chips without writing code. It is especially useful for prototyping, testing, and reverse engineering hardware.

{{% alert context="info" %}}
It's always best to use the [latest firmware]({{< relref "/docs/downloads" >}}). There are continuous improvements and new features. See the [upgrade guide]({{< relref "/docs/tutorial-basics/firmware-update/" >}}) for the simple drag and drop update process.
{{% /alert %}}

## User terminal

<!-- ![](/images/docs/fw/cmd-toolbar.png)-->

{{< termfile source="static/snippets/cmdref-info.html" >}}

Connect to the Bus Pirate command line with your [favorite serial terminal software]({{< relref "/docs/tutorial-basics/quick-setup/" >}}). On Windows we like the latest version of [Tera Term](https://ttssh2.osdn.jp/index.html.en).

{{% alert context="info" %}}
Talk to the Bus Pirate from a serial terminal of your choice. The serial port is emulated over USB, so the serial port speed setting should not matter. It is traditional to use "115200bps, 8/N/1" if you need configure your terminal, but it should not actually matter.
{{% /alert %}}

### VT100 terminal emulation
{{< term "Bus Pirate [/dev/ttyS0]" >}}
VT100 compatible color mode? (Y/n)>
{{< /term >}}

Press ```enter``` to show the command prompt if your terminal is blank. 

If the Bus Pirate has just restarted you will be prompted to choose the terminal emulation mode.
- VT100 mode - Supports color and a live view statusbar at the bottom of the terminal. This should be your first choice unless you specifically need the legacy ASCII mode.
- ASCII mode - Legacy monochrome text only mode.

The terminal mode can be changed from the [configuration menu]({{< relref "/docs/command-reference/#c-configuration-options-menu">}}). Open the configuration menu with the ```c``` command followed by ```enter```. 

{{% alert context="info" %}}
If you choose VT100 mode and see lots of garbage characters in the terminal, check that your terminal emulator has VT100 support and that VT100 support is enabled.
{{% /alert %}}

### Command line
{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">HiZ></span> 
{{< /term >}}

The Bus Pirate has a simple Linux-like command line interface. Enter a command followed by optional parameters and then press ```enter``` to execute.

### HiZ mode
The Bus Pirate always starts in high impedance mode (HiZ), a safe mode with all outputs disabled. HiZ mode intends to protect any connected devices from conditions beyond their specifications. From the HiZ prompt, a bus mode can be selected to use a specific protocol with the ```m``` [mode command]({{< relref "/docs/command-reference/#m-set-bus-mode" >}}).

### Terminal control

| Keyboard Key  |Action          |
|---------------|-----------------|
| ```left arrow```  |  Moves the cursor left one character                                                                |
| ```right arrow``` |  Moves the cursor right one character                                                               |
| ```up arrow```    |  Copies the previous command in the command history buffer to the command line                      |
| ```down arrow```  |  Copies the next command in the command history buffer to the command line                          |
| ```home```        | Moves the cursor to the beginning of the line                                                      |
| ```end```         |  Moves the cursor to the end of the line                                                            |
| ```backspace```   |  Erases the character to the left of the cursor and moves the cursor left one character             |
| ```delete```      |  Erases the character under (or to the right of) the cursor and moves the cursor left one character |

The terminal understands some common control keys. Left and right move the cursor, up and down scroll through the command history. Home and end move the cursor to the beginning or end of the line. Backspace and delete erase characters.

### Default options

{{< termfile  source="static/snippets/cmdref-defaults.html" >}} 

Most prompts have a default value shown in ```( )``` or marked with ```*```, and the option to exit without making changes.
- Press ```enter``` to select the default option. 
- Press ```x``` followed by ```enter``` to exit a menu without changes.

### Saved options

{{< termfile  source="static/snippets/cmdref-saved-options.html" >}} 

Many options will be saved to flash storage. You will be prompted to reloaded previous settings the next time.

## Getting help
 
The latest help for commands and modes is available in the help menu. This will always be more up to date than the documentation you're currently reading. 
- ```?``` or ```help``` - show the help menu with all available commands and options.
- ```help mode``` or ```? mode``` - show the help menu with all available commands and options for the current mode.
- ```<command> -h``` - show command specific help. For example, ```W -h``` shows help for the ```W``` command.

### Global command list

![Bpv52-help](/images/docs/fw/bp-term2.png) 

- ```?``` or ```help``` - show the help menu with all available commands and options.

### Mode help

{{< termfile  source="static/snippets/cmdref-help-mode.html" >}}

- ```help mode``` or ```? mode``` - show the help menu with all available commands and options for the current mode.

### Command help

{{< termfile  source="static/snippets/cmdref-help-psu.html" >}}

- ```<command> -h``` - show command specific help. For example, ```W -h``` shows help for the ```W``` command.

## Basic commands 

|Command | Description |
|---|---|
|```i```| Version information|
|```c```| Configuration options menu|
|```m```| Set bus mode|
|```l```/```L```| Set MSB/LSB first|
|```o```| Data output display format|
|```d```| Display mode|
|```~```| Self-test|
|```reboot```| Reboot the Bus Pirate|
|```$```| Jump to bootloader for updates|
|```cls```| Clear and redraw terminal|
|```ovrclk```| Overclock the CPU|

### ```i``` Version information
{{< termfile  source="static/snippets/cmdref-info.html" >}} 

Display the hardware, firmware, and microcontroller version information. If a mode is selected, additional information about the mode is displayed.
- ```i``` - show the current version information.

### ```c``` Configuration options menu
{{< termfile  source="static/snippets/cmdref-config.html" >}}

Configure language, LED effects, terminal output and other options. On exit settings are saved to bpconfig.bp on the Bus Pirate flash storage.
- ```c``` - show the configuration menu.
- ```x``` - exit the configuration menu and save the current settings to flash storage.

### ```m``` Set bus mode
{{< termfile  source="static/snippets/cmdref-mode-menu.html" >}} 

The Bus Pirate starts in HiZ mode, a safe mode with all outputs disabled. The ```m``` command selects a bus mode. The Bus Pirate supports many different protocols, including I2C, SPI, UART, 1-Wire, and more. Each protocol has its own set of commands and options.
- ```m``` - show the bus mode menu and change modes.

{{< termfile  source="static/snippets/cmdref-mode-short.html" >}} 

An optional mode parameter can be specified to skip the mode menu. For example, ```m i2c``` selects I2C mode. 
- ```m <mode>``` - change bus mode without showing the menu.

### ```l/L``` Set MSB/LSB first
{{< termfile  source="static/snippets/cmdref-l.html" >}} 

The l/L commands determine the [bit order](http://en.wikipedia.org/wiki/Most_significant_bit) for reading and writing bytes. 
- ```l``` - most significant bit (MSB) first. This is the default setting.
- ```L``` - least significant bit (LSB) first. 

{{% alert context="info" %}}
The current bit order configuration is displayed on the extended information screen using the ```i``` command while in a mode other than HiZ.
{{% /alert %}}

### ```o``` Data output display format
{{< termfile  source="static/snippets/cmdref-o.html" >}} 

The Bus Pirate can display values as [hexadecimal](http://en.wikipedia.org/wiki/Hexadecimal), [decimal](http://en.wikipedia.org/wiki/Decimal), [binary](http://en.wikipedia.org/wiki/Binary_numeral_system) and raw
[ASCII](http://en.wikipedia.org/wiki/ASCII) bytes. 

**Auto display** mode mirrors input formatting. Each value is displayed in the HEX/DEC/BIN format entered.

Change the setting in the data display format menu with the ```o``` command. The default display format is Auto.

- ```o``` - show the data display format menu.

{{% alert context="info" %}}
The current display format is shown on the extended information screen using the ```i``` command while in a mode other than HiZ.
{{% /alert %}}

### ```d``` Display mode
{{< termfile  source="static/snippets/.html" >}} 
{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">HiZ></span> d
<span style="color:#bfa530">Display selection
 1. Default
 2. Scope
 x. Exit</span>
<span style="color:#96cb59">Display ></span> 2
<span style="color:#bfa530">Display:</span> Scope
{{< /term >}}

```d``` selects the LCD display mode.
1. Default: Pin labels and voltage
2. Scope: Oscilloscope mode

### ```~``` Self-test 
{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">HiZ></span> ~
<span style="color:#bfa530">SELF TEST STARTING
DISABLE IRQ: OK
ADC SUBSYSTEM: VUSB  5.08V OK
DAC READ/WRITE: OK
FLASH STORAGE: OK
PSU ENABLE: OK
BIO FLOAT TEST (SHOULD BE 0/0.2V)
BIO0 FLOAT: 0/0.04V OK
BIO1 FLOAT: 0/0.04V OK
BIO2 FLOAT: 0/0.04V OK
BIO3 FLOAT: 0/0.04V OK
BIO4 FLOAT: 0/0.04V OK
BIO5 FLOAT: 0/0.04V OK
BIO6 FLOAT: 0/0.04V OK
BIO7 FLOAT: 0/0.04V OK
BIO HIGH TEST (SHOULD BE >3.0V)</span>
{{< /term >}}

Perform a factory self-test. The Bus Pirate is capable of twiddling pins and checking for hardware faults. See the [Bus Pirate self-test guide]({{< relref "/docs/tutorial-basics/self-test/">}}) for a complete list of tests and the problems they detect.

- ```~``` - run the self-test.

{{% alert context="danger" %}}
Disconnect all wires and devices from the Bus Pirate before running the self-test. Any connected devices may be damaged or cause the test to fail. 
{{% /alert %}}

{{% alert context="info" %}}
Self-test is only available in HiZ mode. If you are in a different mode, the Bus Pirate will prompt you to change to HiZ mode before running the test.
{{% /alert %}}

### ```reboot``` Reboot
{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">HiZ></span> reboot

VT100 compatible color mode? (Y/n)>
{{< /term >}}

Reboot the Bus Pirate. 

- ```reboot``` - reboot the Bus Pirate.

{{% alert context="info" %}}
Depending on your serial terminal software you may need to reconnect to the Bus Pirate serial port. The latest versions of many terminal emulators, such as Tera Term, reconnect automatically.
{{% /alert %}}

### ```$``` Jump to bootloader 
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

Activate the Bus Pirate bootloader for firmware updates. The bootloader appears as a USB disk drive connected to your computer. Drag a **.uf2** firmware file into the disk. After an update the Bus Pirate resets. See [firmware downloads]({{< relref "/docs/downloads/">}}) and [upgrade instructions]({{< relref "/docs/tutorial-basics/firmware-update/">}}).

- ```$``` - jump to bootloader mode.

{{% alert context="info" %}}
When jumping to bootloader mode, the Bus Pirate displays the hardware version, download link, and the name of the firmware file to use.
{{% /alert %}}

### ```cls``` Clear and redraw terminal
{{< termfile  source="static/snippets/cmdref-cls.html" >}}

- ```cls``` - clear the screen and redraw the status bar. 

Useful when connecting to an already running Bus Pirate with a new terminal window.

### ```ovrclk``` Overclock the CPU
{{< termfile  source="static/snippets/cmdref-ovrclk.html" >}}

- ```ovrclk [-m <MHz> | -k <kHz>] [-v <core mV>]``` - set the CPU clock speed and core voltage.

{{% alert context="danger" %}}
```ovrclk``` is disabled by default. It must be enabled at compile time. 
{{% /alert %}}

## Utilities

|Command|Description|
|--------|-----------|
|```w```/```W``` | Power supply (off/ON)
|```v```/```V``` | Power supply voltage report (once/CONTINUOUS)
|```p```/```P``` | Pull-up resistors (off/ON)
|```g```/```G``` | Frequency generator (off/ON)
|```f```/```F``` | Measure frequency (once/CONTINUOUS)
|```=```X | Convert X to HEX/DEC/BIN number format
|```\|``` X | Reverse bits in byte X
|```a```/```A```/```@``` | Auxiliary pin control (low/HIGH/input)


### ```w/W``` Power supply (off/ON) 
{{< termfile  source="static/snippets/cmdref-psuon-menu.html" >}} 

A 'Programmable Power Supply Unit' (PPSU) has several handy features:
- 1-5volts adjustable output
- 0-500mA current sense 
- 0-500mA current limit with digital fuse
- One-way valve to protect the PPSU when an external voltage is applied to the VREF/VOUT pin

Uppercase ```W``` enables the onboard power supply unit. You will be prompted for the output voltage and an optional current limit. Default current limit is 300mA, or 0 for no current limit. 

- ```W``` - Enable the power supply unit. Show interactive menu to set voltage and current limit.
- ```W <voltage> <current limit>``` - Enable the power supply unit with voltage and current limit specified. 
- ```W <voltage>``` - Enable the power supply unit with voltage specified. Current limit is set to 300mA.
- ```w``` - Disable the power supply unit.

Check the voltage and current in the live view statusbar if active, or show the power supply voltage report using the ```v``` command.

When the programmed current limit is exceeded the PPSU hardware fuse disables the power supply. The terminal colors invert repeatedly, an alarm bell will sound, an error message is shown and command execution is halted. Use the ```W``` command to restart the PPSU again.

{{% alert context="danger" %}}
300mA is the rated maximum of the PPSU, but we added some headroom in the current limit to account for current spikes.
{{% /alert %}}

{{% alert context="info" %}}
The PPSU is capable of 0.8 to 5volts output. However, the maximum working range is limited to 1-5volts because of the maximum Vgs of the P-channel MOSFET in the one-way valve. Many will be capable of the full range, but some may not. The Bus Pirate IO buffers are only rated to 1.65volts, so in practice this isn't an issue over the specified working range.
{{% /alert %}}



{{< termfile  source="static/snippets/cmdref-psuon-short.html" >}} 

- ```W <voltage> <current limit>``` - Set the voltage and current limit. The voltage is in volts, the current limit is in mA. The current limit is optional, if not specified the default is 300mA, or use 0 for no current limit.

{{< termfile  source="static/snippets/cmdref-psuoff.html" >}} 

Lowercase ```w``` disables the PPSU.
- ```w``` - Disable the power supply.

### ```v/V``` Power supply voltage report 

![](/images/docs/fw/psu-statusbar1a.png) 

The voltage report shows the current state of all the Bus Pirate pins and peripherals. This is a duplicate of the information shown on the live view statusbar.

- ```v``` - Show the power supply voltage report once.
- ```V``` - Show the power supply voltage report, update continuously. Press any key to exit.

### ```p/P``` Pull-up resistors 

{{< termfile  source="static/snippets/cmdref-p.html" >}}

```p``` and ```P``` toggle the pull-up resistors off and on. Pull-up resistors are required for open collector/open drain bus types such as 1-Wire and I2C.

- ```P``` - Enable the pull-up resistors.
- ```p``` - Disable the pull-up resistors.

The onboard pull-up resistors **are powered through the VREF/VOUT pin of the IO header**, either by the onboard power supply or an external voltage applied to the VREF/VOUT pin. 

{{% alert context="info" %}}
A warning is displayed if there's no voltage on the VREF/VOUT pin. Check the status bar or voltage report ```v``` to verify that a voltage is present on VOUT/VREF.
{{% /alert %}}

### ```g/G``` Frequency generator

{{< termfile  source="static/snippets/cmdref-pwmon.html" >}} 

Uppercase ```G``` displays the frequency generation menu. Choose an available pin and enter the period or frequency, including the units (ns, us, ms, Hz, KHz or Mhz). Enter a duty cycle as a percent, don't forget the ```%```. The Bus Pirate will find the closest match and generate a frequency on the pin. 

- ```G``` - show the frequency generation menu.
- ```g``` - disable frequency generator, show menu if multiple frequency generators are active.
- ```g <pin>``` - disable frequency generator on \<pin>.

![](/images/docs/fw/cmd-freq.png)

The frequency generator will be displayed in the live view statusbar and on the LCD with the label ***PWM***.

{{% alert context="danger" %}}
Not all pins will be available due to the PWM structure of the Raspberry Pi chip used in the Bus Pirate, and adjacent pairs must share the same frequency. 
{{% /alert %}}

{{< termfile  source="static/snippets/cmdref-pwmalloff.html" >}} 

- ```g``` - disable frequency generator, show menu if multiple frequency generators are active.

{{< termfile  source="static/snippets/cmdref-pwmoff.html" >}} 

- ```g <pin>``` - disable frequency generator on \<pin>.

### ```f/F``` Measure frequency

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">LED-()></span> F
<span style="color:#bfa530"><span style="color:#bfa530">Frequency measurement</span></span>
<span style="color:#bfa530">Choose available pin:</span>
 1. IO<span style="color:#53a6e6">1</span>
 3. IO<span style="color:#53a6e6">3</span>
 5. IO<span style="color:#53a6e6">5</span>
 7. IO<span style="color:#53a6e6">7</span>
 x. <span style="color:#bfa530">Exit</span>
<span style="color:#96cb59"> ></span> 7
<span style="color:#bfa530">Frequency measurement:</span> Enabled on IO<span style="color:#53a6e6">7</span>
<span style="color:#bfa530">Frequency</span> IO<span style="color:#53a6e6">7</span>: <span style="color:#53a6e6">12.40</span>KHz <span style="color:#53a6e6">80.65</span>us (<span style="color:#53a6e6">12400</span>Hz), <span style="color:#bfa530">Duty cycle:</span> <span style="color:#53a6e6">35.0</span>%

<span style="color:#96cb59">LED-()></span> 
{{< /term >}}

Frequency measurement is available on odd numbered pins (1,3,5,7). A frequency can be sampled once or continuously. 

- ```F``` - show the frequency measurement menu, measure continuously and display in the status bar.
- ```f``` - Disable continuous frequency measurement, show menu if multiple frequency generators are active.
- ```F <pin>``` - measure the frequency and duty cycle on pin \<pin> continuously. Press any key to exit.
- ```f <pin>``` - measure the frequency and duty cycle on pin \<pin> once.

![](/images/docs/fw/cmd-freq.png) 

The frequency will be measured continuously and displayed in the live view statusbar and LCD with the label **FREQ**.

{{% alert context="danger" %}}
Not all pins will be available due to the PWM structure of the Raspberry Pi chip used in the Bus Pirate, and adjacent pairs share the same PWM slice.
{{% /alert %}} 

{{< termfile  source="static/snippets/cmdref-freq-off.html" >}}

- ```f``` - Disable continuous frequency measurement, show menu if multiple frequency generators are active.

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">LED-()></span> f 7
<span style="color:#bfa530"><span style="color:#bfa530">Frequency</span></span> IO<span style="color:#53a6e6">7</span>: <span style="color:#53a6e6">12.40</span>KHz <span style="color:#53a6e6">80.65</span>us (<span style="color:#53a6e6">12400</span>Hz), <span style="color:#bfa530">Duty cycle:</span> <span style="color:#53a6e6">35.0</span>%
<span style="color:#96cb59">LED-()></span>
{{< /term >}}

- ```f <pin>``` - measure the frequency and duty cycle on pin \<pin> once.

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">LED-()></span> F 7
<span style="color:#bfa530"><span style="color:#bfa530">Press any key to exit</span></span>
<span style="color:#bfa530">Frequency</span> IO<span style="color:#53a6e6">7</span>: <span style="color:#53a6e6">12.40</span>KHz <span style="color:#53a6e6">80.65</span>us (<span style="color:#53a6e6">12400</span>Hz), <span style="color:#bfa530">Duty cycle:</span> <span style="color:#53a6e6">35.0</span>%
{{< /term >}}

- ```F <pin>``` - measure the frequency and duty cycle on pin \<pin> continuously. Press any key to exit.

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">LED-()></span> f 6
<span style="color:#bfa530">IO6 has no frequency measurement hardware!
Freq. measure is currently only possible on odd pins (1,3,5,7).
</span>
{{< /term >}}

Only half of the pins support frequency measurement. The Bus Pirate will warn you if hardware isn't available. To see which pins are currently available use the ```F``` command.



### ```=X``` Convert to HEX/DEC/BIN number format

{{< termfile  source="static/snippets/cmdref-convert.html" >}} 

Convert between HEX, DEC and BIN number formats easily. Type ```=``` followed by a number to see the HEX/DEC/BIN equivalent. 

- ```= <number>``` - Display the HEX/DEC/BIN equivalent of \<number>.  

{{% alert context="info" %}}
To change the Bus Pirate output display format see the [```o``` command]({{% relref "/docs/command-reference/#o-data-output-display-format" %}}).
{{% /alert %}}

### ```| X``` Reverse bits 

{{< termfile  source="static/snippets/cmdref-reverse.html" >}} 

Reverse bit order of a number. Displays the HEX/DEC/BIN value of the reversed number.

- ```| <number>``` - Reverse the bits in \<number>. 

{{% alert context="info" %}}
To change the Bus Pirate read/write bit order see the [```l```/```L``` command]({{% relref "/docs/command-reference/#ll-set-msblsb-first" %}}).
{{% /alert %}}

### ```a/A/@``` Auxiliary pin control (low/HIGH/read)
{{< termfile  source="static/snippets/cmdref-auxpin.html" >}} 

Pins that are not assigned a function can be controlled from the command line.
- ```a <pin>``` - set IO \<pin> low (0V).
- ```A <pin>``` - set pin X high (VCC).
- ```@ <pin>``` - set pin X to input (HiZ) and read the pin state. The pin state is reported as 0 or 1.

{{% alert context="warning" %}}
Pins already assigned a function, such as PWM or mode/protocol pins, cannot be changed with the a/A/@ commands. The Bus Pirate will report an error.
{{% /alert %}}

{{% alert context="info" %}}
Commands a/A/@ are followed by a space and the pin number to control. This is different than syntax a/A/@  which use the ```a.<pin>``` notation.
{{% /alert %}}

### ```logic``` Logic analyzer control

![](/images/docs/fw/logic-command-nav.png)

The ```logic``` command configures the logic analyzer core, and can display logic capture graphs directly in the terminal. It supports the "follow along" logic analyzer mode that triggers each time you send data to a bus. It eliminates the need setup triggers and arm a second tool for debugging. 

The Bus Pirate can be [used as a logic analyzer in multiple ways]({{< relref "/docs/logic-analyzer/logicanalyzer" >}}):
- [PulseView and the SUMP interface]({{< relref "/docs/logic-analyzer/pulseview-sump" >}})
- [PulseView With the "follow along logic analyzer" interface]({{< relref "/docs/logic-analyzer/pulseview-fala" >}})
- [Directly in the terminal with the ```logic``` command]({{< relref "/docs/logic-analyzer/logic-command" >}})

{{< termfile  source="static/snippets/cmdref-logic.html" >}}

## Disk Commands

Linux-like commands are used to navigate the flash storage from the Bus Pirate command line. 

| Command | Description | 
|---|---|
|```ls```|List files and directories|q
|```cd```|Change directory|
|```mkdir```|Make directory|
|```rm```|Remove file or directory|
|```cat```|Print file contents as text|
|```hex```|Print file contents in HEX|
|```format```|Format storage disk (FAT16)|
|```label```|Get or set the disk label|
|```dump```|Perform multiple reads with the ```r``` command, save to a file|
|```image```|Display a bitmap image file on the LCD|

These common commands are supported in the firmware as of this update, but always use ```help``` or ```?``` to see the latest commands available. Add -h to any command for extended help: ```hex -h```.

### ```ls``` List directory contents

{{< termfile  source="static/snippets/cmdref-disk-ls.html" >}}  

List the contents of a directory in flash storage. 
- ```ls``` - list the contents of the current directory. 
- ```ls <directory>``` - ls followed by a directory name lists the contents of that directory.

### ```mkdir``` Make directory

{{< termfile  source="static/snippets/cmdref-disk-mkdir.html" >}} 

Make a new directory at the current location in the flash storage. 
- ```mkdir <directory>``` - create a new directory.

### ```cd``` Change directory

{{< termfile  source="static/snippets/cmdref-disk-cd.html" >}} 

Change directory. 
- ```cd <directory>``` - change to a subdirectory.
- ```cd ..``` - change to the parent directory.

### ```rm``` Remove file or directory
{{< termfile  source="static/snippets/cmdref-disk-rm.html" >}} 

Remove file or directory (if empty). 
- ```rm <file | directory>``` - remove a file or empty directory.

### ```label``` Set disk label
{{< termfile  source="static/snippets/cmdref-label.html" >}} 

Set and get the disk label. 
- ```label set <label>``` - set the disk label. The label can be up to 11 characters long and must not contain spaces or special characters.
- ```label get``` - display the current disk label.


### ```format``` Erase and format disk
{{< termfile  source="static/snippets/cmdref-format.html" >}} 

Erase the internal flash storage and format it with a FAT16 file system. **ALL DATA WILL BE LOST!**
- ```format``` - format the entire flash storage, confirm twice. This will erase all files and directories on the disk.

### ```dump``` Dump read data to file
{{< termfile  source="static/snippets/cmdref-dump.html" >}}

- ```dump <bytes> <file>``` - read data using the current mode [```r``` bus command]({{< relref "/docs/command-reference/#r-read-byte">}}) and save it to a file.

{{% alert context="info" %}}
```dump``` is the equivalent of using the ```r``` command to read data from a device, but instead of displaying the data on the terminal, it saves it to a file.
{{% /alert %}}

This command is useful when you want to save data from a device to a file. While the Bus Pirate has commands to dump many chips, the ```dump``` command is a generic read command that can be used with any device.

First, manually send the commands to put the target device in read mode. Then use the ```dump``` command to read the data and save it to a file. 

### ```image``` Display bitmap image on LCD
{{< termfile  source="static/snippets/cmdref-image.html" >}}

- ```image <file>``` - shows the header info from ANY recognized BMP format (v1/2/3)
- ```image <file> -d``` - draw the file content on the LCD. Checks if the file is the correct height/width and a supported pixel format (16bits/565, or 24bit/888)

Load a bitmap image file and display it on the LCD. The Bus Pirate supports BMP format images. The image must be 128x64 pixels in size, and the pixel format must be 16bits/565 or 24bit/888. 

### ```cat``` Print file contents
{{< termfile  source="static/snippets/cmdref-cat.html" >}} 

Print the contents of a file. 
- ```cat <file>``` 

### ```hex``` Hex dump file
{{< termfile  source="static/snippets/hex-cmd-dump.html" >}} 
Print the content of a file in hexadecimal format.
- ```hex <file>``` 

{{% alert context="info" %}}
HEX values 0x00 and 0xFF are printed in white, over values are printed in blue. Printable ACSII characters are yellow, non printable characters are white. 
{{% /alert %}}

#### HEX dump part of a file
{{< termfile  source="static/snippets/hex-cmd-dump-partial.html" >}} 

```-s <start address>``` and ```-b <bytes>``` options can be used to print a part of the file in hexadecimal format.
- ```hex <file> -s <start address> -b <bytes>```

{{% alert context="info" %}}
The HEX display always aligns to a 16 byte boundary. Leading and trailing bytes you didn't request are dark grey.
{{% /alert %}}

#### HEX dump quiet flag
{{< termfile  source="static/snippets/hex-cmd-dump-quiet.html" >}} 

Many HEX editor tools allow you to paste HEX values directly. The ```-q``` option suppresses the header and footer, so you can copy multiple lines from the terminal and paste the output directly into a HEX editor.
- ```hex <file> -q``` - print the file in HEX format without the header and footer.

#### HEX command options

{{< termfile  source="static/snippets/hex-cmd-help.html" >}}

|Flag | Description |
|---|---|
|```-s <start address>```| Start address to read from. Default is 0x00.|
|```-b <bytes>```| Number of bytes to read. Default is all.|
|```-q```| Quiet mode, no address or ASCII columns. Useful for copying HEX values to a HEX editor.|

## Software support

The Bus Pirate has two USB serial ports. 
- One is used for the command line terminal. 
- The other supports support software running on a PC (binmode).

"binmode" supports a variety of protocols and software. 

- [SUMP logic analyzer protocol]({{% relref "/docs/binmode-reference/protocol-sump/"%}}) for [sigrok/PulseView]({{% relref "/docs/logic-analyzer/pulseview-sump/" %}})
- [Binmode test framework](https://forum.buspirate.com/t/bbio2-binary-mode/219/10?u=ian)
- Arduino CH32V003 SWIO
- [Follow Along Logic Analyzer protocol]({{% relref "http://localhost:1313/docs/binmode-reference/protocol-faladata/" %}}) for [sigrok/PulseView]({{% relref "/docs/logic-analyzer/pulseview-fala/" %}})
- [Legacy Binary Mode]({{% relref "/docs/binmode-reference/protocol-spi-legacy/" %}}) for [Flashrom]({{% relref "/docs/software/flashrom/" %}}) and [AVRdude]({{% relref "/docs/software/avrdude/"%}})
- [aIR]({{% relref "/docs/binmode-reference/protocol-air/" %}}) for [AnalysIR]({{% relref "/docs/software/analysir/" %}}).

### ```binmode``` Change binary mode 

{{< termfile  source="static/snippets/cmdref-binmode.html" >}} 

Use the ```binmode``` command see the currently supported binary modes and to select the active binmode.

### **PulseView** logic analyzer

![](/images/docs/fw/sigrok-capture.png)

Two modes are available for the PulseView logic analyzer. The SUMP mode is the default and is compatible with the SUMP protocol. The FALADATA mode is a custom protocol for the Bus Pirate.

### **AVRdude** AVR programmer

![](/images/docs/fw/avrdudess.png)

The Bus Pirate can serve as a programmer and dumper for AVR chips, using the command-line utility AVRDUDE. 

For those who prefer a graphical user interface, AVRDUDESS offers a user-friendly front-end for AVRDUDE. Both tools together provide a powerful setup for working with AVR chips.

### **Flashrom** flash programmer
```bash
flashrom.exe --progress -V -c "W25Q64JV-.Q" -p buspirate_spi:dev=COM54,serialspeed=115200,spispeed=1M -r flash_content.bin
```

The Bus Pirate can serve as a programmer and dumper for flash memory chips, using the command-line utility Flashrom.

Flashrom is a versatile utility for identifying, reading, writing, verifying, and erasing flash chips on a wide range of devices—including mainboards, controller cards, and various programmer modules. It supports hundreds of flash chips, chipsets, and boards.

### **AnalysIR** Infrared remote decoder


## Scripting commands

|Command | Description |
|---|---|
|```macro```| Load a set of macros|
|```script```| Run a script|
|```button```| Assign scripts to the button|
|```pause```| Pause and wait for user input|

There are multiple ways to script actions on the Bus Pirate.

### ```macro``` Load a set of macros

Macros are single line commands stored in a text file. The macro file can be changed as needed, so you can have different sets of macros for different tasks.

```
# This is my example macro file
#! Enable power supply 3.3V, 100mA limit
1:W 3.3 100
#! Read 5 bytes from an I2C EEPROM
2:[0xa0 0][0xa1 r:5]
```
Formatting is simple:
- Lines starting with ```#``` are comments.
- Lines starting with ```#!``` are macro help/descriptions.
- Lines starting with a number and a colon (```1:```) are macros. The number is the macro ID, and the text after the colon is the command to execute.

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">HiZ></span> macro -f macros.mcr
Set macro file: 'macros.mcr'
{{< /term >}}

Set the active macro file with the ```-f <file>``` flag. 

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">HiZ></span> macro -l
'macros.mcr' available macros:

<span style="color:#bfa530">#! Enable power supply 3.3V, 100mA limit</span>
<span style="color:#96cb59">1:W 3.3 100</span>
<span style="color:#bfa530">#! Read 5 bytes from an I2C EEPROM</span>
<span style="color:#96cb59">2:[0xa0 0][0xa1 r:5]</span>
{{< /term >}}

List the macros in the active macro file with the ```-l``` flag. 

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">HiZ></span> macro 1
Exec macro id: 1
W 3.3 100
{{< /term >}}

Execute a macro by its ID number.

|Flag | Description |
|---|---|
|```-f <file>```| Set the macro file to \<file>|
|```-l```| List the macros in the active macro file|
|```-h```| Show help|


### ```script``` Run a script
{{< termfile  source="static/snippets/cmdref-script.html" >}}

Script files are simple text files with one command per line. 

Lines starting with ```#``` are comments. Comments are displayed by default, but can be supressed with the ```-d``` flag.

```
# This is my example script file
# The 'pause' command waits for any key press
pause
# Did it pause?
```

This example uses the ```pause``` command to wait for user input.

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">HiZ></span> script example.scr
<span style="color:#bfa530"># This is my example script file</span>
<span style="color:#bfa530"># The 'pause' command waits for any key press</span>
<span style="color:#96cb59">HiZ></span> pause
Press any key

<span style="color:#bfa530"># Did it pause?</span>
{{< /term >}}

{{% alert context="info" %}}
To exit a running script type ```x```.
{{% /alert %}}

{{% alert context="warning" %}}
Scripts can only inject commands into the command line, not prompts or menus. 
{{% /alert %}}

```
# Enable power supply
W 3.3 50
```
This script works, everything is entered on the command line. 

```
# Show power supply menu
W
# Set 3.3 volts
3.3
# Set current limit to 50mA
50
```
This script does not work. Scripts cannot answer menu prompts. 

|Flag | Description |
|---|---|
|```-p```| Pause at each line, press ```enter``` to continue|
|```-d```| Do not display comments|
|```-x```| Exit the script on error|
|```-h```| Show help|

### ```button``` Assign scripts to the button
{{< termfile  source="static/snippets/cmdref-button.html" >}}

Scripts can be assigned to the Bus Pirate button. Scripts are the same format used with the ```script``` command above.
- By default short presses run ```button.scr```
- By default long presses run ```buttlong.scr```

Use the ```button``` command to change the script assigned to button presses, configure comment display, and set error handling. 

{{% alert context="warning" %}}
Button settings **do not** persist after a reboot.
{{% /alert %}}

|Flag | Description |
|---|---|
|```-f <file>```| Set the script file to run on button press|
|```-d```| Do not display comments|
|```-x```| Exit the script on error|
|```-h```| Show help|

### ```pause``` Pause and wait for user input
{{< termfile  source="static/snippets/cmdref-pause.html" >}}

- ```pause``` - pause and wait for user input. Press any key to continue.

Pause and wait for user input. Useful for pausing during a script or macro.

|Flag | Description |
|---|---|
|```-k```|Pause for any key press (default)|
|```-b```|Pause for button press|
|```-x```|Allow escape from scripts whit the 'x' key|

## Developer commands

|Command | Description |
|---|---|
|```bug```| Replicate a silicon bug|
|```otpdump```| Dump the OTP memory|
|```dummy```| Template for new commands|

A set of command useful or used during development. These commands are not intended for end users, but are available in the firmware.

### ```bug``` Replicate silicon bugs
{{< termfile  source="static/snippets/cmdref-bug.html" >}}

- ```bug <errata>``` - replicate a silicon bug in the Raspberry Pi Chip. 

This command is used for testing and debugging purposes.

### ```otpdump``` Dump OTP memory (BP 6+)
{{< termfile  source="static/snippets/cmdref-otpdump.html" >}}

- ```otpdump``` - dump the OTP memory of the Raspberry Pi chip.

Valid only on RP2350 or later chips with OTP memory (Bus Pirate 6+).

### ```dummy``` New command template
{{< termfile  source="static/snippets/cmdref-dummy.html" >}}

```dummy``` is a template that demonstrates how to create a new command.

If you want to add a new command to the Bus Pirate firmware, you can use this template as a starting point. 

## Bus commands

|Command | Description | Command| Description|
|---|---|---|---|
|```[```/```{```| Bus START condition|```^```| Clock pin tick|
|```>```| Execute bus commands (no START)|```/```| Clock pin high|
|```]```/```}```| Bus STOP condition|```\```| Clock pin low|
|```r```| Read byte|```-```|Data pin high|
|```0b01```| Write this binary value|```_```|Data pin low|
|```0x01```| Write this HEX value|```.```|Read data pin|
|```0d01```| Write this DEC value|
|```"abc"```| Write this ASCII string|
|``` ```| Value delimiter|
|```d```/```D```| Delay (us/ms)|
|```:```| Repeat command|
|```.```| Specify bits to read/write|
|```v.<pin>```| Read voltage on \<pin>|
|```a.<pin>```/```A.<pin>```/```@.<pin>```| Auxillary pin control (low/HIGH/input) |

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">SPI></span> [0x31 r:5]
<span style="color:#bfa530">CS Select (0)</span>
<span style="color:#bfa530"><span style="color:#bfa530">TX:</span></span> 0x<span style="color:#53a6e6">31</span>
<span style="color:#bfa530"><span style="color:#bfa530">RX:</span></span> 0x<span style="color:#53a6e6">00</span> 0x<span style="color:#53a6e6">00</span> 0x<span style="color:#53a6e6">00</span> 0x<span style="color:#53a6e6">00</span> 0x<span style="color:#53a6e6">00</span>
<span style="color:#bfa530">CS Deselect (1)</span>
<span style="color:#96cb59">SPI></span> 
{{< /term >}}

A simple bus commands are used to interact with devices in various protocols. Bus command characters have the same general function in each bus mode, such as ```r``` to read a byte of data.

This example sends a bus start, the value 0x31, and then reads 5
bytes, followed by bus stop. Up to 255 characters may be
entered into the Bus Pirate terminal at once, press ```enter``` to execute the
commands.

{{% alert context="info" %}}
**Bus commands must start with ```[```, ```{```, or ```>```.**
{{% /alert %}}

### ```[ or {``` Bus START condition

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">SPI></span> [
<span style="color:#bfa530">CS Select (0)</span>
<span style="color:#96cb59">SPI></span>
{{< /term >}}

START commands generate a START condition (I2C), a RESET (1-Wire, LED), chip select (SPI) and have similar START type functions in most modes. A line beginning with START is interpreted as bus commands. 

- ```[``` - send the START condition for the currently selected bus mode.
- ```{``` - send the alternate START condition for the currently selected bus mode.

Check the protocol documentation below to see what START and alternate START do in each mode. [In SPI mode]({{< relref "/docs/command-reference/#bus-commands-5">}}), for example, ```[``` selects a chip, while ```{``` selects the chip and displays each byte received when data is written (write with read mode).

{{% alert context="info" %}}
Lines beginning with ```[``` and ```{``` are interpreted as bus commands, data will be sent to the device in the current protocol selected with the [```m``` command]({{% relref "/docs/command-reference/#m-set-bus-mode" %}}).
{{% /alert %}}

### ```>``` Execute bus commands (no START)

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">SPI></span> > 0x55 0xaa

<span style="color:#bfa530">TX:</span> 0x<span style="color:#53a6e6">55</span> 0x<span style="color:#53a6e6">AA</span> 
<span style="color:#96cb59">SPI></span> 
{{< /term >}}

If you want to execute bus commands without sending a START, use the ```>``` bus command. Lines beginning with ```>``` are also executed as bus commands.

- ```>``` - start a line with ```>``` to send bus commands without sending a START condition. 

{{% alert context="info" %}}
The ```>``` command is used to send syntax without sending a START command to the bus.
{{% /alert %}}

### ```] or }``` Bus STOP condition

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">SPI></span> >]
<span style="color:#bfa530">CS Deselect (1)</span>
<span style="color:#96cb59">SPI></span> 
{{< /term >}}

Many protocols have a STOP condition. In various modes ```]``` and ```}``` STOPs (I2C), deselects
(SPI), or closes (UART).

- ```]``` - send the STOP condition for the currently selected bus mode.
- ```}``` - send the alternate STOP condition for the currently selected bus mode.

### ```r``` Read byte 

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">SPI></span> >r
<span style="color:#bfa530"><span style="color:#bfa530">RX:</span></span> 0x<span style="color:#53a6e6">00</span>
<span style="color:#96cb59">SPI></span> 
{{< /term >}}

- ```r``` - read a byte from the bus. Use with the [repeat command]({{% relref "/docs/command-reference/#-repeat-eg-r10" %}}) (r:1...255) for bulk reads.

{{% alert context="info" %}}
The ```>``` before ```r``` tells the Bus Pirate we want to send bus commands.
{{% /alert %}}

### ```0b01``` Write this binary value 

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">SPI></span> >0b01
<span style="color:#bfa530"><span style="color:#bfa530">TX:</span></span> 0b<span style="color:#53a6e6">0000</span>0001
<span style="color:#96cb59">SPI></span> 
{{< /term >}}

[Binary](http://en.wikipedia.org/wiki/Binary_numeral_system) values are
commonly used in electronics because the 1s and 0s correspond to
register 'switches' that control various aspects of a device. When used as part of a bus command, the Bus Pirate will write the value in the currently selected bus protocol.

Begin a binary number with ```0b```, followed by the bits. Padding 0's are not required,
0b00000001=0b1. Can be used with the [repeat command]({{% relref "/docs/command-reference/#-repeat-eg-r10" %}}) (0b110:1...255) for bulk writes.  

- ```0b0``` - binary "0".
- ```0b1``` - binary "1".
- ```0b11111111``` - binary "255".

{{% alert context="info" %}}
The ```>``` before ```0b01``` tells the Bus Pirate we want to send bus commands.
{{% /alert %}}

### ```0x01``` Write this HEX value 

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">SPI></span> >0x01
<span style="color:#bfa530"><span style="color:#bfa530">TX:</span></span> 0x<span style="color:#53a6e6">01</span>
<span style="color:#96cb59">SPI></span> 
{{< /term >}}

[Hexadecimal](http://en.wikipedia.org/wiki/Hexadecimal) values are base
16 numbers that use a-f for the numbers 10-15, this format is very
common in computers and electronics. When used as part of a bus command, the Bus Pirate will write the value in the currently selected bus protocol.

Begin a hexadecimal number with ```0x``` or ```0h```, followed by the hex digits. A-F can be lowercase or uppercase letters. Padding 0's are not required, 0x05=0x5. Hexadecimal numbers can be used with the [repeat command]({{% relref "/docs/command-reference/#-repeat-eg-r10" %}}) (0xff:1...255) for bulk writes.

- ```0x0``` - hexadecimal "0".
- ```0x1``` - hexadecimal "1".
- ```0xff``` - hexadecimal "255".

{{% alert context="info" %}}
The ```>``` before ```0x01``` tells the Bus Pirate we want to send bus commands.
{{% /alert %}}

### ```0-255``` Write this decimal value

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">SPI></span> >1
<span style="color:#bfa530"><span style="color:#bfa530">TX:</span></span> 1
<span style="color:#96cb59">SPI></span>
{{< /term >}}

Any number not started with 0b, 0x or 0h is interpreted as a decimal value. [Decimal](http://en.wikipedia.org/wiki/Decimal) values are common base 10 numbers. Just enter the value, no special prefix is required. Decimal numbers can be used with the [repeat command]({{% relref "/docs/command-reference/#-repeat-eg-r10" %}}) (10:1...255) for bulk writes.

- ```0``` - decimal "0".
- ```1``` - decimal "1".
- ```255``` - decimal "255".

{{% alert context="info" %}}
The ```>``` before ```1``` tells the Bus Pirate we want to send bus commands.
{{% /alert %}}

### ```"abc"``` Write this ASCII string 

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">SPI></span> >"abc"
<span style="color:#bfa530"><span style="color:#bfa530">TX:</span></span> 'a' 0x<span style="color:#53a6e6">61</span> 'b' 0x<span style="color:#53a6e6">62</span> 'c' 0x<span style="color:#53a6e6">63</span> 
{{< /term >}}

Characters enclosed in ```" "``` are sent to the bus as their [ASCII equivalent codes](https://en.wikipedia.org/wiki/ASCII). Useful for writing text strings when programming flash chips, interfacing UARTs, etc.

- ```"abc"``` - Write the ASCII string "abc" to the bus, equivalent to 0x61 0x62 0x63.

{{% alert context="info" %}}
The ```>``` before ```"abc"``` tells the Bus Pirate we want to send bus commands.
{{% /alert %}} 

### ```space``` Value delimiter

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">SPI></span> [1 2 3  rr]
<span style="color:#bfa530">CS Select (0)</span>
<span style="color:#bfa530"><span style="color:#bfa530">TX:</span></span> 1
<span style="color:#bfa530"><span style="color:#bfa530">TX:</span></span> 2
<span style="color:#bfa530"><span style="color:#bfa530">TX:</span></span> 3
<span style="color:#bfa530"><span style="color:#bfa530">RX:</span></span> 0x<span style="color:#53a6e6">00</span>
<span style="color:#bfa530"><span style="color:#bfa530">RX:</span></span> 0x<span style="color:#53a6e6">00</span>
<span style="color:#bfa530">CS Deselect (1)</span>
<span style="color:#96cb59">SPI></span>
{{< /term >}}

Use a space to separate numbers.

- ``` ``` - space is used to separate numbers on the command line. 

{{% alert context="info" %}}
No delimiter is required between non-number commands.
{{% /alert %}}

### ```d/D``` Delay 1uS/MS 

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">SPI></span> >d
<span style="color:#bfa530"><span style="color:#bfa530">Delay:</span></span> <span style="color:#53a6e6">1</span>us
<span style="color:#96cb59">SPI></span> >d:10
<span style="color:#bfa530"><span style="color:#bfa530">Delay:</span></span> <span style="color:#53a6e6">10</span>us
<span style="color:#96cb59">SPI></span> >D
<span style="color:#bfa530"><span style="color:#bfa530">Delay:</span></span> <span style="color:#53a6e6">1</span>ms
<span style="color:#96cb59">SPI></span> >D:10
<span style="color:#bfa530"><span style="color:#bfa530">Delay:</span></span> <span style="color:#53a6e6">10</span>ms
<span style="color:#96cb59">SPI></span> 
{{< /term >}}

Delay in microseconds or milliseconds. Delays can be extended with the [repeat command]({{% relref "/docs/command-reference/#-repeat-eg-r10" %}}) (d:1...255).

- ```d``` - delays 1us.
- ```d:10``` - delay 10us.
- ```D``` - delays 1ms. 
- ```D:10``` - delay 10ms.

{{% alert context="info" %}}
The ```>``` before ```d``` tells the Bus Pirate we want to send bus commands.
{{% /alert %}}

### ```:``` Repeat (e.g. r:10) 

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">SPI></span> [ 0x55:2 D:3 r:3]
<span style="color:#bfa530">CS Select (0)</span>
<span style="color:#bfa530"><span style="color:#bfa530">TX:</span></span> 0x<span style="color:#53a6e6">55</span> 0x<span style="color:#53a6e6">55</span>
<span style="color:#bfa530"><span style="color:#bfa530">Delay:</span></span> <span style="color:#53a6e6">2</span>ms
<span style="color:#bfa530"><span style="color:#bfa530">RX:</span></span> 0x<span style="color:#53a6e6">00</span> 0x<span style="color:#53a6e6">00</span> 0x<span style="color:#53a6e6">00</span>
<span style="color:#bfa530">CS Deselect (1)</span>
<span style="color:#96cb59">SPI></span> 
{{< /term >}}

Many commands can be repeated by adding ```:```, followed by the number of times to repeat. To read five bytes, enter ```r:5```, etc. 

- ```0x55:2``` - write 0x55 to the bus twice.
- ```D:3``` - delay 3ms.
- ```r:3``` - read 3 bytes from the bus.

{{% alert context="info" %}}
Repeat values can also be HEX/DEC/BIN formatted.
{{% /alert %}}

### ```.``` Specify number of bits to read/write 

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">SPI></span> >0x5a.4
<span style="color:#bfa530"><span style="color:#bfa530">TX:</span></span> 0x<span style="color:#53a6e6">0A</span>.4
<span style="color:#96cb59">SPI></span>
{{< /term >}}

Write/read partial bytes (where enabled by hardware) using the ```.``` option. ```0x75.4``` will write 0x5 (4 bits) to the bus. 

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">SPI></span> >r.4
<span style="color:#bfa530"><span style="color:#bfa530">RX:</span></span> 0x<span style="color:#53a6e6">05</span>.4
<span style="color:#96cb59">SPI></span>
{{< /term >}}

Read 4 bits from the bus.

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">SPI></span> >0x5432.12
<span style="color:#bfa530"><span style="color:#bfa530">TX:</span></span> 0x<span style="color:#53a6e6">04</span>32.12
<span style="color:#96cb59">SPI></span>
{{< /term >}}

Write 12 bits of 0x5432 to the bus.

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">SPI></span> >0x5a.4:2
<span style="color:#bfa530"><span style="color:#bfa530">TX:</span></span> 0x<span style="color:#53a6e6">0a</span>.4 0x<span style="color:#53a6e6">0a</span>.4
<span style="color:#96cb59">SPI></span> 
{{< /term >}}

Partial write/reads can be combined with the repeat command.

### ```v``` Measure voltage

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">SPI></span> > v.1 v.2 v.3

<span style="color:#bfa530">Volts on IO1:</span> <span style="color:#53a6e6">3.2</span>V
<span style="color:#bfa530">Volts on IO2:</span> <span style="color:#53a6e6">3.2</span>V
<span style="color:#bfa530">Volts on IO3:</span> <span style="color:#53a6e6">3.2</span>V
<span style="color:#96cb59">SPI></span> 
{{< /term >}}

It is possible to measure the voltage of any IO pin while executing bus commands.

- ```v.<pin>``` - measure the voltage on IO pin \<pin>

{{% alert context="info" %}}
The ```>``` before ```v.1 v.2 v.3``` tells the Bus Pirate we want to send bus commands.
{{% /alert %}}

### ```a/A/@``` Auxiliary pin control (low/HIGH/read)

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">UART></span> >a.1
<span style="color:#bfa530">IO<span style="color:#53a6e6">1<span style="color:#bfa530"> set to</span></span></span> OUTPUT: <span style="color:#53a6e6">0</span>

<span style="color:#96cb59">UART></span> >A.1
<span style="color:#bfa530">IO<span style="color:#53a6e6">1<span style="color:#bfa530"> set to</span></span></span> OUTPUT: <span style="color:#53a6e6">1</span>

<span style="color:#96cb59">UART></span> >@.1
<span style="color:#bfa530">IO<span style="color:#53a6e6">1<span style="color:#bfa530"> set to</span></span></span> INPUT: <span style="color:#53a6e6">0</span>

<span style="color:#96cb59">UART></span>
{{< /term >}}

Sometimes it's useful to control IO pins directly when executing bus commands.

- ```a.<pin>``` - set \<pin> low (0V).
- ```A.<pin>``` - set \<pin> high (VCC).
- ```@.<pin>``` - set \<pin> to input (HiZ) and read the pin state. The pin state is reported as 0 or 1.

{{% alert context="warning" %}}
Pins already assigned a function, such as PWM or mode/protocol pins, cannot be changed with the a/A/@ commands. The Bus Pirate will report an error.
{{% /alert %}}

{{% alert context="info" %}}
Bus commands a/A/@ use the ```a.<pin>``` notation, the syntax is followed by a **.** and the pin number to control. This is different than the commands a/A/@, which are followed by a space and the pin number to control.
{{% /alert %}}

### ```^``` Clock pin tick (limited)

{{< termfile  source="static/snippets/cmdref-bitwise-tick.html" >}}

Send a single clock tick to the bus. The clock pin is set high (VCC) for a short time, then set low (0V).

{{% alert context="warning" %}}
"Bitwise" commands provide low-level control over the clock and data pins, allowing precise manipulation of their states. These commands are only available in specific modes, such as 2WIRE and 3WIRE.
{{% /alert %}}

### */* Clock pin high (limited)

{{< termfile  source="static/snippets/cmdref-bitwise-clock-high.html" >}}

Set the clock pin high (VCC).

{{% alert context="warning" %}}
"Bitwise" commands provide low-level control over the clock and data pins, allowing precise manipulation of their states. These commands are only available in specific modes, such as [2WIRE]({{% relref "/docs/command-reference/#2-wire" %}}) and [3WIRE]({{% relref "/docs/command-reference/#3-wire" %}}).
{{% /alert %}}

### \\ Clock pin low (limited)

{{< termfile  source="static/snippets/cmdref-bitwise-clock-low.html" >}}

Set the clock pin low (0V).

{{% alert context="warning" %}}
"Bitwise" commands provide low-level control over the clock and data pins, allowing precise manipulation of their states. These commands are only available in specific modes, such as [2WIRE]({{% relref "/docs/command-reference/#2-wire" %}}) and [3WIRE]({{% relref "/docs/command-reference/#3-wire" %}}).
{{% /alert %}}

### *-* Data pin high (limited)

{{< termfile  source="static/snippets/cmdref-bitwise-data-high.html" >}}

Set the data pin high (VCC).

{{% alert context="warning" %}}
"Bitwise" commands provide low-level control over the clock and data pins, allowing precise manipulation of their states. These commands are only available in specific modes, such as [2WIRE]({{% relref "/docs/command-reference/#2-wire" %}}) and [3WIRE]({{% relref "/docs/command-reference/#3-wire" %}}).
{{% /alert %}}

### *_* Data pin low (limited)

{{< termfile  source="static/snippets/cmdref-bitwise-data-low.html" >}}

Set the data pin low (0V).

{{% alert context="warning" %}}
"Bitwise" commands provide low-level control over the clock and data pins, allowing precise manipulation of their states. These commands are only available in specific modes, such as [2WIRE]({{% relref "/docs/command-reference/#2-wire" %}}) and [3WIRE]({{% relref "/docs/command-reference/#3-wire" %}}).
{{% /alert %}}

### *.* Read data pin (limited)

{{< termfile  source="static/snippets/cmdref-bitwise-data-read.html" >}}

Read the current state of the data pin.

{{% alert context="warning" %}}
"Bitwise" commands provide low-level control over the clock and data pins, allowing precise manipulation of their states. These commands are only available in specific modes, such as [2WIRE]({{% relref "/docs/command-reference/#2-wire" %}}) and [3WIRE]({{% relref "/docs/command-reference/#3-wire" %}}).
{{% /alert %}}

## Supported bus protocols

| | | |
|---|---|---|
|HiZ|1WIRE|UART|
|HDUART|I2C|SPI|
|2WIRE|3WIRE|DIO|
|LED|INFRARED|JTAG|

The Bus Pirate supports a variety of bus protocols. Each protocol has its own set of commands and features. Select a protocol with the [```m``` command]({{% relref "/docs/command-reference/#m-set-bus-mode" %}}).

Several protocols have sub modes such as LED and INFRARED.

{{% alert context="info" %}}
Always update to the latest firmware as protocols are frequently improved and new protocols added.
{{% /alert %}}

## HiZ

-   **Bus:** High impedance (HiZ)
-   **Connections:** none
-   **Output type:** not allowed
-   **Pull-up resistors:** not allowed
-   **Maximum voltage:** 5 volts

HiZ is the default Bus Pirate mode. It is a safe mode: all outputs and hardware are disabled. 

To change into a protocol mode, use the [```m``` command]({{% relref "/docs/command-reference/#m-set-bus-mode" %}}).

{{% alert context="info" %}}
HiZ is a safe mode. If something goes wrong with your target device, switch to safe mode to disable all outputs and hardware.
{{% /alert %}}

## 1-Wire

-   **Bus:** [1-Wire](https://en.wikipedia.org/wiki/1-Wire)
-   **Connections:** one data pin (OWD) and ground
-   **Output type:** open drain/open collector
-   **Pull-up resistors:** always required (2K - 10K ohms)
-   **Maximum voltage:** 5volts

1-Wire is a single wire bus for low speed interfaces.

### Pull-up resistors

1-Wire is an open-collector bus, it requires pull-up resistors to hold the
data line high and create the data '1'. 1-Wire parts don't
output high, they only pull low. Without pull-up resistors there can
never be a '1'. 

Enable the Bus Pirate onboard pull-up resistors with the [```P``` command]({{% relref "/docs/command-reference/#pp-pull-up-resistors"%}}).

{{% alert context="info" %}}
- 1-Wire requires a pull-up resistor to hold the data line high.
- 1-Wire parts don't output high, they only pull low.
- Without pull-up resistors there can never be a '1'. 
- Enable the Bus Pirate onboard pull-up resistors with the ```P``` command.
{{% /alert %}}

### Connections

| Bus Pirate | Direction                     | Circuit | Description   |
|------------|--------------------------|---------|---------------|
| OWD       | <font size="+2">↔</font> | OWD     | 1-Wire Data   |
| GND        | <font size="+2">⏚</font> | GND     | Signal Ground |

### Bus commands

|Command|Description|
|-------|-----------|
| \{ or [ | Issue 1-Wire reset, detect device presence. |
| r       | Read one byte. (r:1…255 for bulk reads)|
| 0b      | Write this binary value. Format is 0b00000000 for a byte, but partial bytes are also fine: 0b1001.|
| 0x      | Write this HEX value. Format is 0x01. Partial bytes are fine: 0xA. A-F can be lower-case or capital letters. |
| 0-255   | Write this decimal value. Any number not preceded by 0x or 0b is interpreted as a decimal value. |
| ```space```| Value delimiter. Use a space to separate numbers. No delimiter is required between non-number values: \{0xa6 0 0 16 5 0b111 0xaF rrrr}. |

{{% readfile "/_common/other-commands.md" %}}

### ```scan``` 1-Wire address search

{{< termfile source="static/snippets/ds18b20-scan.html" >}}

- ```scan``` - perform a 1-Wire ROM search.

```scan``` performs a 1-Wire ROM search to detect the ID of every connected 1-Wire device. The type of device is shown if the family ID is known.

### ```eeprom``` Read, write, erase, verify, test, dump 1-Wire EEPROMs


{{< asciicast src="/screencast/1wire-eeprom-command-cast.json" poster="npt:0:43"  idleTimeLimit=2 >}}
<br/>
```eeprom``` is a command to read, write, erase, verify, test and dump common GX/DS243x 1-Wire EEPROMs. 


#### 1-Wire EEPROM list supported devices

{{< termfile source="static/snippets/1wire-eeprom-command-list.html" >}}

- ```eeprom list``` - list all EEPROM devices supported by the ```eeprom``` command

| Device  | Size| Bytes | Page Size | Addr Bytes | Blk Sel Bits | kHz max |
|---------|-----|--|-----------|------------|--------------|---------|
| [DS2431](https://www.analog.com/media/en/technical-documentation/data-sheets/DS2431.pdf)/GX2431  | 1K |128   | 8         | 2          | 0            | 16      |
| [DS24B33](https://www.analog.com/media/en/technical-documentation/data-sheets/ds24b33.pdf)  | 4K |512   | 32        | 2          | 0          | 16      |

{{% alert context="info" %}}
There are only two widely used 1-Wire EEPROM: DS2431+ (1Kbit) and DS24B33 (4Kbit). There is also a clone of the DS2431+ called GX2431.
{{% /alert %}}

{{% alert context="danger" %}}
The ```eeprom``` command uses the "skip ROM" method to access the EEPROM. This means that only one EEPROM can be connected to the 1-Wire bus at a time. If you have multiple EEPROMs, you must disconnect all but one before using the ```eeprom``` command.
{{% /alert %}}

##### Chip voltage requirements

|Family|Minimum Voltage|Maximum Voltage|
|---|---|---|---|
|DS243X|2.8V|5.25V|


Before using the ```eeprom``` command, you'll need to enable a power supply with the [```W``` command]({{< relref "/docs/command-reference/#ww-power-supply-offon">}}) and pull-up resistors with the [```P``` command]({{< relref "/docs/command-reference/#pp-pull-up-resistors">}}).

{{% alert context="danger" %}}
**1-Wire EEPROMs are powered from the bus data line, not a supply pin.** If EEPROM writes fail you may need to add a 2K or smaller pull-up resistor between a power supply (VOUT) and the 1-Wire data pin.
{{% /alert %}}

#### 1-Wire EEPROM dump to terminal

{{< termfile source="static/snippets/1wire-eeprom-command-dump-partial.html" >}}

Display the contents of an EEPROM in the terminal. 
- ```eeprom dump -d <device>``` - display EEPROM contents
- ```eeprom dump -d <device> -s <start>``` - display EEPROM contents, starting at address `<start>`
- ```eeprom dump -d <device> -s <start> -b <bytes>``` - display a specific range of bytes, starting at address `<start>` and reading `<bytes>` bytes

#### 1-Wire EEPROM read to file
{{< term  >}}
<span style="color:rgb(150,203,89)">1WIRE></span>&nbsp;eeprom&nbsp;read&nbsp;-d&nbsp;ds2431&nbsp;-f&nbsp;eeprom.bin&nbsp;-v
DS2431:&nbsp;128&nbsp;bytes,&nbsp;&nbsp;0&nbsp;block&nbsp;select&nbsp;bits,&nbsp;2&nbsp;byte&nbsp;address,&nbsp;8&nbsp;byte&nbsp;pages

Read:&nbsp;Reading&nbsp;EEPROM&nbsp;to&nbsp;file&nbsp;eeprom.bin...
Progress:&nbsp;[###########################]&nbsp;100.00%
Read&nbsp;complete
Read&nbsp;verify...
Progress:&nbsp;[###########################]&nbsp;100.00%
Read&nbsp;verify&nbsp;complete
Success&nbsp;:)

<span style="color:rgb(150,203,89)">1WIRE></span>&nbsp;
{{< /term>}}

Read the contents of an EEPROM and save it to a file.
- ```eeprom read -d <device> -f <file>``` - read EEPROM contents to file `<file>`
- ```eeprom read -d <device> -f <file> -v``` - read EEPROM contents to file `<file>`, verify the read operation

#### 1-Wire EEPROM write from file
{{< term  >}}
<span style="color:rgb(150,203,89)">1WIRE></span>&nbsp;eeprom&nbsp;write&nbsp;-d&nbsp;ds2431&nbsp;-f&nbsp;eeprom.bin&nbsp;-v
DS2431:&nbsp;128&nbsp;bytes,&nbsp;&nbsp;0&nbsp;block&nbsp;select&nbsp;bits,&nbsp;2&nbsp;byte&nbsp;address,&nbsp;8&nbsp;byte&nbsp;pages

Write:&nbsp;Writing&nbsp;EEPROM&nbsp;from&nbsp;file&nbsp;eeprom.bin...
Progress:&nbsp;[###########################]&nbsp;100.00%
Write&nbsp;complete
Write&nbsp;verify...
Progress:&nbsp;[###########################]&nbsp;100.00%
Write&nbsp;verify&nbsp;complete
Success&nbsp;:)

<span style="color:rgb(150,203,89)">1WIRE></span>&nbsp;
{{< /term>}}
Write the contents of a file to an EEPROM.
- ```eeprom write -d <device> -f <file>``` - write EEPROM from file `<file>`
- ```eeprom write -d <device> -f <file> -v``` - write EEPROM from file `<file>`, verify the write operation

{{% alert context="danger" %}}
If the **file is bigger than the EEPROM**, only the first bytes of the file will be written to the EEPROM. The rest of the file will be ignored.

If the **file is smaller than the EEPROM**, the full file will be written to the EEPROM, and the rest of the EEPROM will be left unchanged. The eeprom command will read the target page from the EEPROM, write the new data to the page, and then write the full page back to the EEPROM. This is done to avoid writing partial pages, which some devices cannot handle.
{{% /alert %}}

#### 1-Wire EEPROM verify against file
{{< term  >}}
<span style="color:rgb(150,203,89)">1WIRE></span>&nbsp;eeprom&nbsp;verify&nbsp;-d&nbsp;ds2431&nbsp;-f&nbsp;eeprom.bin
DS2431:&nbsp;128&nbsp;bytes,&nbsp;&nbsp;0&nbsp;block&nbsp;select&nbsp;bits,&nbsp;2&nbsp;byte&nbsp;address,&nbsp;8&nbsp;byte&nbsp;pages

Verify:&nbsp;Verifying&nbsp;EEPROM&nbsp;contents&nbsp;against&nbsp;file&nbsp;eeprom.bin...
Progress:&nbsp;[###########################]&nbsp;100.00%
Verify&nbsp;complete

<span style="color:rgb(150,203,89)">1WIRE></span>&nbsp;
{{< /term>}}
Verify the contents of an EEPROM match a file.
- ```eeprom verify -d <device> -f <file>``` - verify EEPROM contents against file `<file>`

{{% alert context="danger" %}}
If the **file is bigger than the EEPROM**, only the first bytes of the file will be verified against the EEPROM. The rest of the file will be ignored.

If the **file is smaller than the EEPROM**, the full file will be verified against the EEPROM, and the rest of the EEPROM will be ignored.
{{% /alert %}}

#### 1-Wire EEPROM erase
{{< term  >}}
<span style="color:rgb(150,203,89)">1WIRE></span>&nbsp;eeprom&nbsp;erase&nbsp;-d&nbsp;ds2431&nbsp;-v
DS2431:&nbsp;128&nbsp;bytes,&nbsp;&nbsp;0&nbsp;block&nbsp;select&nbsp;bits,&nbsp;2&nbsp;byte&nbsp;address,&nbsp;8&nbsp;byte&nbsp;pages

Erase:&nbsp;Writing&nbsp;0xFF&nbsp;to&nbsp;all&nbsp;bytes...
Progress:&nbsp;[###########################]&nbsp;100.00%
Erase&nbsp;complete
Erase&nbsp;verify...
Progress:&nbsp;[###########################]&nbsp;100.00%
Erase&nbsp;verify&nbsp;complete
Success&nbsp;:)

<span style="color:rgb(150,203,89)">1WIRE></span>&nbsp;
{{< /term>}}

Erase the contents of an EEPROM, writing 0xFF to all bytes.
- ```eeprom erase -d <device>``` - erase EEPROM contents
- ```eeprom erase -d <device> -v``` - erase EEPROM contents, verify the erase operation
#### 1-Wire EEPROM test
{{< term  >}}
<span style="color:rgb(150,203,89)">1WIRE></span>&nbsp;eeprom&nbsp;test&nbsp;-d&nbsp;ds2431
DS2431:&nbsp;128&nbsp;bytes,&nbsp;&nbsp;0&nbsp;block&nbsp;select&nbsp;bits,&nbsp;2&nbsp;byte&nbsp;address,&nbsp;8&nbsp;byte&nbsp;pages

Erase:&nbsp;Writing&nbsp;0xFF&nbsp;to&nbsp;all&nbsp;bytes...
Progress:&nbsp;[###########################]&nbsp;100.00%
Erase&nbsp;complete
Erase&nbsp;verify...
Progress:&nbsp;[###########################]&nbsp;100.00%
Erase&nbsp;verify&nbsp;complete

Test:&nbsp;Writing&nbsp;alternating&nbsp;patterns
Writing&nbsp;0xAA&nbsp;0x55...
Progress:&nbsp;[###########################]&nbsp;100.00%
Write&nbsp;complete
Write&nbsp;verify...
Progress:&nbsp;[###########################]&nbsp;100.00%
Write&nbsp;verify&nbsp;complete
Writing&nbsp;0x55&nbsp;0xAA...
Progress:&nbsp;[###########################]&nbsp;100.00%
Write&nbsp;complete
Write&nbsp;verify...
Progress:&nbsp;[###########################]&nbsp;100.00%
Write&nbsp;verify&nbsp;complete
Success&nbsp;:)

<span style="color:rgb(150,203,89)">1WIRE></span>&nbsp;
{{< /term>}}

Test EEPROM functionality. Erase the EEPROM to 0xff and verify the erase. Then write alternating patterns of 0xAA and 0x55, verifying each write operation. Any stuck bits should be detected during the test.
- ```test -d <device>``` - test EEPROM functionality

#### 1-Wire EEPROM show protection status
{{< termfile source="static/snippets/1wire-eeprom-command-protect.html" >}}
Show the write protection status of the EEPROM.
- ```eeprom protection -d <device>``` - show the protection status of the EEPROM 

#### 1-Wire EEPROM options and flags

{{< termfile source="static/snippets/1wire-eeprom-command-help.html" >}}

|Option|Description|
|---|---|
|```eeprom list```|List all supported EEPROM devices|
|```eeprom dump```|Dump EEPROM contents to terminal.Space to continue, x to exit.|
|```eeprom read```|Read EEPROM contents to file|
|```eeprom write```|Write EEPROM from file|
|```eeprom verify```|Verify EEPROM contents against file|
|```eeprom erase```|Erase EEPROM contents, writing 0xFF to all bytes|
|```eeprom test```|Test EEPROM functionality, erase and write alternating patterns|
|```eeprom protect```|Show the write protection status of the EEPROM|

Options tell the eeprom command what to do.

{{% alert context="info" %}}
Always check the latest options and flags with ```eeprom -h``` to see the most up-to-date features.
{{% /alert %}}

|Flag|Description|
|---|---|
|```-d <device>```|Specify the EEPROM device type, e.g. 24x02|
|```-f <file>```|Specify the file for read, write and verify|
|```-v```|Verify the read or write operation|
|```-s <start>```|Specify the start address for dump operations|
|```-b <bytes>```|Specify the number of bytes to read for dump operations|
|```-q```|Dump quiet mode, no address or ASCII columns. Useful for copying HEX values to a HEX editor.|
|```-c```|Dump: disable paging, display all data in one go.|
|```-h```|Show help for the ```eeprom``` command|

Flags pass file names and other settings.



### ```ds18b20``` Read temperature

{{< termfile source="static/snippets/ds18b20-command.html" >}}

- ```ds18b20``` - read the temperature from a single DS18B20 device. 

```ds18b20``` reads the temperature from a single [18B20 temperature sensor]({{% relref "/docs/devices/ds18b20" %}}). The temperature is displayed in Celsius.

{{% alert context="warning" %}}
The device is accessed with the skip ROM command, so it will only work with a single DS18B20 device connected.
{{% /alert %}}

### Device demos
- [DS18B20 Temperature Sensor]({{% relref "/docs/devices/ds18b20" %}})


## UART
-   **Bus:** [UART](http://en.wikipedia.org/wiki/Serial_uart),
    [MIDI](http://en.wikipedia.org/wiki/Musical_Instrument_Digital_Interface)
    (universal asynchronous receiver transmitter)
-   **Connections:** two data pins (RX/TX) and ground
-   **Output type:** push-pull (1.65-5volts). Powered by onboard supply or an external voltage on the VOUT/VREF pin
-   **Maximum Voltage:** 5volts

{{% alert context="warning" %}}
UART is also known as the common PC serial port. The PC serial port
operates at full RS232 voltage levels (-13volts to +13volts) though,
which are not compatible with the Bus Pirate without an [RS232 adapter]({{% relref "/docs/overview/dual-rs232-adapter/" %}}).
{{% /alert %}}

### Connections
| Bus Pirate | Direction                     | Circuit | Description   |
|------------|--------------------------|---------|---------------|
| TX       | <font size="+2">→</font> | RX    | Bus Pirate Transmit   |
| RX        | <font size="+2">←</font> | TX     | Bus Pirate Receive  |
| GND        | <font size="+2">⏚</font> | GND     | Signal Ground |

Connect the Bus Pirate transmit pin (TX) to the UART device receive
pin (RX). Connect the Bus Pirate receive pin (RX) to the UART
device transmit pin (TX).

### Configuration options

{{< termfile source="static/snippets/cmdref-mode-uart-config.html" >}}

### Bus commands

|Command| Description  |
|---------|-------|
| [      | Open UART, use ```r``` to read bytes. |
| \{       | Open UART, display data as it arrives asynchronously. |
| \] or } | Close UART.  |
| r       | Check UART for byte, or fail if empty. (r:1…255 for bulk reads) |
| 0b      | Write this binary value. Format is 0b00000000 for a byte, but partial bytes are also fine: 0b1001.|
| 0x      | Write this HEX value. Format is 0x01. Partial bytes are fine: 0xA. A-F can be lower-case or capital letters. |
| 0-255   | Write this decimal value. Any number not preceded by 0x or 0b is interpreted as a decimal value. |
| ```space```| Value delimiter. Use a space to separate numbers. No delimiter is required between non-number values: \{0xa6 0 0 16 5 0b111 0xaF rrrr}. |

{{% readfile "/_common/other-commands.md" %}}

### ```bridge``` USB to serial bridge

{{< termfile source="static/snippets/cmdref-mode-uart-bridge.html" >}}

{{< term >}}
<span style="color:#96cb59">UART></span> bridge
<span style="color:#d7af00">UART bridge. Press Bus Pirate button to exit.</span>
$GPGSV,1,1,00*79
$BDGSV,1,1,00*68
$GNRMC,,V,,,,,,,,,,M*4E
$GNVTG,,,,,,,,,M*2D
$GNZDA,,,,,,*56
$GPTXT,01,01,01,ANTENNA OK*35
{{</term>}}

Transparent UART ```bridge```. Acts as a USB to serial converter between the UART on the IO pins and the USB serial port used by the Bus Pirate terminal. 
- Use directly with devices that have a terminal interface (example: routers)
- *Exit your terminal program* to use the port with a script or software (example: programming a chip, GPS software)

Press the Bus Pirate button to exit.

{{% alert context="warning" %}}
The UART bridge is between the Bus Pirate UART pins and the USB serial port used by the Bus Pirate terminal. To use the UART brige with a script or software, *exit your terminal program* first and then use the same port with your application. 
{{% /alert %}}

{{% alert context="info" %}}
Use ```bridge -h``` to see the latest options and features.
{{% /alert %}}

### ```gps``` Decoding GPS NMEA sentences

{{< termfile source="static/snippets/cmdref-mode-uart-gps.html" >}}

Most GPS modules output [NMEA sentences](https://gpsd.gitlab.io/gpsd/NMEA.html) through a serial UART. The ```gps``` command decodes common sentences using [minmea](https://github.com/kosma/minmea). The raw data and decoded data are printed in the terminal. Press any key to exit.

{{% alert context="info" %}}
Use ```gps -h``` to see the latest options and features.
{{% /alert %}}

### ```glitch``` Glitch hacking framework

{{< termfile source="static/snippets/cmdref-mode-uart-glitch.html" >}}

A [glitch hacking]({{< relref "/docs/devices/uart-glitch-command/">}}) framework.

### MIDI

[MIDI](http://en.wikipedia.org/wiki/Musical_Instrument_Digital_Interface)
is a command set used by electronic (music) instruments. It travels over
a standard serial UART configured for 31250bps/8/n/1.

MIDI is a ring network, each node has an input and output socket. Each
node passes messages to the next in the ring. The input and outputs are
opto-isolated. The signaling is at 5volts, 5ma (current-based
signaling). An adapter is required: [example
1](https://www.compuphase.com/electronics/midi_rs232.htm), [example
2](https://midi.org/specs).

### Device demos
- [NMEA GPS module]({{% relref "/docs/devices/nmea-gps/" %}})

## HDUART

-   **Bus:** Half-duplex [UART](http://en.wikipedia.org/wiki/Serial_uart),
    [MIDI](http://en.wikipedia.org/wiki/Musical_Instrument_Digital_Interface)
    (universal asynchronous receiver transmitter), RX and TX on the same wire
-   **Connections:** one data pin (RXTX) and ground
-   **Output type:** open collector/open drain
-   **Pull-up resistors:** always required (2K - 10K ohms)
-   **Maximum Voltage:** 5volts

{{% alert context="info" %}}
Half-duplex UART is a common serial UART, but receive and transmit share a single data line. This is used to interface [mobile phone SIM cards and bank IC cards]({{% relref "/docs/devices/sim-bank-ic-cards/" %}}), among other devices.
{{% /alert %}}


### Connections
| Bus Pirate | Direction                     | Circuit | Description   |
|------------|--------------------------|---------|---------------|
| RXTX       | <font size="+2">←→</font> | RXTX    | Bus Pirate Transmit and Receive   |
| GND        | <font size="+2">⏚</font> | GND     | Signal Ground |

### Configuration options

{{< termfile source="static/snippets/cmdref-mode-hduart-config.html" >}}

### Pull-up resistors

Half-duplex UART is an open-collector bus, it requires pull-up resistors to hold the data line high to create the data '1'. The Bus Pirate doesn't output high, it only pulls low. Without pull-up resistors there can never be a '1'. 

Enable the Bus Pirate onboard pull-up resistors with the [```P``` command]({{% relref "/docs/command-reference/#pp-pull-up-resistors" %}}).

{{% alert context="info" %}}
- Half-duplex UART requires pull-up resistors to hold the data line high.
- Without pull-up resistors there can never be a '1'. 
- Enable the Bus Pirate onboard pull-up resistors with the [```P``` command]({{% relref "/docs/command-reference/#pp-pull-up-resistors" %}}).
{{% /alert %}}

### Bus commands

|Command| Description  |
|---------|-------|
| [      | Open UART, display data as it arrives asynchronously. |
| ]      | Close UART.  |
| {       | RST pin (IO2) high |
|  } | RST pin (IO2) low  |
| r       | Check UART for byte, or fail if empty. (r:1…255 for bulk reads) |
| 0b      | Write this binary value. Format is 0b00000000 for a byte, but partial bytes are also fine: 0b1001.|
| 0x      | Write this HEX value. Format is 0x01. Partial bytes are fine: 0xA. A-F can be lower-case or capital letters. |
| 0-255   | Write this decimal value. Any number not preceded by 0x or 0b is interpreted as a decimal value. |
| ```space```| Value delimiter. Use a space to separate numbers. No delimiter is required between non-number values: \{0xa6 0 0 16 5 0b111 0xaF rrrr}. |


{{% readfile "/_common/other-commands.md" %}}

### ```bridge``` USB to serial bridge

{{< termfile source="static/snippets/cmdref-mode-hduart-bridge.html" >}}
 
Transparent UART ```bridge```. Bidirectional UART pass-through to interact with other serial devices from inside the Bus Pirate terminal. Press the Bus Pirate button to exit. Useful for reading SIM cards with [pySim](https://github.com/simula/pysim).

{{% alert context="info" %}}
Use ```bridge -h``` to see the latest options and features.
{{% /alert %}}

### Device demos
- [Mobile SIMs & Bank IC Cards]({{% relref "/docs/devices/sim-bank-ic-cards/" %}})

## I2C
-   **Bus:** [I2C](http://en.wikipedia.org/wiki/I2c) (eye-squared-see or
    eye-two-see)
-   **Connections:** two data pins (SDA/SCL) and ground
-   **Output type:** open drain/open collector
-   **Pull-up resistors:** always required (2K - 10K ohms)
-   **Maximum voltage:** 1.2 to 5 volts
-  **Common speed:** 100kHz, 400kHz, 1MHz

### I2C Protocol Overview

![](/images/docs/fw/i2c-pulseview.png)

**I2C (Inter-Integrated Circuit)** is a 2-wire protocol used for communication between devices. It uses two lines: **SDA** (data) and **SCL** (clock). The protocol supports multiple devices on the same bus, with each device identified by a unique 7-bit address.

#### **Start and Stop Conditions**
   - ```S``` - Each transaction begins with a **start condition** by pulling SDA low while SCL remains high.
   - ```P``` - Each transaction ends with a **stop condition** by releasing SDA high while SCL remains high.
   - ```Sr``` - A **repeat start condition** starts a new transaction with the same device, without sending a stop condition. It can be replaced with a stop condition followed by a start condition, but the repeat start is more efficient.

#### **Byte Transmission**
   - Data is transmitted 8 bits at a time, starting with the most significant bit (MSB).
   - ```A```/```N``` - After each byte there is a 9th **ACK**/**NACK** bit. The receiver sends an **ACK** (acknowledge) by pulling SDA low or a **NACK** (not acknowledge) by leaving SDA high. NACK is typically used to tell a chip that we are done reading data from it. 

#### **Addressing**
   - The first byte sent after a start condition contains the 7-bit device address and a **read/write bit**. In the logic analyzer trace the 7-bit address is 0b1010000 (0x50).
     - ```W``` - `0` for write operations (0b1010000`0` = 0xA0).
     - ```R``` - `1` for read operations (0b1010000`1` = 0xA1).

#### **Bus Pirate I2C syntax**

{{< termfile source="static/snippets/cmdref-i2c-example.html" >}}

{{% alert context="info" %}}
```[0xA0 0x00 [0xA1 r]``` is the Bus Pirate syntax for the I2C example above.
{{% /alert %}}

- ```[``` - I2C start condition
- ```0xA0``` - Write the device address `0xA0`, which is the 7-bit address `0x50` with the write/read bit cleared (0).
- ```0x00``` - Write the command `0x00`, which is often used to select a register or address.
- ```[``` - I2C repeat start condition.
- ```0xA1``` - Write the device address `0xA1`, which is the 7-bit address `0x50` with the write/read bit set (1).
- ```r``` - Read one byte from SDA, which will be the data from the device.
- ```]``` - I2C stop condition.


### Configuration options

{{< termfile source="static/snippets/cmdref-mode-i2c-config.html" >}}

### Pull-up resistors

I2C is an open-collector bus, it requires pull-up resistors to hold the
clock and data lines high and create the data '1'. I2C parts don't
output high, they only pull low, without pull-up resistors there can
never be a '1'. This will cause common errors such as the I2C address
scanner reporting a response at every address. 

Enable the Bus Pirate onboard pull-up resistors with the [```P``` command]({{% relref "/docs/command-reference/#pp-pull-up-resistors" %}}).

{{% alert context="info" %}}
- I2C requires pull-up resistors to hold the clock and data lines high.
- I2C parts don't output high, they only pull low.
- Without pull-up resistors there can never be a '1'. 
- Enable the Bus Pirate onboard pull-up resistors with the [```P``` command]({{% relref "/docs/command-reference/#pp-pull-up-resistors" %}}).
{{% /alert %}}

### Connections

| Bus Pirate | Direction                     | Circuit | Description   |
|------------|--------------------------|---------|---------------|
| SDA       | <font size="+2">↔</font> | SDA     | Serial Data   |
| SCL        | <font size="+2">→</font> | SCL     | Serial Clock  |
| GND        | <font size="+2">⏚</font> | GND     | Signal Ground |

### Bus commands

|Command|Description|
|-------|-----------|
| \{ or [ | Issue (repeated) I2C start condition. |
| ] or } | Issue I2C stop condition. |
| r       | Read one byte, send ACK. (r:1…255 for bulk reads)|
| 0b      | Write this binary value, check ACK. Format is 0b00000000 for a byte, but partial bytes are also fine: 0b1001.|
| 0x      | Write this HEX value, check ACK. Format is 0x01. Partial bytes are fine: 0xA. A-F can be lower-case or capital letters. |
| 0-255   | Write this decimal value, check ACK. Any number not preceded by 0x or 0b is interpreted as a decimal value. |
| ```space```| Value delimiter. Use a space to separate numbers. No delimiter is required between non-number values: \{0xa6 0 0 16 5 0b111 0xaF rrrr}. |

{{% readfile "/_common/other-commands.md" %}}

### ```scan``` I2C address search

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">I2C></span> scan
I2C address search:
0x50 (0xA0 W) (0xA1 R)
0x51 (0xA2 W) (0xA3 R)
0x52 (0xA4 W) (0xA5 R)
0x53 (0xA6 W) (0xA7 R)
0x54 (0xA8 W) (0xA9 R)
0x55 (0xAA W) (0xAB R)
0x56 (0xAC W) (0xAD R)
0x57 (0xAE W) (0xAF R)

Found 16 addresses, 8 W/R pairs.

<span style="color:#96cb59">I2C></span> 
{{< /term >}}

The ```scan``` command searches for I2C device addresses.

You can find the [I2C](http://en.wikipedia.org/wiki/I%C2%B2C) address
for most I2C-compatible chips in the datasheet. But what if you're
working with an unknown chip, a dated chip with no datasheet or you're
just too lazy to look it up?

{{< termfile source="static/snippets/cmdref-mode-i2c-scan-help.html" >}}

The Bus Pirate has a built-in address scanner that checks every possible I2C address for a
response. This brute force method is a fast and easy way to see if any
chips are responding, and to uncover undocumented access addresses.

I2C chips respond to a 7bit address, so up to 128 devices can share the
same two communication wires. An additional bit of the address
determines if the operation is a write to the chip (0), or a read from
the chip (1).

#### Scanner details

The ```scan``` command in I2C mode runs the address scanner.

-   For I2C write addresses: the BP sends a start, the write address,
    looks for an ACK, then sends a stop.
-   For I2C read addresses: the BP sends a start, the read address,
    looks for an ACK. If there is an ACK, it reads a byte and NACKs it.
    Finally it sends a stop.

When the I2C chip responds to the read address, it outputs data and will
miss a stop condition sent immediately after the read address (bus
contention). If the I2C chip misses the stop condition, the address
scanner will see ghost addresses until the read ends randomly. By
reading a byte after any read address that ACKs, we have a chance to
NACK the read and properly end the I2C transaction.

### ```sniff``` I2C bus sniffer

{{< termfile source="static/snippets/cmdref-mode-i2c-sniff-help.html" >}}

Sniff I2C packets up to 500kHz.

### ```i2c``` Generic dump register command

{{< termfile source="static/snippets/i2cdump.html" >}}

Many I2C devices follow the same pattern to read the contents of the chip registers or memory. Send the device write address followed by a register address to begin reading from. Then send the device read address and read data, the register address increments as each byte is read.

The ```i2c``` command implements this common pattern to dump I2C device contents to the terminal or read them to a file.

{{% alert context="info" %}}
The address register width generally depends on the device size. Small devices (256 bytes or less) often use a 1-byte address register. Larger devices (EEPROMs, sensors, etc) often use a 2-byte address register. Some devices use 3 or 4 byte address registers. Check the device datasheet for details.
{{% /alert %}}

|Option|Description|
|-|-|
|dump|Dump I2C device contents to terminal. Space to continue, x to exit|
|read|Read I2C device contents to file|

Options tell the i2c command what to do.

|Flag|Description|
|-|-|
|-a <device>|Specify the 7-bit I2C device address, e.g. 0x50|
|-w <width>|Specify the address register width in bytes (1-4, default 1)|
|-r <start>|Specify the starting register address (default 0x00)|   
|-f <file>|Specify the file for read|
|-b <bytes>|Dump: specify the number of bytes to read|
|-q|Dump: quiet mode, no address or ASCII columns. Useful for copying HEX values to a HEX editor.|
|-c|Dump: disable paging, display all data in one go.|
|-h|Show help for the i2c command|

Flags pass file names and other settings.


### ```eeprom``` Read, write, erase, verify, test, dump I2C EEPROMs
{{< asciicast src="/screencast/i2c-eeprom-command-cast.json" poster="npt:0:58"  idleTimeLimit=2 >}}
<br/>

```eeprom``` is a command to read, write, erase, verify, test and dump common 24x I2C EEPROMs. 

{{% alert context="info" %}}
You do need to specify the device type, there is no non-destructive autodetect method for I2C EEPROMs.
{{% /alert %}}

#### I2C EEPROM list supported devices

{{< term  >}}
<span style="color:rgb(150,203,89)">I2C></span>&nbsp;eeprom&nbsp;list
{{< /term>}}

- ```eeprom list``` - list all EEPROM devices supported by the ```eeprom``` command

{{% alert context="info" %}}
See [Indentifying I2C EEPROM Chips]({{< relref "/docs/devices/identify-serial-memory-chips/#identifying-i2c-eeprom-chips">}}) for more information on chip markings, power requirements, and other details.
{{% /alert %}}

|Device|Size|Size (bytes)|Page Size|Address Bytes|Block Select Bits|Block Select Bit Offset|
|---|---|---|---|---|---|---|
|[24x01](https://ww1.microchip.com/downloads/en/devicedoc/21711j.pdf)|1 Kbit|128|8|1|0||
|[24x02](https://ww1.microchip.com/downloads/en/devicedoc/21709c.pdf)|2 Kbit|256|8|1|0||
|[24x04](https://ww1.microchip.com/downloads/en/DeviceDoc/21708K.pdf)|4 Kbit|512|16|1|1|0|
|[24x08](https://ww1.microchip.com/downloads/en/devicedoc/21710k.pdf)|8 Kbit|1024|16|1|2|0|
|[24x16](https://ww1.microchip.com/downloads/en/DeviceDoc/20002213B.pdf)|16 Kbit|2048|16|1|3|0|
|[24x32](https://ww1.microchip.com/downloads/en/DeviceDoc/21072G.pdf)|32 Kbit|4096|32|2|0||
|[24x64](https://ww1.microchip.com/downloads/aemDocuments/documents/MPD/ProductDocuments/DataSheets/24AA64-24FC64-24LC64-64-Kbit-I2C-Serial-EEPROM-DS20001189.pdf)|64Kbit|8192|32|2|0||
|[24x128](https://ww1.microchip.com/downloads/aemDocuments/documents/MPD/ProductDocuments/DataSheets/24AA128-24LC128-24FC128-128-Kbit-I2C-Serial-EEPROM-DS20001191.pdf)|128 Kbit|16384|64|2|0||
|[24x256](https://ww1.microchip.com/downloads/aemDocuments/documents/MPD/ProductDocuments/DataSheets/24AA256-24LC256-24FC256-256K-I2C-Serial-EEPROM-DS20001203.pdf)|256 Kbit|32768|64|2|0||
|[24x512](https://ww1.microchip.com/downloads/aemDocuments/documents/MPD/ProductDocuments/DataSheets/24AA512-24LC512-24FC512-512-Kbit-I2C-Serial-EEPROM-DS20001754.pdf)|512 Kbit|65536|128|2|0||
|[24x102*5*](https://ww1.microchip.com/downloads/en/devicedoc/21941b.pdf)|1 Mbit|131072|128|2|1|3|
|[24x1026](https://ww1.microchip.com/downloads/aemDocuments/documents/MPD/ProductDocuments/DataSheets/24AA1026-24FC1026-24LC1026-1024-Kbit-I2C-Serial-EEPROM-DS20002270.pdf)|1 Mbit|131072|128|2|1|0|   
|[24xM01](https://ww1.microchip.com/downloads/en/DeviceDoc/AT24CM01-I2C-Compatible-Two-Wire-Serial-EEPROM-Data-Sheet-20006170A.pdf)|1 Mbit|131072|256|2|1|0|
|[24xM02](https://ww1.microchip.com/downloads/aemDocuments/documents/MPD/ProductDocuments/DataSheets/AT24CM02-2-Mbit-I2C-Serial-EEPROM-DS20006197.pdf)|2 Mbit|262144|256|2|2|0|

{{% alert context="info" %}}
24x chips have a variety of part numbers, but tend to operate in the same way. Often a manufacturer specific part number indicates a different voltage range or upgraded features. AT24C, 24C, 24LC, 24AA, 24FC are all generally part of same basic 24x family of chips. 
{{% /alert %}}  

{{% alert context="danger" %}}
The default I2C address for most 24x chips is 0x50, but many have pins for setting a different address. The ```eeprom``` command uses 0x50 by default, but you can specify a different I2C address with the ```-a``` flag.
{{% /alert %}}

##### Chip voltage requirements

|24xx Family|Minimum Voltage|Maximum Voltage|Notes|
|---|---|---|---|
|AT24C|2.7V|5.5V|400kHz max|
|24C|2.7V|5.5V|400kHz max|
|24LC|2.5V|5.5V|400kHz max|
|24AA|1.7V|5.5V|400kHz max|
|24FC|1.8V|5.5V|1MHz max|

<br/>

Before using the ```eeprom``` command, you'll need to enable a power supply with the [```W``` command]({{< relref "/docs/command-reference/#ww-power-supply-offon">}}) and pull-up resistors with the [```P``` command]({{< relref "/docs/command-reference/#pp-pull-up-resistors">}}).

{{% alert context="danger" %}}
**Most EEPROMs should be fine with a 3.3 volt power supply, but if possible check the datasheet to be sure!**
{{% /alert %}}

#### I2C EEPROM dump to terminal

{{< termfile source="static/snippets/i2c-eeprom-command-dump-partial.html" >}}

Display the contents of an I2C EEPROM in the terminal. 
- ```eeprom dump -d <device>``` - display EEPROM contents
- ```eeprom dump -d <device> -s <start>``` - display EEPROM contents, starting at address `<start>`
- ```eeprom dump -d <device> -s <start> -b <bytes>``` - display a specific range of bytes, starting at address `<start>` and reading `<bytes>` bytes

#### I2C EEPROM read to file
{{< term  >}}
<span style="color:rgb(150,203,89)">I2C></span>&nbsp;eeprom&nbsp;read&nbsp;-d&nbsp;24x02&nbsp;-f&nbsp;eeprom.bin&nbsp;-v
24X02:&nbsp;256&nbsp;bytes,&nbsp;&nbsp;0&nbsp;block&nbsp;select&nbsp;bits,&nbsp;1&nbsp;byte&nbsp;address,&nbsp;8&nbsp;byte&nbsp;pages

Read:&nbsp;Reading&nbsp;EEPROM&nbsp;to&nbsp;file&nbsp;eeprom.bin...
Progress:&nbsp;[###########################]&nbsp;100.00%
Read&nbsp;complete
Read&nbsp;verify...
Progress:&nbsp;[###########################]&nbsp;100.00%
Read&nbsp;verify&nbsp;complete
Success&nbsp;:)

<span style="color:rgb(150,203,89)">I2C></span>&nbsp;
{{< /term>}}

Read the contents of an I2C EEPROM and save it to a file.
- ```eeprom read -d <device> -f <file>``` - read EEPROM contents to file `<file>`
- ```eeprom read -d <device> -f <file> -v``` - read EEPROM contents to file `<file>`, verify the read operation

#### I2C EEPROM write from file
{{< term  >}}
<span style="color:rgb(150,203,89)">I2C></span>&nbsp;eeprom&nbsp;write&nbsp;-d&nbsp;24x02&nbsp;-f&nbsp;eeprom.bin&nbsp;-v
24X02:&nbsp;256&nbsp;bytes,&nbsp;&nbsp;0&nbsp;block&nbsp;select&nbsp;bits,&nbsp;1&nbsp;byte&nbsp;address,&nbsp;8&nbsp;byte&nbsp;pages

Write:&nbsp;Writing&nbsp;EEPROM&nbsp;from&nbsp;file&nbsp;eeprom.bin...
Progress:&nbsp;[###########################]&nbsp;100.00%
Write&nbsp;complete
Write&nbsp;verify...
Progress:&nbsp;[###########################]&nbsp;100.00%
Write&nbsp;verify&nbsp;complete
Success&nbsp;:)
<span style="color:rgb(150,203,89)">I2C></span>&nbsp;
{{< /term>}}
Write the contents of a file to an I2C EEPROM.
- ```eeprom write -d <device> -f <file>``` - write EEPROM from file `<file>`
- ```eeprom write -d <device> -f <file> -v``` - write EEPROM from file `<file>`, verify the write operation

{{% alert context="danger" %}}
If the **file is bigger than the EEPROM**, only the first bytes of the file will be written to the EEPROM. The rest of the file will be ignored.

If the **file is smaller than the EEPROM**, the full file will be written to the EEPROM, and the rest of the EEPROM will be left unchanged. The eeprom command will read the target page from the EEPROM, write the new data to the page, and then write the full page back to the EEPROM. This is done to avoid writing partial pages, which some devices cannot handle.
{{% /alert %}}

#### I2C EEPROM verify against file
{{< term  >}}
<span style="color:rgb(150,203,89)">I2C></span>&nbsp;eeprom&nbsp;verify&nbsp;-d&nbsp;24x02&nbsp;-f&nbsp;eeprom.bin
24X02:&nbsp;256&nbsp;bytes,&nbsp;&nbsp;0&nbsp;block&nbsp;select&nbsp;bits,&nbsp;1&nbsp;byte&nbsp;address,&nbsp;8&nbsp;byte&nbsp;pages

Verify:&nbsp;Verifying&nbsp;EEPROM&nbsp;contents&nbsp;against&nbsp;file&nbsp;eeprom.bin...
Progress:&nbsp;[###########################]&nbsp;100.00%
Verify&nbsp;complete
Success&nbsp;:)
<span style="color:rgb(150,203,89)">I2C></span>&nbsp;
{{< /term>}}
Verify the contents of an I2C EEPROM match a file.
- ```eeprom verify -d <device> -f <file>``` - verify EEPROM contents against file `<file>`

{{% alert context="danger" %}}
If the **file is bigger than the EEPROM**, only the first bytes of the file will be verified against the EEPROM. The rest of the file will be ignored.

If the **file is smaller than the EEPROM**, the full file will be verified against the EEPROM, and the rest of the EEPROM will be ignored.
{{% /alert %}}

#### I2C EEPROM erase
{{< term  >}}
<span style="color:rgb(150,203,89)">I2C></span>&nbsp;eeprom&nbsp;erase&nbsp;-d&nbsp;24x02&nbsp;-v
24X02:&nbsp;256&nbsp;bytes,&nbsp;&nbsp;0&nbsp;block&nbsp;select&nbsp;bits,&nbsp;1&nbsp;byte&nbsp;address,&nbsp;8&nbsp;byte&nbsp;pages

Erase: Writing 0xFF to all bytes...
Progress:&nbsp;[###########################]&nbsp;100.00%
Erase&nbsp;complete
Erase&nbsp;verify...
Progress:&nbsp;[###########################]&nbsp;100.00%
Erase&nbsp;verify&nbsp;complete
Success&nbsp;:)
<span style="color:rgb(150,203,89)">I2C></span>&nbsp;
{{< /term>}}

Erase the contents of an I2C EEPROM, writing 0xFF to all bytes.
- ```eeprom erase -d <device>``` - erase EEPROM contents
- ```eeprom erase -d <device> -v``` - erase EEPROM contents, verify the erase operation
#### I2C EEPROM test
{{< term  >}}
<span style="color:rgb(150,203,89)">I2C></span>&nbsp;eeprom&nbsp;test&nbsp;-d&nbsp;24x02
24X02:&nbsp;256&nbsp;bytes,&nbsp;&nbsp;0&nbsp;block&nbsp;select&nbsp;bits,&nbsp;1&nbsp;byte&nbsp;address,&nbsp;8&nbsp;byte&nbsp;pages

Erase:&nbsp;Writing&nbsp;0xFF&nbsp;to&nbsp;all&nbsp;bytes...
Progress:&nbsp;[###########################]&nbsp;100.00%
Erase&nbsp;complete
Erase&nbsp;verify...
Progress:&nbsp;[###########################]&nbsp;100.00%
Erase&nbsp;verify&nbsp;complete

Test:&nbsp;Writing&nbsp;alternating&nbsp;patterns
Writing&nbsp;0xAA&nbsp;0x55...
Progress:&nbsp;[###########################]&nbsp;100.00%
Write&nbsp;complete
Write&nbsp;verify...
Progress:&nbsp;[###########################]&nbsp;100.00%
Write&nbsp;verify&nbsp;complete
Writing&nbsp;0x55&nbsp;0xAA...
Progress:&nbsp;[###########################]&nbsp;100.00%
Write&nbsp;complete
Write&nbsp;verify...
Progress:&nbsp;[###########################]&nbsp;100.00%
Write&nbsp;verify&nbsp;complete
Success&nbsp;:)

<span style="color:rgb(150,203,89)">I2C></span>&nbsp;
{{< /term>}}
Test I2C EEPROM functionality. Erase the EEPROM to 0xff and verify the erase. Then write alternating patterns of 0xAA and 0x55, verifying each write operation. Any stuck bits should be detected during the test.
- ```eeprom test -d <device>``` - test EEPROM functionality

#### I2C EEPROM options and flags

{{< termfile source="static/snippets/i2c-eeprom-command-help.html" >}}

|Option|Description|
|---|---|
|```eeprom list```|List all supported EEPROM devices|
|```eeprom dump```|Dump EEPROM contents to terminal. Space to continue, x to exit.|
|```eeprom read```|Read EEPROM contents to file|
|```eeprom write```|Write EEPROM from file|
|```eeprom verify```|Verify EEPROM contents against file|
|```eeprom erase```|Erase EEPROM contents, writing 0xFF to all bytes|
|```eeprom test```|Test EEPROM functionality, erase and write alternating patterns|

Options tell the ```eeprom``` command what to do.

|Flag|Description|
|---|---|
|```-d <device>```|Specify the EEPROM device type, e.g. 24x02|
|```-f <file>```|Specify the file for read, write and verify|
|```-v```|Verify the read or write operation|
|```-a```|Specify an alternate I2C address (0x50 default)|
|```-s <start>```|Specify the start address for dump operations|
|```-b <bytes>```|Specify the number of bytes to read for dump operations|
|```-q```|Dump quiet mode, no address or ASCII columns. Useful for copying HEX values to a HEX editor.|
|```-c```|Dump: disable paging, display all data in one go.|
|```-h```|Show help for the ```eeprom``` command|

Flags pass file names and other settings.

### ```ddr5``` Probe, read, write, unlock DDR5 SDRAM modules

{{< asciicast src="/screencast/ddr5-command-cast.json" poster="npt:0:22"  idleTimeLimit=2 >}}
<br/>
The ```ddr5``` command can probe, read, write, and unlock the SPD hub chip in [DDR5 SDRAM computer memory modules]({{< relref "/docs/devices/ddr5">}}) (UDIMM, SODIMM). 
- Unlock SPD chips, backup SPD data and restore corrupted SPD tables. 
- Search for, and replicate, hidden entries unscrupulous manufacturers use to lock equipment to proprietary RAM modules.

DDR5 SPD dumps can be edited with a HEX editor or a dedicated SPD editor GUI like [DDR5SPDEditor](https://github.com/edlf/DDR5SPDEditor).

{{% alert context="info" %}}
The [DDR5 SPD I2C adapter plank]({{< relref "/docs/overview/ddr-ram-i2c-adapter/" >}}) has everything you need to play with DDR5 without soldering. The plank provides the correct voltage levels and pinouts to interface with a DDR5 SPD chip in offline mode.
{{% /alert %}}

#### DDR5 probe

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:rgb(150,203,89)">I2C></span>&nbsp;ddr5&nbsp;probe
Device&nbsp;Type:&nbsp;0x5118
Device&nbsp;Revision:&nbsp;1.4
Vendor&nbsp;ID:&nbsp;0x8632&nbsp;(Montage&nbsp;Technology&nbsp;Group)
Write&nbsp;Protection&nbsp;for&nbsp;NVM&nbsp;Blocks:&nbsp;0x3FFF
...
SPD&nbsp;EEPROM&nbsp;JEDEC&nbsp;Manufacturing&nbsp;Information&nbsp;blocks&nbsp;8-9:
&nbsp;&nbsp;Module&nbsp;Manuf.&nbsp;Code:&nbsp;0x859B&nbsp;(Crucial&nbsp;Technology)
&nbsp;&nbsp;Module&nbsp;Manuf.&nbsp;Location:&nbsp;0x00
&nbsp;&nbsp;Module&nbsp;Manuf.&nbsp;Date:&nbsp;22Y/04W
&nbsp;&nbsp;Module&nbsp;Serial&nbsp;Number:&nbsp;0xE6FFB785
&nbsp;&nbsp;Module&nbsp;Part&nbsp;Number:&nbsp;CT8G48C40U5.M4A1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
....
{{< /term >}}

```ddr5 probe``` identifies the DDR5 SPD chip and displays its type, revision, vendor ID, and write protection status. It also reads the JEDEC manufacturing information blocks to display stored information about the memory configure and manufacturer. 

The probe command also searches the Manufacture Specific Data block and End User Programmable blocks for hidden information. This will discover EXPO (AMD) and XMP (Intel) overclock profiles, as well as hidden information that unscrupulous manufacturers use to lock equipment to proprietary RAM modules.

#### DDR5 dump
{{< termfile source="static/snippets/ddr5-command-dump-partial.html" >}}

The ```ddr5 dump``` command displays the contents of a DDR5 SPD chip EEPROM/non-volatile memory in the terminal. It reads the chip and prints the contents of each 64-byte block.
- ```ddr5 dump``` - display the contents of the DDR5 SPD chip in the terminal
- ```ddr5 dump -s <start>``` - display the contents of the DDR5 SPD chip, starting at address `<start>`
- ```ddr5 dump -s <start> -b <bytes>``` - display a specific range of bytes, starting at address `<start>` and reading `<bytes>` bytes

#### DDR5 read to file

{{< termfile source="static/snippets/ddr5-command-read.html" >}}

Read the contents of a DDR5 SPD chip and save to a file with the ```ddr5 read``` command. The file name is specified with the ```-f``` flag.
- ```ddr5 read -f <file>``` - read the contents of the DDR5 SPD chip to file `<file>`

#### DDR5 verify against file

{{< termfile source="static/snippets/ddr5-command-verify.html" >}}

Verify the contents of a DDR5 SPD chip against a file with the ```ddr5 verify``` command. The file name is specified with the ```-f``` flag. This command reads the chip and compares it to the file, reporting the location of any differences.

- ```ddr5 verify -f <file>``` - verify the contents of the DDR5 SPD chip against the file `<file>`

#### DDR5 write from file

{{< termfile source="static/snippets/ddr5-command-write.html" >}}

Write a file to a DDR5 SPD chip with the ```ddr5 write``` command. The file name is specified with the ```-f``` flag. 
- ```ddr5 write -f <file>``` - write the contents of `<file>` to the DDR5 SPD chip

{{% alert context="info" %}}
During write the command will unlock the block protection bits. When the write is complete, the write protection bits will be restored to the original state.  
{{% /alert %}} 

{{% alert context="danger" %}}
The ```ddr5 write``` command will overwrite the contents of the DDR5 SPD chip. Use with caution, as it can corrupt the SPD data and render the RAM module unusable. Always make a backup with the ```ddr5 read``` command before writing to the chip.
{{% /alert %}}

#### DDR5 lock/unlock block

{{< termfile source="static/snippets/ddr5-command-lock.html" >}}

Lock or unlock a block in the DDR5 SPD chip with the ```ddr5 lock``` and ```ddr5 unlock``` commands. The block number is specified with the ```-b``` flag (0-15). Each block is 64 bytes in size.
- ```ddr5 lock -b <block>``` - lock the specified block in the DDR5 SPD chip
- ```ddr5 unlock -b <block>``` - unlock the specified block in the DDR5 SPD chip

{{% alert context="info" %}}
In order to unlock blocks the module's HSA pin **must** be connected to ground. This is required to unlock the block protection bits in the DDR5 SPD chip. See the [DDR5 SPD demo]({{% relref "/docs/devices/ddr5/#connections" %}}) for more details.
{{% /alert %}}

#### DDR5 crc check
{{< termfile source="static/snippets/ddr5-command-crc.html" >}}

Calculate or verify the CRC of the JEDEC blocks 0-7 in a DDR5 SPD dump file with the ```ddr5 crc``` command. The file name is specified with the ```-f``` flag. This command reads the specified file and calculates the CRC for the first 8 blocks, reporting any discrepancies.
- ```ddr5 crc -f <file>``` - calculate CRC for the first 8 blocks of the DDR5 SPD chip dump file `<file>`

{{% alert context="info" %}}
To verify the CRC on a DDR5 SPD chip instead of a file, use the ```ddr5 probe``` command. It will automatically calculate and verify the CRC for the first 8 blocks of the SPD chip.
{{% /alert %}}

#### DDR5 crc patch

{{< term >}}
<span style="color:rgb(150,203,89)">I2C></span>&nbsp;ddr5 patch -f ddr5.bin
Checking CRC for JEDEC blocks 0-7, file: ddr5.bin
Stored CRC (bytes 510:511): 0x37 0x00
Calculated CRC: 0x37 0x3E
Patching CRC in file to: 0x37 0x3E
File patched successfully :)
Verifying patched file CRC:
CRC verify
Stored CRC (bytes 510:511): 0x37 0x3E
Calculated CRC: 0x37 0x3E
CRC okay :)
{{< /term >}}

To update the CRC of a DDR5 SPD dump file, say after making modifications in a HEX editor, use the ```ddr5 patch``` command. This command reads the specified file, calculates the correct CRC for the first 8 blocks, and updates the stored CRC in the file. The file name is specified with the ```-f``` flag.
- ```ddr5 patch -f <file>``` - update the CRC for the first 8 blocks of the DDR5 SPD chip dump file `<file>`

{{% alert context="info" %}}
The ```ddr5 patch``` command does not modify the contents of the DDR5 SPD chip, it only updates the CRC in the specified file.
{{% /alert %}}

#### DDR5 Options and flags
{{< termfile source="static/snippets/ddr5-command-help.html" >}}

{{% alert context="info" %}}
Use ```ddr5 -h``` to see the latest options and features.
{{% /alert %}}

|Option|Description|
|------|-----------|
|```ddr5 probe```|Probe DDR5 SPD chip for ID and NVM/EEPROM status.|
|```ddr5 dump```|Display DDR5 SPD NVM contents in the terminal.|
|```ddr5 read```|Read DDR5 SPD NVM to a file. Specify file with -f flag.|
|```ddr5 write```|Write file to DDR5 SPD NVM. Specify file with -f flag.|
|```ddr5 verify```|Verify DDR5 SPD NVM against file. Specify file with -f flag.|
|```ddr5 lock```|Lock DDR5 SPD NVM block (64 bytes per block). Specify block with -b flag.|
|```ddr5 unlock```|Unlock DDR5 SPD NVM block. Specify block with -b flag.|
|```ddr5 crc```|Calculate/verify CRC of JEDEC blocks 0-7 in a file. Specify file with -f flag.|
|```ddr5 patch```|Update the CRC of JEDEC blocks 0-7 in a file. Specify file with -f flag.|

Options tell the ddr5 command what to do.

|Flag|Description|
|-----|-----------|
|```-f```|File flag. Specify a file to write, read, verify, check or patch CRC|
|```-b```|Block flag. Specify a DDR5 SPD NVM block to lock or unlock (0 - 15)|
|```-s```|Start address flag. Specify the dump start address|
|```-b```|Bytes flag. Specify the number of bytes to dump|
|```-q```|Dump quiet mode, no address or ASCII columns. Useful for copying HEX values to a HEX editor.|
|```-h```|Show help for Bus Pirate commands and modes|

Flags pass file names and other settings.

### ```ddr4``` Probe, read, write, unlock DDR4 SDRAM modules

{{< asciicast src="/screencast/ddr4-command-cast.json" poster="npt:0:22"  idleTimeLimit=2 >}} 
<br/>
The ```ddr4``` command can probe, read, write, and unlock the Serial Presence Detect EEPROM in [DDR4 SDRAM computer memory modules]({{< relref "/docs/devices/ddr4">}}) (UDIMM, SODIMM). 
- Unlock SPD EEPROMs, backup SPD data and restore corrupted SPD tables. 
- Search for, and replicate, hidden entries unscrupulous manufacturers use to lock equipment to proprietary RAM modules.

DDR4 SPD dumps can be edited with a HEX editor or a dedicated SPD editor GUI like [DDR4XMPEditor](https://github.com/integralfx/DDR4XMPEditor).

{{% alert context="info" %}}
The [DDR4 SPD I2C adapter plank]({{< relref "/docs/overview/ddr-ram-i2c-adapter/" >}}) has everything you need to play with DDR4 without soldering. The plank provides the correct voltage levels and pinouts to interface with a DDR4 SPD EEPROM. 9 Volt battery required (not included).
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

```ddr4 probe``` queries the DDR4 SPD EEPROM and displays its size and write protection status. It also parses the JEDEC SPD manufacturing information blocks to display stored information about the memory configuration and manufacturer. 

#### DDR4 dump
{{< termfile source="static/snippets/ddr4-command-dump-partial.html" >}}

The ```ddr4 dump``` command displays the contents of the DDR4 SPD EEPROM in the terminal. 
- ```ddr4 dump``` - display the contents of the DDR4 SPD EEPROM in the terminal
- ```ddr4 dump -s <start>``` - display the contents of the DDR4 SPD EEPROM, starting at address `<start>`
- ```ddr4 dump -s <start> -b <bytes>``` - display a specific range of bytes, starting at address `<start>` and reading `<bytes>` bytes

#### DDR4 read to file

{{< termfile source="static/snippets/ddr4-command-read.html" >}}

Read the contents of a DDR4 SPD EEPROM and save it to a file with the ```ddr4 read``` command. The file name is specified with the ```-f``` flag.
- ```ddr4 read -f <file>``` - read the contents of the DDR4 SPD EEPROM to file `<file>`

#### DDR4 verify against file

{{< termfile source="static/snippets/ddr4-command-verify.html" >}}

Verify the contents of a DDR4 SPD EEPROM against a file with the ```ddr4 verify``` command. The file name is specified with the ```-f``` flag. 

- ```ddr4 verify -f <file>``` - verify the contents of the DDR4 SPD EEPROM against the file `<file>`

#### DDR4 lock/unlock block

{{< termfile source="static/snippets/ddr4-command-lock.html" >}}

Lock or unlock a block in the DDR4 SPD EEPROM with the ```ddr4 lock``` and ```ddr4 unlock``` commands. The block number is specified with the ```-b``` flag (0-3). Each block is 128 bytes in size.
- ```ddr4 lock -b <block>``` - lock the specified block in the DDR4 SPD EEPROM
- ```ddr4 unlock``` - unlock all blocks in the DDR4 SPD EEPROM. This all or nothing, there is no per-block unlock.

{{% alert context="info" %}}
In order to change lock status, 9 volts must be present on the SA0 EEPROM address pin when executing the command. See the [DDR4 SPD demo]({{% relref "/docs/devices/ddr4/#connections" %}}) for more details.
{{% /alert %}}

{{% alert context="warning" %}}
Changing the lock status takes time. To make it as easy as possible to apply the 9 volt programming voltage manually, the Bus Pirate uses a fixed 100ms delay when changing lock status instead of busy polling. Datasheets generally specify 4ms write times, so this should be safe for all DDR4 SPD EEPROMs.
{{% /alert %}}

#### DDR4 write from file

{{< termfile source="static/snippets/ddr4-command-write.html" >}}

Write a file to a DDR4 SPD EEPROM with the ```ddr4 write``` command. The file name is specified with the ```-f``` flag. 
- ```ddr4 write -f <file>``` - write the contents of `<file>` to the DDR4 SPD EEPROM

{{% alert context="info" %}}
You will need to manually unlock all blocks with the ```ddr4 unlock``` command before writing to the DDR4 SPD EEPROM.
{{% /alert %}}

{{% alert context="danger" %}}
The ```ddr4 write``` command will overwrite the contents of the DDR4 SPD EEPROM. Use with caution, as it can corrupt the SPD data and render the RAM module unusable. Always make a backup with the ```ddr4 read``` command before writing to the EEPROM.
{{% /alert %}}

#### DDR4 crc check
{{< termfile source="static/snippets/ddr4-command-crc.html" >}}

Calculate or verify the CRC of SPD bytes 0-125 in a file with the ```ddr4 crc``` command. The file name is specified with the ```-f``` flag. This command reads the specified file and calculates the CRC for the first 126 bytes, reporting any discrepancies.
- ```ddr4 crc -f <file>``` - calculate CRC for the first 126 bytes of the DDR4 SPD EEPROM dump file `<file>`

{{% alert context="info" %}}
To verify the CRC on a DDR4 SPD EEPROM instead of a file, use the ```ddr4 probe``` command. It will automatically calculate and verify the CRC for the SPD records in the EEPROM.
{{% /alert %}}

#### DDR4 crc patch

{{< termfile source="static/snippets/ddr4-command-patch.html" >}}

To update the CRC of a DDR4 SPD dump file, say after making modifications in a HEX editor, use the ```ddr4 patch``` command. This command reads the specified file, calculates the correct CRC for the first 126 bytes, and updates the stored CRC in the file if needed. The file name is specified with the ```-f``` flag.
- ```ddr4 patch -f <file>``` - update the CRC for the first 126 bytes of the DDR4 SPD EEPROM dump file `<file>`

{{% alert context="info" %}}
The ```ddr4 patch``` command does not modify the contents of the DDR4 SPD EEPROM, it only updates the CRC in the specified file.
{{% /alert %}}

#### DDR4 Options and flags
{{< termfile source="static/snippets/ddr4-command-help.html" >}}

{{% alert context="info" %}}
Use ```ddr4 -h``` to see the latest options and features.
{{% /alert %}}

|Option|Description|
|------|-----------|
|```ddr4 probe```|Probe DDR4 SPD EEPROM for size and lock status.|
|```ddr4 dump```|Display DDR4 SPD EEPROM contents in the terminal.|
|```ddr4 read```|Read DDR4 SPD EEPROM to a file. Specify file with -f flag.|
|```ddr4 write```|Write file to DDR4 SPD EEPROM. Specify file with -f flag.|
|```ddr4 verify```|Verify DDR4 SPD EEPROM against file. Specify file with -f flag.|
|```ddr4 lock```|Lock DDR4 SPD EEPROM block (128 bytes per block). Specify block with -b flag.|
|```ddr4 unlock```|Unlock all DDR4 EEPROM protection blocks.|
|```ddr4 crc```|Calculate/verify CRC of JEDEC blocks 0-7 in a file. Specify file with -f flag.|
|```ddr4 patch```|Update the CRC of JEDEC blocks 0-7 in a file. Specify file with -f flag.|

Options tell the ddr4 command what to do.

|Flag|Description|
|-----|-----------|
|```-f```|File flag. Specify a file to write, read, verify, check or patch CRC|
|```-b```|Block flag. Specify a DDR4 protection block to lock (0 - 3)|
|```-s```|Start address flag. Specify the dump start address|
|```-b```|Bytes flag. Specify the number of bytes to dump|
|```-q```|Dump quiet mode, no address or ASCII columns. Useful for copying HEX values to a HEX editor.|
|```-h```|Show help for Bus Pirate commands and modes|

Flags pass file names and other settings.

### ```tcs3472``` Read color sensor, show on LEDs

{{< termfile source="static/snippets/tcs3472x-command.html" >}}

Command to read color data from a [TCS3472 color sensor]({{< relref "/docs/devices/tcs3472x/#tsc3472-command">}}) and display the RGB values on the Bus Pirate LEDs.

|Flag|Description|
|-|-|
|-g|Set the gain to 1x, 4x, 16x, or 60x. Default is 16x.|
|-i|Set the number of integration cycles to 1-256. Default is 256.|

{{% alert context="info" %}}
The upper byte of red, blue and green measurements are sent to the Bus Pirate LEDs. The lower byte is disgarded. If the LEDs don't seem to be lighting, try increasing the gain to 60x with the ```-g``` flag.
{{% /alert %}}

### ```sht4x``` Read temperature and humidity

{{< termfile source="static/snippets/sht4x-command.html" >}}

Read temperature and humidity from a [SHT40/41/43/45 sensor]({{< relref "/docs/devices/sht40-sht41-sht43-sht45/">}}).

### ```sht3x``` Read temperature and humidity

{{< termfile source="static/snippets/sht3x-command.html" >}}
Read temperature and humidity from a [SHT30/31/35 sensor]({{< relref "/docs/devices/sht30-sht31-sht35/">}}).

### ```si7021``` Read temperature and humidity

{{< termfile source="static/snippets/si7021-command.html" >}}

Command to read temperature and humidity from a [SHT21/SI7021/HTU21 sensor]({{< relref "/docs/devices/si7021/">}}).

### ```ms5611``` Read temperature and pressure

{{< termfile source="static/snippets/cmdref-mode-i2c-ms5611-help.html" >}}

Command to read temperature and pressure from a MS5611 sensor.

### ```tsl2561``` Read light intensity

{{< termfile source="static/snippets/tsl2561-command.html" >}}

Command to read light intensity from a [TSL2561 sensor]({{< relref "/docs/devices/tsl2561/">}}).

### Device demos
- [24C02 Smart IC Card]({{% relref "/docs/devices/24c02/" %}})
- [TCS3472x Color Sensor]({{% relref "/docs/devices/tcs3472x/" %}})
- [DDR5 SDRAM modules]({{< relref "/docs/devices/ddr5">}})
- [AT24C256 EEPROM]({{% relref "/docs/devices/at24c256/" %}})
- [SHT3x]({{% relref "/docs/devices/sht30-sht31-sht35/" %}}) and [SHT4x]({{% relref "/docs/devices/sht40-sht41-sht43-sht45/" %}}) Temperature & Humidity Sensors
- [MB85RC256V FRAM]({{% relref "/docs/devices/mb85rc256v/" %}})
- [SI7021, HTU21, SHT21 Humidity & Temperature]({{% relref "/docs/devices/si7021/" %}})
- [TSL2561 LUX Sensor]({{% relref "/docs/devices/tsl2561/" %}})

<!--

## ACK/NACK management

These examples read and write from the RAM of a DS1307 RTC chip.
```
I2C> [0xd1 rrrr]
I2C START CONDITION
WRITE: 0xD1 GOT ACK: YES**<<<read address** 
READ: 0×07 ACK **<<<sent ACK*[ 
READ: 0x06 ACK 
READ: 0x05 ACK 
READ: 0x04 NACK **<<<last read before STOP, sent NACK** 
I2C STOP CONDITION 
I2C>
```
I2C read operations must be ACKed
or NACKed by the host (the Bus Pirate). The Bus Pirate automates this,
but you should know a few rules about how it works.

The I2C library doesn't ACK/NACK a read operation until the following
command. If the next command is a STOP (or START) the Bus Pirate sends a
NACK bit. On all other commands it sends an ACK bit. The terminal output
displays the (N)ACK status. 
```
I2C> [0xd1 r:5] 
I2C START CONDITION
WRITE: 0xD1 GOT ACK: YES 
BULK READ 0×05 BYTES: 
0×07 ACK 0×06 ACK 0×05 ACK 0×04 ACK 0×03 NACK 
I2C STOP CONDITION 
I2C> 
```
Nothing changes for write commands because the slave ACKs to the Bus Pirate during
writes. Here’s an example using the bulk read command (r:5).
```
I2C>[0xd1 r **<<<setup and read one byte** 
I2C START CONDITION 
WRITE: 0xD1 GOT ACK: YES 
READ: 0x07 *(N)ACK PENDING **<<<no ACK sent yet** 
I2C>r**<<<read another byte** 
ACK**<<<ACK for previous byte** 
READ: 0x06 *(N)ACK PENDING**<<<no ACK yet** 
I2C>] **<<<STOP command** 
NACK **<<<next command is STOP, so NACK** 
I2C STOP CONDITION 
I2C> 
```
A consequence of the
delayed ACK/NACK system is that partial transactions will leave read
operations incomplete.

Here, we setup a read operation ([0xd1) and read a byte (r). Since the
Bus Pirate has no way of knowing if the next operation will be another
read (r) or a stop condition (]), it leaves the ninth bit hanging. The
warning “*(N)ACK PENDING” alerts you to this state.

Our next command is another read (r), so the Bus Pirate ACKs the
previous read and gets another byte. Again, it leaves the (N)ACK bit
pending until the next command.

The final command is STOP (]). The Bus Pirate ends the read with a NACK
and then sends the stop condition.
-->

## SPI

-   **Bus:** [SPI](http://en.wikipedia.org/wiki/Serial_Peripheral_Interface_Bus) (serial peripheral interface)
-   **Connections:** four data pins (MOSI/MISO/CLOCK/CHIP_SELECT) and ground
-   **Output type:** push-pull (1.65-5volts)
-   **Maximum voltage:** 5volts

{{% alert context="info" %}}
SPI is a common 4 wire full duplex protocol. Separate connections for data-in and data-out allow communication to and from the controller at the same time. Multiple sub devices can share the bus, but each will need an individual Chip Select (CS) connection. Chip Select is generally active when low.
{{% /alert %}} 

{{% alert context="warning" %}}
Looking for something like SPI, but with individual control over the clock and data pins? Check out [3WIRE]({{< relref "/docs/command-reference/#3-wire">}}) and [2WIRE]({{< relref "/docs/command-reference/#2-wire">}}) mode.
{{% /alert %}}

### SPI Protocol Overview

![alt text](/images/docs/command-reference/image-4.png)

**SPI (Serial Peripheral Interface)** is a synchronous serial communication protocol commonly used for short-distance communication between a master device and one or more sub devices. SPI uses four main lines: **SCLK** (clock), **MOSI** (Master Out Sub In), **MISO** (Master In Sub Out), and **CS** (Chip Select).

#### Communication Sequence

- **CS (Chip Select)**: Communication begins when the master pulls the CS line low, selecting the sub device.
- **Master Transmission**: The master sends one or more bytes over MOSI. In this example, the master writes `0x9F`.
- **Data Response**: After receiving data, the sub device can respond by sending data back over MISO. In this sequence, the sub device responds with `0xEF`, `0x40`, and `0x14`.
- **CS High**: Communication ends when the master releases the CS line (sets it high).

#### Data Flow Example

1. **CS goes low** to select the device.
2. **Master writes** `0x9F` (command) on MOSI.
3. **Sub device responds** with `0xEF`, `0x40`, `0x41` on MISO, one bit per clock cycle.
4. **CS goes high** to end the transaction.

#### Notes

- SPI is full-duplex: data can be sent and received simultaneously.
- There is no addressing on the bus; each device is selected individually using its CS line.
- The master controls the clock and initiates all communication.

#### Bus Pirate SPI syntax

{{< termfile source="static/snippets/nor-jedecid.html" >}}

{{% alert context="info" %}}
```[0x9f r:3]``` is the Bus Pirate syntax for the SPI example above.
{{% /alert %}}

- ```[``` - CS low (active).
- ```0x9f``` - Write the command `0x9F` on MOSI.
- ```r:3``` - Read 3 bytes from MISO, which are `0xEF`, `0x40`, and `0x14`.
- ```]``` - CS high (inactive).


### Connections

| Bus Pirate | Direction                    | Circuit | Description          |
|------------|--------------------------|---------|----------------------|
| MOSI       | <font size="+2">→</font> | MOSI    | Master Out Sub In |
| MISO       | <font size="+2">←</font> | MISO    | Master In Sub Out |
| CS         | <font size="+2">→</font> | CS      | Chip Select          |
| CLK        | <font size="+2">→</font> | CLK     | Clock signal         |
| GND        | <font size="+2">⏚</font> | GND     | Signal Ground        |

### Configuration options

{{< termfile source="static/snippets/cmdref-mode-spi-config.html" >}}

### Bus commands

|Command|Description|
|-------|--------------|
| [ | Chip select (CS) active |
| \{ | Chip Select (CS) active, show the SPI read byte while writing (full duplex/write with read mode)|
| ] or } | Chip Select (CS) disable|
| r    | Read one byte by sending dummy byte (0xff). (r:1…255 for bulk reads) |
| 0b      | Write this binary value. Format is 0b00000000 for a byte, but partial bytes are also fine: 0b1001.|
| 0x      | Write this HEX value. Format is 0x01. Partial bytes are fine: 0xA. A-F can be lower-case or capital letters. |
| 0-255   | Write this decimal value. Any number not preceded by 0x or 0b is interpreted as a decimal value. |
| ```space```| Value delimiter. Use a space to separate numbers. No delimiter is required between non-number values: \{0xa6 0 0 16 5 0b111 0xaF rrrr}. |

{{% readfile "/_common/other-commands.md" %}}

### ```flash``` Read/Write/Erase common flash chips

{{< asciicast src="/screencast/nor-flash-command.json" poster="npt:1:08"  idleTimeLimit=2 >}}
<br/>
The ```flash``` command can read, write, and erase common SPI flash memory chips directly in the Bus Pirate terminal. The [Serial Flash Universal Driver](https://github.com/armink/SFUD) at the heart of the flash command attempts to identify the flash chip and select the appropriate settings. Most modern flash chips contain SFDP tables that describe the chip capabilities. If a chip doesn't have SFDP tables, the driver has a database of common chips on which to fall back. 

{{% alert context="info" %}}
See [Indentifying SPI Flash Chips]({{< relref "/docs/devices/identify-serial-memory-chips/#spi-flash-memory">}}) for more information on chip markings, power requirements, and other details.
{{% /alert %}}

{{< termfile source="static/snippets/cmdref-mode-spi-flash-help.html" >}}

#### Flash probe

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">SPI></span> flash probe
Probing:
		Device ID	Manuf ID	Type ID		Capacity ID
RESID (0xAB)	0x13
REMSID (0x90)	0x13		0xef
RDID (0x9F)			0xef		0x40		0x14

Initializing SPI flash...
Flash device manufacturer ID 0xEF, type ID 0x40, capacity ID 0x14
SFDP V1.5, 0 parameter headers
		Type		Ver.	Length	Address
Table 0		JEDEC (0x00)	1.5	64B	0x000080
JEDEC basic flash parameter table info:
MSB-LSB  3    2    1    0
[0001] 0xFF 0xF1 0x20 0xE5
...
[0009] 0x00 0x00 0xD8 0x10
4 KB Erase is supported throughout the device (instruction 0x20)
Write granularity is 64 bytes or larger
Flash status register is non-volatile
3-Byte only addressing
Capacity is 1048576 Bytes
Flash device supports 4KB block erase (instruction 0x20)
Flash device supports 32KB block erase (instruction 0x52)
Flash device supports 64KB block erase (instruction 0xD8)
Found a Winbond  flash chip (1048576 bytes)
Flash device reset success
{{< /term >}}

```flash probe``` searches the flash chip for any identifying information. The flash command tries three common methods to identify a flash chip (RESID, REMSID, RDID), then attempts to read the SFDP tables.  

{{% alert context="info" %}}
Use ```flash -h``` to see the latest options and features.
{{% /alert %}}

#### Dump a flash chip

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">SPI></span> flash dump -s 0x10 -b 32
          00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F  0123456789ABCDEF
----------------------------------------------------------|----------------|
00000010: 75 61 67 65 22 3A 20 30 2C 0A 22 74 65 72 6D 69 |uage": 0,."termi|
00000020: 6E 61 6C 5F 61 6E 73 69 5F 63 6F 6C 6F 72 22 3A |nal_ansi_color":|
{{< /term >}}

Dump the contents of a flash chip to the terminal with the ```flash dump``` command.
- ```-s <start address>``` - Optional: specify the dump start address
- ```-b <bytes>``` - Optional: specify the number of bytes to dump

One screen of data is displayed at a time. Press space to continue to the next screen, or 'x' to exit. 
{{% alert context="info" %}}
Disable paging with the ```-c``` flag to display all data in one go. Use the ```-q``` flag to disable the address and ASCII columns, which is useful for copying HEX values to a HEX editor.
{{% /alert %}}

#### Read a flash chip

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">SPI></span> flash read -f example.bin
Reading 1048576 bytes from flash to example.bin
[-------C o o o o o]
{{< /term >}}

Read the contents of a flash chip to a file with the ```flash read``` command. The file name is specified with the ```-f``` flag.

#### Write a flash chip

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">SPI></span> flash write -f example.bin -e -v
Erasing 1048576 bytes
[-----------------C]
Writing 1048576 bytes from example.bin to flash
[-----------------C]
Verifying 1048576 bytes from example.bin to flash
[-------c o o o o]
{{< /term >}}

Write a file to a flash chip with the ```flash write``` command. The file name is specified with the ```-f``` flag. Use the ```-e``` flag to erase the chip before writing, and the ```-v``` flag to verify the write.

#### Verify a flash chip

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">SPI></span> flash verify -f example.bin
Verifying 1048576 bytes from example.bin to flash
[-------c o o o o]
{{< /term >}}

Verify the contents of a flash chip against a file with the ```flash verify``` command. The file name is specified with the ```-f``` flag.

#### Test a flash chip

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">SPI></span> flash test
Erasing 1048576 bytes
[-----------------C]
Writing 1048576 bytes to flash
[-----------------C]
Verifying 1048576 bytes
[-------c o o o o]
{{< /term >}}

The ```flash test``` command erases the chip, writes dummy data, and verifies the write. This is a way to test a chip.

#### Flash Options and flags

| Option | Description |
|---------|-------------|
| ```flash probe``` | Probe flash chip for ID and SFDP info. |
|```flash dump``` | Dump flash chip contents to terminal. Space to continue, x to exit. |
| ```flash erase``` | Erase flash chip. |
| ```flash write``` | Write file to flash chip. Specify file with -f flag. Use -e flag to erase before write|
| ```flash read``` | Read flash chip to file. Specify file with -f flag|
| ```flash verify``` | Verify flash chip against file. Specify file with -f flag |
| ```flash test``` | Erase and write full chip with dummy data, verify. |

Options tell the flash command what to do.

| Flag | Description |
|------|-------------|
| ```-f``` | File flag. File to write, read or verify. |
| ```-e``` | Erase flag. Add erase before write. |
| ```-v``` | Verify flag. Add verify after write or erase. |
|```-s <start>```|Specify the start address for dump operations|
|```-b <bytes>```|Specify the number of bytes to read for dump operations|
|```-q```|Dump quiet mode, no address or ASCII columns. Useful for copying HEX values to a HEX editor.|
|```-c```|Dump: disable paging, display all data in one go.|

Flags pass file names and other settings.

### ```eeprom``` Read, write, erase, verify, test, dump SPI EEPROMs

{{< asciicast src="/screencast/spi-eeprom-command-cast.json" poster="npt:1:01"  idleTimeLimit=2 >}}
<br/>
```eeprom``` is a command to read, write, erase, verify, test and dump common SPI and Microwire EEPROMs. 

{{% alert context="info" %}}
You do need to specify the device type, there is no non-destructive autodetect method for SPI EEPROMs.
{{% /alert %}}

#### SPI EEPROM list supported devices

{{< term  >}}
<span style="color:rgb(150,203,89)">SPI></span>&nbsp;eeprom&nbsp;list
{{< /term>}}

- ```eeprom list``` - list all EEPROM devices supported by the ```eeprom``` command

{{% alert context="info" %}}
**25x** (Microchip), **AT25x** (fmr. Atmel) and **M95x** (STM) are all compatible SPI EEPROMs. There are slight feature differences, but they all use the same command set. **If you have a STM 95x EEPROM, specify the equivalent 25X device.**

**93x** are Microwire EEPROMs, which use a older variant of the SPI protocol. They are also compatible with the SPI ```eeprom``` command.

See [Indentifying SPI EEPROM Chips]({{< relref "/docs/devices/identify-serial-memory-chips/#identifying-spi-eeprom-chips">}}) and [Identifying Microwire EEPROMs]({{< relref "/docs/devices/identify-serial-memory-chips/#identifying-microwire-eeprom-chips">}}) for more information on chip markings, power requirements, and other details.
{{% /alert %}}

| Device                      | Density   | Size (bytes)| Page Size (Bytes) |Address Bytes| Block Select Bits |B.S. Offset|
|-----------------------------------|-----------|------------|------|-------------------|----------|-------|
| [25X010](https://ww1.microchip.com/downloads/aemDocuments/documents/MPD/ProductDocuments/DataSheets/25AA010A-25LC010A-1-Kbit-SPI-Bus-Serial-EEPROM-20001832J.pdf)| 1 Kbit    | 128        | 8(AT)/16              | 1  |0|
| [25X020](https://ww1.microchip.com/downloads/aemDocuments/documents/MPD/ProductDocuments/DataSheets/25AA020A-25LC020A-2-Kbit-SPI-Bus-Serial-EEPROM-20001833H.pdf)| 2 Kbit    | 256 | 8(AT)/16 | 1 |0|
| [25X040](https://ww1.microchip.com/downloads/aemDocuments/documents/MPD/ProductDocuments/DataSheets/25AA040A-25LC040A4-Kbit-SPI-Bus-Serial-EEPROM-20001827J.pdf) | 4 Kbit    | 512        | 8(AT)/16              | 1         |1|3|
| [25X080](https://ww1.microchip.com/downloads/aemDocuments/documents/MPD/ProductDocuments/DataSheets/8-Kbit-SPI-Bus-Serial-EEPROM-20002151C.pdf) | 8 Kbit    | 1024   | 16/32(AT,STM)   | 2   |0|
|[25X160](https://ww1.microchip.com/downloads/aemDocuments/documents/MPD/ProductDocuments/DataSheets/25AA160CD-25LC160CD-16-Kbit-SPI-Bus-Serial-EEPROM-20002150C.pdf)| 16 Kbit   | 2048        | 16/32(AT,STM)   | 2   |0|
|[25X320](https://ww1.microchip.com/downloads/aemDocuments/documents/MPD/ProductDocuments/DataSheets/25AA320A-25LC320A-32K-SPI-Bus-Serial-EEPROM-20001828H.pdf)| 32 Kbit   | 4096 | 32   | 2  | 0|
|[25X640](https://ww1.microchip.com/downloads/aemDocuments/documents/MPD/ProductDocuments/DataSheets/25AA640A-25LC640A-64K-SPI-Bus-Serial-EEPROM-20001830G.pdf)  | 64 Kbit   | 8192        | 32                | 2          |0|
|[25X128](https://ww1.microchip.com/downloads/aemDocuments/documents/MPD/ProductDocuments/DataSheets/25AA128-25LC128-128K-SPI-Bus-Serial-EEPROM-20001831G.pdf)           | 128 Kbit  | 16384         | 64                | 2             |0|
|[25X256](https://ww1.microchip.com/downloads/aemDocuments/documents/MPD/ProductDocuments/DataSheets/25LCXXXX-8K-256K-SPI-Serial-EEPROM-High-Temp-Family-Data-Sheet-DS20002131.pdf)| 256 Kbit  | 32768        | 64                | 2          | 0|
|[25X512](https://ww1.microchip.com/downloads/aemDocuments/documents/MPD/ProductDocuments/DataSheets/25LC512-512-Kbit-SPI-Bus-Serial-EEPROM-Data-Sheet-20002065.pdf) | 512 Kbit  | 65536 | 128 |2| 0 |
| [25XM01](https://ww1.microchip.com/downloads/aemDocuments/documents/OTH/ProductDocuments/DataSheets/AT25M01-SPI-Serial-EEPROM-Data-Sheet-20006226A.pdf), [25X1024](https://ww1.microchip.com/downloads/aemDocuments/documents/MPD/ProductDocuments/DataSheets/25LC1024-1-Mbit-SPI-Bus-Serial-EEPROM-20002064E.pdf)| 1 Mbit | 131072  |  256 | 3  | 0  |
| [25XM02](https://ww1.microchip.com/downloads/aemDocuments/documents/OTH/ProductDocuments/DataSheets/AT25M02-SPI-Serial-EEPROM-Data-Sheet-20006230A.pdf)| 2 Mbit    |262144 | 256         | 3       |0            |
| [25XM04](https://ww1.microchip.com/downloads/aemDocuments/documents/MPD/ProductDocuments/DataSheets/25CSM04-4-Mbit-SPI-Serial-EEPROM-with-128-Bit-Serial-Number-and-Enhanced-Write-Protection-20005817D.pdf) | 4 Mbit  |524288| 256/512(STM)  |3       | 0             |

<br/>

{{% alert context="danger" %}}
25x/95x chips have a variety of part numbers, but tend to operate in the same way. Often a manufacturer specific part number indicates a different voltage range or upgraded features. AT25, 25LC, 25AA, 25CS and M95 are all part of same basic 25x family of chips. 
{{% /alert %}}  

{{% alert context="info" %}}
**93x** are Microwire EEPROMs, which use a older variant of the SPI protocol. They are also compatible with the SPI ```eeprom``` command.
{{% /alert %}}

##### Chip voltage requirements

|25x/95x Family|Minimum Voltage|Maximum Voltage|
|---|---|---|---|
|AT25|1.8V|5.5V|
|25LC|2.5V|5.5V|
|25AA|1.8V|5.5V|
|25CS|1.7V|5.5V|
|M95|2.5V|5.5V|

Before using the ```eeprom``` command, you'll need to enable a power supply with the [```W``` command]({{< relref "/docs/command-reference/#ww-power-supply-offon">}}). 

{{% alert context="warning" %}}
Some chips have Write Protect and Hold pins, these should also be held high for normal operation. If you're using a [flash chip adapter plank]({{< relref "/docs/overview/spi-flash-adapters/">}}) an easy way to hold these pins high is to enable pull-up resistors with the [```P``` command]({{< relref "/docs/command-reference/#pp-pull-up-resistors">}}).
{{% /alert %}}

#### SPI EEPROM dump to terminal

{{< termfile source="static/snippets/spi-eeprom-command-dump-partial.html" >}}

Display the contents of an EEPROM in the terminal. 
- ```eeprom dump -d <device>``` - display EEPROM contents
- ```eeprom dump -d <device> -s <start>``` - display EEPROM contents, starting at address `<start>`
- ```eeprom dump -d <device> -s <start> -b <bytes>``` - display a specific range of bytes, starting at address `<start>` and reading `<bytes>` bytes

#### SPI EEPROM read to file
{{< term  >}}
<span style="color:rgb(150,203,89)">SPI></span>&nbsp;eeprom&nbsp;read&nbsp;-d&nbsp;25x020&nbsp;-f&nbsp;eeprom.bin&nbsp;-v
25X020:&nbsp;256&nbsp;bytes,&nbsp;&nbsp;0&nbsp;block&nbsp;select&nbsp;bits,&nbsp;1&nbsp;byte&nbsp;address,&nbsp;8&nbsp;byte&nbsp;pages

Read:&nbsp;Reading&nbsp;EEPROM&nbsp;to&nbsp;file&nbsp;eeprom.bin...
Progress:&nbsp;[###########################]&nbsp;100.00%
Read&nbsp;complete
Read&nbsp;verify...
Progress:&nbsp;[###########################]&nbsp;100.00%
Read&nbsp;verify&nbsp;complete
Success&nbsp;:)

<span style="color:rgb(150,203,89)">SPI></span>&nbsp;
{{< /term>}}

Read the contents of an EEPROM and save it to a file.
- ```eeprom read -d <device> -f <file>``` - read EEPROM contents to file `<file>`
- ```eeprom read -d <device> -f <file> -v``` - read EEPROM contents to file `<file>`, verify the read operation

#### SPI EEPROM write from file
{{< term  >}}
<span style="color:rgb(150,203,89)">SPI></span>&nbsp;eeprom&nbsp;write&nbsp;-d&nbsp;25x020&nbsp;-f&nbsp;eeprom.bin&nbsp;-v
25X020:&nbsp;256&nbsp;bytes,&nbsp;&nbsp;0&nbsp;block&nbsp;select&nbsp;bits,&nbsp;1&nbsp;byte&nbsp;address,&nbsp;8&nbsp;byte&nbsp;pages

Write:&nbsp;Writing&nbsp;EEPROM&nbsp;from&nbsp;file&nbsp;eeprom.bin...
Progress:&nbsp;[###########################]&nbsp;100.00%
Write&nbsp;complete
Write&nbsp;verify...
Progress:&nbsp;[###########################]&nbsp;100.00%
Write&nbsp;verify&nbsp;complete
Success&nbsp;:)

<span style="color:rgb(150,203,89)">SPI></span>&nbsp;
{{< /term>}}
Write the contents of a file to an EEPROM.
- ```eeprom write -d <device> -f <file>``` - write EEPROM from file `<file>`
- ```eeprom write -d <device> -f <file> -v``` - write EEPROM from file `<file>`, verify the write operation

{{% alert context="danger" %}}
If the **file is bigger than the EEPROM**, only the first bytes of the file will be written to the EEPROM. The rest of the file will be ignored.

If the **file is smaller than the EEPROM**, the full file will be written to the EEPROM, and the rest of the EEPROM will be left unchanged. The eeprom command will read the target page from the EEPROM, write the new data to the page, and then write the full page back to the EEPROM. This is done to avoid writing partial pages, which some devices cannot handle.
{{% /alert %}}

#### SPI EEPROM verify against file
{{< term  >}}
<span style="color:rgb(150,203,89)">SPI></span>&nbsp;eeprom&nbsp;verify&nbsp;-d&nbsp;25x020&nbsp;-f&nbsp;eeprom.bin
25X020:&nbsp;256&nbsp;bytes,&nbsp;&nbsp;0&nbsp;block&nbsp;select&nbsp;bits,&nbsp;1&nbsp;byte&nbsp;address,&nbsp;8&nbsp;byte&nbsp;pages

Verify:&nbsp;Verifying&nbsp;EEPROM&nbsp;contents&nbsp;against&nbsp;file&nbsp;eeprom.bin...
Progress:&nbsp;[###########################]&nbsp;100.00%
Verify&nbsp;complete

<span style="color:rgb(150,203,89)">SPI></span>&nbsp;
{{< /term>}}
Verify the contents of an EEPROM match a file.
- ```eeprom verify -d <device> -f <file>``` - verify EEPROM contents against file `<file>`

{{% alert context="danger" %}}
If the **file is bigger than the EEPROM**, only the first bytes of the file will be verified against the EEPROM. The rest of the file will be ignored.

If the **file is smaller than the EEPROM**, the full file will be verified against the EEPROM, and the rest of the EEPROM will be ignored.
{{% /alert %}}

#### SPI EEPROM erase
{{< term  >}}
<span style="color:rgb(150,203,89)">SPI></span>&nbsp;eeprom&nbsp;erase&nbsp;-d&nbsp;25x020&nbsp;-v
25X020:&nbsp;256&nbsp;bytes,&nbsp;&nbsp;0&nbsp;block&nbsp;select&nbsp;bits,&nbsp;1&nbsp;byte&nbsp;address,&nbsp;8&nbsp;byte&nbsp;pages

Erase:&nbsp;Writing&nbsp;0xFF&nbsp;to&nbsp;all&nbsp;bytes...
Progress:&nbsp;[###########################]&nbsp;100.00%
Erase&nbsp;complete
Erase&nbsp;verify...
Progress:&nbsp;[###########################]&nbsp;100.00%
Erase&nbsp;verify&nbsp;complete
Success&nbsp;:)

<span style="color:rgb(150,203,89)">SPI></span>&nbsp;
{{< /term>}}

Erase the contents of an EEPROM, writing 0xFF to all bytes.
- ```eeprom erase -d <device>``` - erase EEPROM contents
- ```eeprom erase -d <device> -v``` - erase EEPROM contents, verify the erase operation

#### SPI EEPROM test
{{< term  >}}
<span style="color:rgb(150,203,89)">SPI></span>&nbsp;eeprom&nbsp;test&nbsp;-d&nbsp;25x020
25X020:&nbsp;256&nbsp;bytes,&nbsp;&nbsp;0&nbsp;block&nbsp;select&nbsp;bits,&nbsp;1&nbsp;byte&nbsp;address,&nbsp;8&nbsp;byte&nbsp;pages

Erase:&nbsp;Writing&nbsp;0xFF&nbsp;to&nbsp;all&nbsp;bytes...
Progress:&nbsp;[###########################]&nbsp;100.00%
Erase&nbsp;complete
Erase&nbsp;verify...
Progress:&nbsp;[###########################]&nbsp;100.00%
Erase&nbsp;verify&nbsp;complete

Test:&nbsp;Writing&nbsp;alternating&nbsp;patterns
Writing&nbsp;0xAA&nbsp;0x55...
Progress:&nbsp;[###########################]&nbsp;100.00%
Write&nbsp;complete
Write&nbsp;verify...
Progress:&nbsp;[###########################]&nbsp;100.00%
Write&nbsp;verify&nbsp;complete
Writing&nbsp;0x55&nbsp;0xAA...
Progress:&nbsp;[###########################]&nbsp;100.00%
Write&nbsp;complete
Write&nbsp;verify...
Progress:&nbsp;[###########################]&nbsp;100.00%
Write&nbsp;verify&nbsp;complete
Success&nbsp;:)

<span style="color:rgb(150,203,89)">SPI></span>&nbsp;
{{< /term>}}
Test I2C EEPROM functionality. Erase the EEPROM to 0xff and verify the erase. Then write alternating patterns of 0xAA and 0x55, verifying each write operation. Any stuck bits should be detected during the test.
- ```eeprom test -d <device>``` - test EEPROM functionality

#### SPI EEPROM show protection status
{{< termfile source="static/snippets/spi-eeprom-command-protect.html" >}}
Show the write protection status of the EEPROM.
- ```eeprom protection -d <device>``` - show the protection status of the EEPROM 

##### BP1, BP0, and WPEN bits
|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|WPEN|X|X|X|BP1|BP0|WEL|WIP|

Many SPI EEPROMS have some sort of write protection configured through the status register. 25X EEPROMs generally have two block protection bits (BP1, BP0) that disable writes to a memory range. The write protection can be reversed by clearing the protection bits.

|BP1|BP0|Protected Range|
|---|---|----------------|
|0|0|No protection|
|0|1|Upper 1/4|
|1|0|Upper 1/2|
|1|1|All|

BP1 and BP0 generally protect the upper 1/4, 1/2, or all of the EEPROM. 

The WPEN bit overrides the physical write protect pin. If the WPEN bit is 0, writes are allowed even if the WP pin is held low.

{{% alert context="danger" %}}
**Sometimes write protection is irreversible**. This is pretty rare, but we've seen one or two chips with this non-standard feature that otherwise work like a normal 25X chip. This does not apply to the 25X chips from Atmel/Microchip, which all have reversible write protection, but you might find it on some rarer chips. Always consult the datasheet if possible, or just leave the protection bits alone. 
{{% /alert %}}


#### SPI EEPROM update protection bits
{{< termfile source="static/snippets/spi-eeprom-command-protect-set.html" >}}
Update the block protection bits of the EEPROM. Protected blocks cannot be written to until the protection is removed.
- ```eeprom protect -d <device> -b <bits>``` - write the block protection bits of the EEPROM. `<bits>` is a 2-bit value (BP1, BP0) and protects memory regions according to the table below. For example `-b 0b11` protects the whole EEPROM, `-b 0b01` protects the upper 1/4 of the EEPROM, and `-b 0b00` disables all protection.
- ```eeprom protect -d <device> -w <value>``` - write the Write Pin ENable (WPEN) bit. If the WPEN bit is 0, it overrides the physical write protect pin. For example, `-w 0` disables the WPEN bit, allowing writes to the EEPROM even if the pin is held high.

|BP1|BP0|Protected Range|
|---|---|----------------|
|0|0|No protection|
|0|1|Upper 1/4|
|1|0|Upper 1/2|
|1|1|All|

{{% alert context="info" %}}
Many chips support block protection bits, fewer support the WPEN bit. To test what features a chip supports, use the ```-t``` flag to proble the write protect features. 
{{% /alert %}}

#### SPI EEPROM test write protection features
{{< termfile source="static/snippets/spi-eeprom-command-protect-test.html" >}}

25X EEPROMs frequently have block protection (BP) bits that disable writes to a memory range. Newer chips also have a Write Pin ENable (WPEN) bit that overrides the physical write protect pin. To probe the write protection features we try to enable all of them, then check which were actually enabled. The command will restore the original protection settings after the test.
- ```eeprom protect -d <device> -t``` - test the write protection features of the EEPROM. 

#### SPI EEPROM options and flags
{{< termfile source="static/snippets/spi-eeprom-command-help.html" >}}

|Option|Description|
|---|---|
|```eeprom list```|List all supported EEPROM devices|
|```eeprom dump```|Dump EEPROM contents to terminal. Space to continue, x to exit.|
|```eeprom read```|Read EEPROM contents to file|
|```eeprom write```|Write EEPROM from file|
|```eeprom verify```|Verify EEPROM contents against file|
|```eeprom erase```|Erase EEPROM contents, writing 0xFF to all bytes|
|```eeprom test```|Test EEPROM functionality, erase and write alternating patterns|
|```eeprom protect```|Show, update, test the write protection status of the EEPROM|

Options tell the eeprom command what to do.

{{% alert context="info" %}}
Always check the latest options and flags with ```eeprom -h``` to see the most up-to-date features.
{{% /alert %}}

|Flag|Description|
|---|---|
|```-d <device>```|Specify the EEPROM device type, e.g. 24x02|
|```-f <file>```|Specify the file for read, write and verify|
|```-v```|Verify the read or write operation|
|```-p <value>```|Update the block protection bits, 0b00-0b11 valid|
|```-w <value>```|Update the Write Pin ENable (WPEN) bit, 0 to disable, 1 to enable|
|```-t```|Test the write protection features of the EEPROM|
|```-s <start>```|Specify the start address for dump operations|
|```-b <bytes>```|Specify the number of bytes to read for dump operations|
|```-q```|Dump quiet mode, no address or ASCII columns. Useful for copying HEX values to a HEX editor.|
|```-c```|Dump: disable paging, display all data in one go.|
|```-h```|Show help for the ```eeprom``` command|

Flags pass file names and other settings.


### Device demos
- [NOR Flash Memory]({{% relref "/docs/devices/spi-flash-chips/" %}})
- [W25Q64 NOR FLASH]({{% relref "/docs/devices/w25q64/" %}})

## 2-WIRE

-   **Bus:** 2 wire bus with bidirectional data (SDA) line and a clock (SCL) line
-   **Connections:** two data pins (SDA/SCL) and ground. An additional pin is reserved for RESET, and is controlled by the ```{```/```}``` commands.
-   **Output type:** open drain/open collector
-   **Pull-up resistors:** always required (2K - 10K ohms)
-   **Maximum voltage:** 5volts

{{% alert context="info" %}}
2-wire is a generic 8bit protocol mode with a bidirectional data line (SDA) and a clock line (SCL). 2-wire can be used to interface with [SLE4442 smart cards]({{% relref "/docs/devices/sle4442/" %}}), half-duplex SPI devices and other 2 wire busses that don't use a full I2C implementation.
{{% /alert %}}

### Connections

| Bus Pirate | Direction                     | Circuit | Description   |
|------------|--------------------------|---------|---------------|
| SDA       | <font size="+2">↔</font> | SDA     | Serial Data   |
| SCL        | <font size="+2">→</font> | SCL     | Serial Clock  |
| RST        | <font size="+2">→</font> | RST     | Reset signal for some devices  |
| GND        | <font size="+2">⏚</font> | GND     | Signal Ground |

### Configuration options

{{< termfile source="static/snippets/cmdref-mode-2wire-config.html" >}}


### Pull-up resistors

2-Wire is an open-collector bus, it requires pull-up resistors to hold the
clock and data lines high and create the data '1'. In 2-Wire mode, the Bus Pirate doesn't
output high, it only pulls low. Without pull-up resistors there can
never be a '1'. 

Enable the Bus Pirate onboard pull-up resistors with the [```P``` command]({{% relref "/docs/command-reference/#pp-pull-up-resistors" %}}).

{{% alert context="info" %}}
- 2-Wire requires pull-up resistors to hold the clock and data lines high.
- Without pull-up resistors there can never be a '1'. 
- Enable the Bus Pirate onboard pull-up resistors with the [```P``` command]({{% relref "/docs/command-reference/#pp-pull-up-resistors" %}}).
{{% /alert %}}

### Bus commands

|Command|Description|
|-------|-----------|
| [ | Issue I2C-style START condition. Some devices don't follow the I2C standard, but still use a similar START condition. |
| ] | Issue I2C-style STOP condition. Some devices don't follow the I2C standard, but still use a similar STOP condition.|
| \{ | RST/reset pin **high** |
| } | RST/reset pin **low** |
| r       | Read one byte. (r:1…255 for bulk reads)|
| 0b      | Write this binary value. Format is 0b00000000 for a byte, but partial bytes are also fine: 0b1001.|
| 0x      | Write this HEX value. Format is 0x01. Partial bytes are fine: 0xA. A-F can be lower-case or capital letters. |
| 0-255   | Write this decimal value. Any number not preceded by 0x or 0b is interpreted as a decimal value. |
| ```space```| Value delimiter. Use a space to separate numbers. No delimiter is required between non-number values: \{0xa6 0 0 16 5 0b111 0xaF rrrr}. |
| ^ | One clock tick, low to high to low transition. |
| / | Set clock pin high. |
| \ | Set clock pin low. |
| _ | Set data pin low. |
| - | Set data pin high. |
| . | Read data pin. |

{{% alert context="info" %}}
2WIRE supports bitwise operations on the clock and data lines. The commands ```^```, ```/```, ```\```, ```_```, ```-``` and ```.``` control the clock and data lines directly. This is useful for some devices that require precise timing or specific signal patterns.
{{% /alert %}}

{{% readfile "/_common/other-commands.md" %}}

### ```sniff``` 2WIRE bus sniffer

{{< termfile source="static/snippets/cmdref-mode-2wire-sniff-help.html" >}}

Sniff 8 bit I2C-like protocols that don't use an ACK/NAK bit, for example the SLE4442 smart card.

### ```sle4442``` Work with SLE4442 smart cards

{{< asciicast src="/screencast/sle4442-command-cast.json" poster="npt:0:18"  idleTimeLimit=2 >}}
<br/>
The ```sle4442``` command in the Bus Pirate's 2-WIRE mode automates the process of reading, writing and unlocking a [SLE4442 smart card]({{< relref "/docs/devices/sle4442" >}}).

{{% alert context="info" %}}
Use ```sle4442 -h``` to see the latest options and features.
{{% /alert %}}

#### SLE4442 Answer to Reset (ATR)

{{< termfile source="static/snippets/sle4442-cmd-init.html" >}}
 
```sle4442``` and ```sle4442 init``` reset the card and decodes the Answer To Reset (ATR) response.

- ```sle4442 init``` - reset the card and decode the ATR

#### Dump SLE4442 card memory

{{< termfile source="static/snippets/sle4442-cmd-dump.html" >}}

```sle4442 dump``` reads and displays the main, security and protection memory areas. The card **does not** need to be unlocked to read the contents. The passcode is only required to write to the card.
- ```sle4442 dump``` - read and display the main, security and protection memory areas
- ```sle4442 dump -s 0x06 -b 32``` - read and display the main memory area starting at address 0x06, reading 32 bytes
- ```sle4442 dump -f <file name>``` - read and save the main, security and protection memory areas to a file

#### Unlock SLE4442 card with passcode

{{< termfile source="static/snippets/sle4442-cmd-unlock.html" >}}

```sle4442 unlock``` unlocks the card using the Programmable Security Code (PSC). Use the ```-p``` flag to specify the PSC. 

- ```sle4442 unlock -p <psc>``` - unlock the card with the current PSC

{{% alert context="info" %}}
New cards usually have a default PSC of 0xffffff.
{{% /alert %}}

#### Write data to SLE4442 card

{{< termfile source="static/snippets/sle4442-cmd-write.html" >}}

```sle4442 write``` writes a single byte of data to the card. Specify the address with the ```-a``` flag and the data value with the ```-v``` flag.

- ```sle4442 write -a <address> -v <value>``` - write a byte of data to the card

{{% alert context="warning" %}}
The card must be unlocked before writing data.
{{% /alert %}}

#### Change SLE4442 passcode/PSC

{{< termfile source="static/snippets/sle4442-cmd-psc-set.html" >}}

```sle4442 psc``` changes the Programmable Security Code (PSC). Use the ```-p``` flag to specify the current PSC and the ```-n``` flag to specify the new PSC.

- ```sle4442 psc -p <current_psc> -n <new_psc>``` - change the PSC

#### Write protection memory

Write the protection bits in the SLE4442 card with the ```sle4442 protect``` command. Use the ```-v``` flag to specify the protection bits. The protection bits are a 32-bit value where each bit corresponds to a specific memory area.

- ```sle4442 protect -v 0xffffffff``` sets the write protection bits in the SLE4442 card. Use the ```-v``` flag to specify the protection bits.

#### Options and flags

{{< termfile source="static/snippets/cmdref-mode-2wire-sle4442-help.html" >}}

{{% alert context="info" %}}
Use ```sle4442 -h``` to see the latest options and features.
{{% /alert %}}

|Option|Description|
|------|-----------|
|sle4442 init|Initialize and probe the card Answer To Reset|
|sle4442 dump|Display main, security and protect memory, optional save to file|
|sle4442 unlock|Unlock card with Programmable Security Code (PSC)|
|sle4442 write|Write data to card (requires unlock)|
|sle4442 erase|Erase data from range 0x32-0x255 (requires unlock)|
|sle4442 psc|Change Programmable Security Code (PSC)|
|sle4442 protect|Set write protection bits in the card|

Options tell the SLE4442 command what to do.

|Flag|Description|
|------|-----------|
|-a|Write address flag|
|-v|Write value flag|
|-p|Current Programmable Security Code (PSC) flag|
|-n|New Programmable Security Code (PSC) flag|
|-f|File flag, specify a file to save the memory dump|
|-s|Start address for memory dump|
|-b|Number of bytes in memory dump|
|-q|Memory dump quiet mode, no address or ASCII columns. Useful for copying HEX values to a HEX editor.|

Flags pass file names and other settings to the command.

### Device demos
- [SLE4442 Smart Card]({{% relref "/docs/devices/sle4442/" %}})

## 3-WIRE

-   **Bus:** [SPI](http://en.wikipedia.org/wiki/Serial_Peripheral_Interface_Bus)-like bus with granular control of the clock and data lines
-   **Connections:** four data pins (MOSI/MISO/CLOCK/CHIP_SELECT) and ground
-   **Output type:** push-pull (1.65-5volts)
-   **Maximum voltage:** 5volts

{{% alert context="info" %}}
3WIRE is like [SPI]({{% relref "/docs/command-reference/#spi" %}}) with extra commmands to control the clock and data lines individually.
{{% /alert %}} 

### Connections

| Bus Pirate | Direction                    | Circuit | Description          |
|------------|--------------------------|---------|----------------------|
| MOSI       | <font size="+2">→</font> | MOSI    | Master Out Sub In |
| MISO       | <font size="+2">←</font> | MISO    | Master In Sub Out |
| CS         | <font size="+2">→</font> | CS      | Chip Select          |
| CLK        | <font size="+2">→</font> | CLK     | Clock signal         |
| GND        | <font size="+2">⏚</font> | GND     | Signal Ground        |

### Configuration options

{{< termfile source="static/snippets/cmdref-mode-3wire-config.html" >}}

### Bus commands

|Command|Description|
|-------|-----------|
|[| 	Chip select (CS) active|
|{| 	Chip Select (CS) active, show the SPI read byte while writing|
|] or }| 	Chip Select (CS) disable|
| r       | Read one byte. (r:1…255 for bulk reads)|
| 0b      | Write this binary value. Format is 0b00000000 for a byte, but partial bytes are also fine: 0b1001.|
| 0x      | Write this HEX value. Format is 0x01. Partial bytes are fine: 0xA. A-F can be lower-case or capital letters. |
| 0-255   | Write this decimal value. Any number not preceded by 0x or 0b is interpreted as a decimal value. |
| ```space```| Value delimiter. Use a space to separate numbers. No delimiter is required between non-number values: \{0xa6 0 0 16 5 0b111 0xaF rrrr}. |
| ^ | One clock tick, low to high to low transition. |
| / | Set clock pin high. |
| \ | Set clock pin low. |
| _ | Set MOSI pin low. |
| - | Set MOSI pin high. |
| . | Read MISO pin. |

{{% alert context="info" %}}
3WIRE supports bitwise operations on the clock and data lines. The commands ```^```, ```/```, ```\```, ```_```, ```-``` and ```.``` control the clock and data lines directly. This is useful for some devices that require precise timing or specific signal patterns.
{{% /alert %}}

{{% readfile "/_common/other-commands.md" %}}

## DIO

-   **Bus:** DIO (digital input/output)
-   **Connections:** all IOs available for use
-   **Output type:** tristate (push-pull, high impedance) (1.65-5volts)
-   **Maximum voltage:** 5volts

{{< asciicast src="/screencast/dio-use.json" poster="npt:0:24"  idleTimeLimit=2 autoPlay=false >}}
<br/>
{{% alert context="info" %}}
DIO is a mode with no specific protocol. All the Bus Pirate pins are free for use as [input/ouputs]({{% relref "/docs/command-reference/#aa-auxiliary-pin-control-lowhighread" %}}), [frequency generators]({{% relref "/docs/command-reference/#gg-frequency-generator" %}}), [frequency measurement]({{% relref "/docs/command-reference/#ff-measure-frequency" %}}), etc.
{{% /alert %}} 

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:rgb(150,203,89)">DIO></span>&nbsp;> 0xff

<span style="color:#bfa530">TX:</span>&nbsp;0xFF
<span style="color:rgb(150,203,89)">DIO></span>&nbsp;> 0x00

<span style="color:#bfa530">TX:</span>&nbsp;0x00
<span style="color:rgb(150,203,89)">DIO></span>&nbsp;> 0b10101010

<span style="color:#bfa530">TX:</span>&nbsp;0b10101010
<span style="color:rgb(150,203,89)">DIO></span>&nbsp;> 0b01010101

<span style="color:#bfa530">TX:</span>&nbsp;0b01010101
{{< /term >}}

Bus commands can be used to control all the unused IO pins at once, or use `r` to read the state of all pins.
- `>0x00` - set all pins low
- `>0xff` - set all pins high
- `>0b10101010` - set every other pin high/low
- `>0b01010101` - set every other pin low/high
- `>r` - read the state of all pins
- `>@.0` - make pin 0 an input (used in bus command context)
- `@ 0` - make pin 0 an input (note no `>` is used)

Return a pin to input with the `@` [auxiliary pin]({{% relref "/docs/command-reference/#aa-auxiliary-pin-control-lowhighread" %}}) read command. 

Pins with active frequency generation or measurement are not changed.

{{% alert context="info" %}}
Don't forget to start bus command with the `>` bus command character. 
{{% /alert %}}

## LED - WS2812/SK6812/'NeoPixel'

-   **Bus:** [WS2812/SK6812/'NeoPixel'](https://www.mouser.com/pdfDocs/WS2812B-2020_V10_EN_181106150240761.pdf) one wire
-   **Connections:** one data pin (SDO), and ground
-   **Output type:** 1.65-5volts
-   **Maximum voltage:** 5volts

WS2812/SK6812 are common RGB LEDs with a one wire interface. 

{{% alert context="danger" %}}
LEDs are power hungry, up to 60mA each at full brightness. The programmable power supply is rated for 300mA maximum. The LEDs will need an external power supply when driving more than a few in a strip.
{{% /alert %}}


### Connections

| Bus Pirate | Direction       | Circuit | Description   |
|------------|--------------------------|---------|---------------|
| SDO       | <font size="+2">→</font> | DIN     | Serial Data Out   |
| GND        | <font size="+2">⏚</font> | GND     | Signal Ground |

### Configuration options

{{< termfile source="static/snippets/cmdref-mode-led-config.html" >}}

### Bus commands

|Command|Description|
|-------|--------------|
| [ or \{ | Reset (low for >280us)|
| ] or } | --|
| 0b      | Write this binary value. Format is 0b00000000 for a byte, but partial bytes are also fine: 0b1001.|
| 0x      | Write this HEX value. Format is 0x01. Partial bytes are fine: 0xA. A-F can be lower-case or capital letters. |
| 0-255   | Write this decimal value. Any number not preceded by 0x or 0b is interpreted as a decimal value. |
| ```space```| Value delimiter. Use a space to separate numbers. No delimiter is required between non-number values: \{0xa6 0 0 16 5 0b111 0xaF rrrr}. |

{{% readfile "/_common/other-commands.md" %}}

### Device demos

- [Onboard SK6812 LED demo]({{% relref "/docs/tutorial-basics/leds-demo/" %}})
- [WS2812/SK6812/'NeoPixel' LED strip demo]({{% relref "/docs/devices/ws2812-sk6812-neopixel/" %}})

## LED - APA102/SK9822

-   **Bus:** [APA102/SK9822](https://www.mouser.com/datasheet/2/737/APA102_2020_SMD_LED-2487271.pdf) two wire
-   **Connections:** two data pins (SDO, SCL), and ground
-   **Output type:** 1.65-5volts
-   **Maximum voltage:** 5volts

APA102/SK9822 are common RGB LEDs with a two wire interface. 

{{% alert context="danger" %}}
LEDs are power hungry, up to 60mA each at full brightness. The programmable power supply is rated for 300mA maximum. The LEDs will need an external power supply when driving more than a few in a strip.
{{% /alert %}}


### Connections

| Bus Pirate | Direction                     | Circuit | Description   |
|------------|--------------------------|---------|---------------|
| SDO       | <font size="+2">→</font> | SDI     | Serial Data Out   |
| SCL        | <font size="+2">→</font> | CKI     | Serial Clock  |
| GND        | <font size="+2">⏚</font> | GND     | Signal Ground |

### Configuration options

{{< termfile source="static/snippets/cmdref-mode-led-config.html" >}}

### Bus commands

|Command|Description|
|-------|--------------|
| [ or \{ | Start Frame (0x00000000) |
| ] or } | End Frame (0xffffffff)|
| 0b      | Write this binary value. Format is 0b00000000 for a byte, but partial bytes are also fine: 0b1001.|
| 0x      | Write this HEX value. Format is 0x01. Partial bytes are fine: 0xA. A-F can be lower-case or capital letters. |
| 0-255   | Write this decimal value. Any number not preceded by 0x or 0b is interpreted as a decimal value. |
| ```space```| Value delimiter. Use a space to separate numbers. No delimiter is required between non-number values: \{0xa6 0 0 16 5 0b111 0xaF rrrr}. |

{{% readfile "/_common/other-commands.md" %}}

### Device demos

- [APA102/SK9822 LED strip demo]({{% relref "/docs/devices/apa102-sk9822/" %}}) 
 
## INFRARED - RAW

-   **Bus:** Infrared (IR) signals (raw)
-   **Connections:** one transmit pin, one receive pin and ground
-   **Output type:** open drain input, push-pull ouput (1.65-5volts)
-  **Maximum voltage:** 5volts

{{% alert context="info" %}}
Infrared is a mode for sending and receiving infrared signals. The Bus Pirate can send and receive  RC5 and NEC protocols, and raw IR signals. Compatible with the [IR Toy v3 plank]({{% relref "/docs/overview/infrared-toy-v3/" %}}).
{{% /alert %}}

### Connections

| Bus Pirate | Direction                     | Circuit | Description   |
|------------|--------------------------|---------|---------------|
| LERN (IO1) | <font size="+2">←</font> | LEARNER      | 20-60kHz IR learner receiver  |
| BARR (IO3) | <font size="+2">←</font> | 38K BARRIER      | 38kHz IR barrier receiver |
| IRTX (IO4) | <font size="+2">→</font> | TRANSMIT      | IR transmitter LED |
| 38K (IO5) |<font size="+2">←</font> | 38K DEMODULATOR      | 36-40kHz IR demodulator |
| 56K (IO7) |<font size="+2">←</font> | 56K DEMODULATOR      | 56kHz IR demodulator |

### Configuration options

{{< termfile source="static/snippets/cmdref-mode-infrared-config.html" >}}

### Bus commands

{{% readfile "/_common/other-commands.md" %}}

### ```tvbgone```

{{% alert context="info" %}}
TV-B-Gone, turn off many brands of TV
{{% /alert %}}

### ```irtx```

{{% alert context="info" %}}
Transmit IR signals (aIR format)
{{% /alert %}}

### ```irrx```

{{% alert context="info" %}}
Receive, record, retransmit IR signals (aIR format)
{{% /alert %}}

### Device demos

- [Infrared Remote Controls]({{% relref "/docs/devices/infrared-remote-control/" %}})


## INFRARED - NEC

-   **Bus:** NEC Infrared (IR) remote control protocol
-   **Connections:** one transmit pin, one receive pin and ground
-   **Output type:** open drain input, push-pull ouput (1.65-5volts)
-  **Maximum voltage:** 5volts

{{% alert context="info" %}}
Infrared is a mode for sending and receiving infrared signals. The Bus Pirate can send and receive  RC5 and NEC protocols, and raw IR signals. Compatible with the [IR Toy v3 plank]({{% relref "/docs/overview/infrared-toy-v3/" %}}).
{{% /alert %}}

### Connections

| Bus Pirate | Direction                     | Circuit | Description   |
|------------|--------------------------|---------|---------------|
| BARR (IO3) | <font size="+2">←</font> | 38K BARRIER      | 38kHz IR barrier receiver |
| IRTX (IO4) | <font size="+2">→</font> | TRANSMIT      | IR transmitter LED |
| 38K (IO5) |<font size="+2">←</font> | 38K DEMODULATOR      | 36-40kHz IR demodulator |
| 56K (IO7) |<font size="+2">←</font> | 56K DEMODULATOR      | 56kHz IR demodulator |
<!-- | LERN (IO1) | <font size="+2">←</font> | LEARNER      | 20-60kHz IR learner receiver  |-->

### Configuration options

{{< termfile source="static/snippets/cmdref-mode-infrared-config.html" >}}

### Bus commands

{{% readfile "/_common/other-commands.md" %}}


### Device demos

- [Infrared Remote Controls]({{% relref "/docs/devices/infrared-remote-control/" %}})


## INFRARED - RC5

-   **Bus:** RC5 Infrared (IR) remote control protocol
-   **Connections:** one transmit pin, one receive pin and ground
-   **Output type:** open drain input, push-pull ouput (1.65-5volts)
-  **Maximum voltage:** 5volts

{{% alert context="info" %}}
Infrared is a mode for sending and receiving infrared signals. The Bus Pirate can send and receive  RC5 and NEC protocols, and raw IR signals. Compatible with the [IR Toy v3 plank]({{% relref "/docs/overview/infrared-toy-v3/" %}}).
{{% /alert %}}

### Connections

| Bus Pirate | Direction                     | Circuit | Description   |
|------------|--------------------------|---------|---------------|
| BARR (IO3) | <font size="+2">←</font> | 38K BARRIER      | 38kHz IR barrier receiver |
| IRTX (IO4) | <font size="+2">→</font> | TRANSMIT      | IR transmitter LED |
| 38K (IO5) |<font size="+2">←</font> | 38K DEMODULATOR      | 36-40kHz IR demodulator |
| 56K (IO7) |<font size="+2">←</font> | 56K DEMODULATOR      | 56kHz IR demodulator |
<!-- | LERN (IO1) | <font size="+2">←</font> | LEARNER      | 20-60kHz IR learner receiver  |-->

### Configuration options

{{< termfile source="static/snippets/cmdref-mode-infrared-config.html" >}}

### Bus commands


{{% readfile "/_common/other-commands.md" %}}

### Device demos

- [Infrared Remote Controls]({{% relref "/docs/devices/infrared-remote-control/" %}})

## JTAG
-   **Bus:** JTAG
-   **Connections:** varries
-   **Output type:** push-pull (1.65-5volts)
-   **Maximum voltage:** 5volts

{{% alert context="info" %}}
JTAG mode is **NOT** for working directly with JTAG devices (yet!). JTAG mode hosts [blueTag](https://github.com/Aodrulez/blueTag), an open source JTAG and SWD pin finder.
{{% /alert %}}

### ```bluetag``` JTAG & SWD pinout finder

{{< asciicast src="/screencast/bluetag-jtag-demo.json" poster="npt:0:23"  idleTimeLimit=2 autoPlay=false >}}
<br/>
[blueTag](https://github.com/Aodrulez/blueTag) is an open source JTAG and SWD pin finder integrated into the Bus Pirate firmware. It can identify the JTAG/SWD pins on a target device by sending a series of test signals and analyzing the responses. 

#### Connections
- Connect the Bus Pirate IO pins to the suspected JTAG/SWD pins on the target device. 
- Start with IO0 and work your way up to IO7. 
- If possible, look for ground pours and power pins on the JTAG or SWD port and avoid connecting IO pins to them.
- Connect the Bus Pirate ground pin to the target device ground.
- Power the device.

{{% alert context="warning" %}}
Measure the target device supply/pin voltage. The Bus Pirate IO pins should set to match with the ```W``` power supply command. 
{{% /alert %}}

{{% alert context="info" %}}
If the target has an obvious voltage out pin, then you can power the Bus Pirate IO pins from that. Attach the Bus Pirate VOUT pin to the target voltage out pin and **skip the ```W``` power supply command setup step**. 
{{% /alert %}}

#### Search for JTAG pins

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">JTAG></span> bluetag jtag -c 8
Number of channels set to: 8

     Progress: [##########################] 100.00%

     [  Pinout  ]  TDI=IO0 TDO=IO3 TCK=IO4 TMS=IO2 TRST=N/A

     [ Device 0 ]  0x59602093 (mfg: 'Xilinx', part: 0x9602, ver: 0x5)

<span style="color:#96cb59">JTAG></span> 
{{< /term >}}

- ```bluetag jtag -c <channels>``` - search for JTAG pins on the target device. The ```-c``` flag specifies the number of channels to search, starting from IO0.

This chip is identified as a Xilinx device with the pinout: TDI=IO0 TDO=IO3 TCK=IO4 TMS=IO2 TRST=N/A.

{{% alert context="info" %}}
If the scan fails, you can try again with the ```-d``` flag to [disable pin pulsing]({{< relref "/docs/command-reference/#bluetag-options" >}}). This may help find stubborn JTAG pins.
{{% /alert %}}

#### Search for SWD pins

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">JTAG></span> bluetag swd -c 8
Number of channels set to: 8

     Progress: [##########################] 100.00%

     [  Pinout  ]  SWDIO=IO5 SWCLK=IO6

     [ Device 0 ]  0x0BC12477 (mfg: 'ARM Ltd', part: 0xbc12, ver: 0x0)

<span style="color:#96cb59">JTAG></span> 
{{< /term >}}

- ```bluetag swd -c <channels>``` - search for SWD pins on the target device. The ```-c``` flag specifies the number of channels to search, starting from IO0.

This chip is identified as an ARM device with the pinout: SWDIO=IO5 SWCLK=IO6.

{{% alert context="info" %}}
The Bus Pirate can find its own SWD pins. Connect IO0-IO2 to the three debug pins on the bottom of the Bus Pirate and then run ```bluetag swd -c 3```. 
{{% /alert %}}

#### ```bluetag``` Options

{{< termfile source="static/snippets/bluetag-help.html" >}}

|Option|Description|
|---|---|
|```-c <channels>```|Number of channels to search, starting from IO0.|
|```-v```|Show blueTag version.|
|```-d```|Disable pin pulsing, may help if normal search fails.|
|```-h```|Show help message.|

### Device demos
- [JTAG & SWD pinout finder]({{% relref "/docs/devices/jtag-swd-pin-finder/" %}})
