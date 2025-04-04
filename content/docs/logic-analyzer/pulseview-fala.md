+++
weight = 50300
title = 'PulseView (Follow Along)'
+++

![](/images/docs/fw/fala1.png)

FALA is a "live action" logic analyzer mode that automatically captures everything that happens when you send commands from the Bus Pirate. It eliminates the need to setup triggers and arm a second tool for debugging.  We like to call it FALA for short.

- [PulseView with FALA mode](https://github.com/DangerousPrototypes/BusPirate5-firmware/releases/tag/custom) (Windows)
- [libsigrok with FALA mode](https://github.com/phdussud/libsigrok/tree/bp5-fala) (Linux experimental)
- [Support topic](https://forum.buspirate.com/t/pulseview-demo-for-follow-along-logic-analyzer-mode/681) (Windows/Linux)

Currently pre-build FALA support is only available in a special patched version of PulseView for Windows.

Linux users have reported to build libsigrok library that works with FALA and recent versions of PulseView.

{{% alert context="danger" %}}
All Bus Pirate hardware supports follow along logic analyzer, however only Bus Pirate 6 has a second buffer to capture pins directly. In earlier hardware **all output pins are measured behind the IO buffer**. This means the logic capture may not match the actual output of the IO buffer. **This is not a problem when the Bus Pirate is used as a logic analyzer only and all pins are inputs**.
{{% /alert %}}

## Capabilities

- 62.5MSPS (or more if overclocked)
- 131K samples
- 8 channels
- Trigger: single pin, high or low
- Follow along logic analyzer mode
- Base pin can be set to an internal pin for debugging the Bus Pirate itself

## Enable FALA Interface

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">HiZ></span> binmode

<span style="color:#bfa530">Select binary mode</span>
 1. SUMP logic analyzer
 2. Binmode test framework
 3. Arduino CH32V003 SWIO
 4. Follow along logic analyzer
 x. <span style="color:#bfa530">Exit</span>
<span style="color:#96cb59"> ></span> 4
<span style="color:#bfa530">Binmode selected:</span> Follow along logic analyzer

<span style="color:#96cb59">HiZ></span> 
{{< /term >}}

Enable the FALA binary interface with the ```binmode``` command. This will configure the logic analyzer and send capture notifications to the Bus Pirate's second serial port.
- Type ```binmode``` in the terminal
- Select "Follow along lgic analyzer"


## Configure PulseView

![](/images/docs/fw/fala2.png)

Click "connect to device" and configure PulseView for the Bus Pirate FALA mode.

- Select the ```BP5 + binmode-FALA``` driver
- Select ```serial port``` and choose the Bus Pirate serial port that is **not** used for the terminal (lower number for me these days)
- Click ```Scan for devices```
- Hopefully the Bus Pirate is detected. Click OK.

### Run Capture on PulseView

![](/images/docs/fw/fala3.png)

Click "run" to start capturing.

## Capture Samples

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">HiZ></span> m

<span style="color:#bfa530">Mode selection</span>
 1. <span style="color:#bfa530">HiZ</span>
...
 6. <span style="color:#bfa530">SPI</span>
...
 x. <span style="color:#bfa530">Exit</span>
<span style="color:#96cb59">Mode ></span> 6

<span style="color:#bfa530">Use previous settings?</span>
 <span style="color:#bfa530">SPI speed:</span> 10 kHz
 <span style="color:#bfa530">Data bits:</span> 8
 <span style="color:#bfa530">Clock polarity:</span> Idle LOW
 <span style="color:#bfa530">Clock phase:</span> LEADING edge
 <span style="color:#bfa530">Chip select:</span> Active LOW (/CS)

<span style="color:#96cb59">y/n, x to exit (Y) ></span> y

{{< /term >}}

Enter a Bus Pirate mode. For now, SPI is best for testing.
- ```m``` to enter a mode, I suggest SPI

### Auto Capture Speed
{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#bfa530">Actual speed:</span> 10kHz
<span style="color:#bfa530">Logic analyzer speed:</span> 80000Hz (8x oversampling)
<span style="color:#bfa530">Use the 'logic' command to change capture settings</span>

<span style="color:#bfa530">Mode:</span> SPI
<span style="color:#96cb59">SPI></span> 
{{< /term >}}

When changing protocol modes with the ```m``` command, FALA will automatically set the capture speed to oversample the bus speed by a factor of 8. 

### Write Data


{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">SPI></span> W 5
<span style="color:#53a6e6">5.00</span>V<span style="color:#bfa530"> requested, closest value: <span style="color:#53a6e6">5.00</span></span>V
<span style="color:#bfa530">Current limit:</span>Disabled

<span style="color:#bfa530">Power supply:</span>Enabled
<span style="color:#bfa530">Vreg output: <span style="color:#53a6e6">5.0</span></span>V<span style="color:#bfa530">, Vref/Vout pin: <span style="color:#53a6e6">5.0</span></span>V<span style="color:#bfa530">, Current: <span style="color:#53a6e6">3.2</span></span>mA<span style="color:#bfa530">
</span>
<span style="color:#96cb59">SPI></span> [0x00 0xff 0x55 0xaa]

CS Enabled
<span style="color:#bfa530">TX:</span> 0x<span style="color:#53a6e6">00</span> 0x<span style="color:#53a6e6">FF</span> 0x<span style="color:#53a6e6">55</span> 0x<span style="color:#53a6e6">AA</span> 
CS Disabled

<span style="color:#bfa530">Logic analyzer:</span> 288 samples captured
<span style="color:#96cb59">SPI></span> 
{{< /term >}}

Every time you send data to the bus, the logic analyzer will capture samples. Enable the power supply and write some data.
- ```W 5``` to enable a 5volt power supply
- ```[0x00 0xff 0x55 0xaa]``` write some data to the bus
- ```Logic analyzer: 288 samples captured``` indicates how many samples were captured by the logic analyzer

### Live Logic View!

![](/images/docs/fw/fala4.png)

The samples are loaded into PulseView every time something happens on the bus.
- You may need to zoom a lot if there are only a few samples
- The box with a 2 (red arrow) indicates the number of captures. Up and down arrows scroll through the capture history

![](/images/docs/fw/fala5.png)

Autozoom fits all samples in the logic graph (red arrow).

## Change Capture Speed
{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">SPI></span> logic -o 16
Oversample rate set to: 16

Logic Analyzer settings
 Oversample rate: 16
 Sample frequency: 10000Hz

Note: oversample rate is not 1
Actual sample frequency: 160000Hz (16 * 10000Hz)

<span style="color:#96cb59">SPI></span> 
{{< /term >}}

The base capture speed or the oversample rate can can be changed with the ```logic``` command. Changing the oversample rate with the ```-o``` flag is probably easiest as the Bus Pirate will calculate the new sample frequency for you.

## Limitations

This is Windows only for now. The FALA mode is not supported in the official PulseView release.

Only a few modes have been updated to work with FALA. Some modes have internal buffers that cause the logic capture to end early or even return no samples. Each mode needs a new function to indicate when all bus activity is done. 

All Bus Pirate hardware supports the follow along logic analyzer, however only Bus Pirate 6 has a second buffer for the follow along mode. In earlier hardware **all output pins are measured behind the IO buffer**. This means the logic capture may not match the actual output of the IO buffer. **This is not a problem when the Bus Pirate is used as a logic analyzer only and all pins are inputs**.

## Logic Analyzer System

![](/images/docs/fw/logic-system.png)

{{% alert context="info" %}}
The ```logic``` command and the [follow along binmode interface](/logic-analyzer/pulseview-fala) can be run at the same time. However, the capture buffer is shared with [SUMP logic analyzer mode](/logic-analyzer/pulseview-sump). SUMP and follow along logic analyzer modes cannot be used at the same time and will result in a memory error warning.
{{% /alert %}}

## FALA Protocol

- [FALA protocol documentation](/binmode-reference/protocol-faladata)
