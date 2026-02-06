+++
title = "BPIO2 FlatBuffers Interface"
description = "Bus Pirate FlatBuffers interface (BPIO2) documentation"
icon = "article"
date = "2023-05-22T00:27:57+01:00"
lastmod = "2023-05-22T00:27:57+01:00"
draft = false
toc = true
weight = 80505
+++

![alt text](/images/docs/protocol-bpio2/f33267dd266389489198f64e70e020669f340f66.png)

The Bus Pirate BPIO2 binmode is a [FlatBuffers](https://flatbuffers.dev/) interface designed for simple and complete control of the Bus Pirate hardware from an application or script. 

Pre-compiled BPIO2 FlatBuffer "tooling" is available for [a bunch](https://github.com/DangerousPrototypes/BusPirate-BPIO2-flatbuffer-interface) of common languages. This means you can easily integrate the BPIO2 protocol into your projects without needing to write extensive parsing or serialization code.

- [Python Library](#python-library) - A demonstration library for interacting with BPIO2 
- [Rust crate](https://github.com/DangerousPrototypes/BusPirate-BPIO2-flatbuffer-interface/tree/main/rust) - A library for interacting with BPIO2 in Rust
- [Debugging](#debugging) - Display BPIO2 debug information in the Bus Pirate terminal
- [FlatBuffer Tooling Download](#flat-buffer-tooling-download) - Download precompiled FlatBuffer tooling for BPIO2
- [Compile your own tooling](#compiling-your-own-tooling) - How to generate your own tooling from the BPIO2 schema
- [Schema](#schema) - Explanation of the low level FlatBuffers tables used in BPIO2

## Why BPIO2?

Bus Pirate v3.x has a **BBIO1** interface, an abbreviation for **Bit Bang Input/Output**. The interface was originally designed for simple bit-banging only, other protocols were hacked in later. If I may say so, it was a bit of a mess. 

We *could* call this BBIO2, but it's in no way similar to the original BBIO1 interface and it's only marginally for bit-banging. Instead, we call it BPIO2 meaning the second generation of Bus Pirate I/O.

### Configure BPIO2 binmode

{{< term>}}
SPI> binmode

Select binary mode
 1. SUMP logic analyzer
 2. BPIO2 flatbuffer interface
 3. Arduino CH32V003 SWIO
 4. Follow along logic analyzer
 5. Legacy Binary Mode for Flashrom and AVRdude (EXPERIMENTAL)
 6. IRMAN IR decoder (LIRC, etc)
 7. AIR capture (AnalysIR, etc)
 x. Exit
 > 2
{{</ term>}}

Be sure to configure BPIO2 as the binmode. Type `binmode` in the Bus Pirate terminal, and select the BPIO2 flatbuffer interface. Optionally save BPIO2 as the default binmode when prompted.

BPIO2 is now available on the second serial port (the one not used by the terminal).

{{% alert context="danger" %}}
**Nothing working?**
- Be sure the BPIO2 binmode is selected 
- Connect to the second serial port (not the terminal serial port).
{{% /alert %}}

## Python Library

[Download the BPIO2 Python library and examples](https://github.com/DangerousPrototypes/BusPirate-BPIO2-flatbuffer-interface/tree/main/python):
- `/` - Example Python scripts using the library
- `/pybpio/` - Python library for BPIO2
- `/tooling/` - FlatBuffers generated Python tooling
- `/flatbuffers/` - FlatBuffers library for Python

### Install

In addition to Python 3 or later, pyserial and COBS are required to use the BPIO2 library. You can install them using pip:

```bash
pip3 install -r requirements.txt
```

### Client Show Status

The BPIO2 client has a `show_status()` method that sends a `StatusRequest` to the Bus Pirate and prints the `StatusResponse`.

1. Import the BPIOClient class from the bpio_client module.
2. Create an instance of the BPIOClient class, passing the serial port as an argument.
3. Call the `show_status()` method to retrieve and print the status of the Bus Pirate.

```python
>>> from bpio_client import BPIOClient
>>> client = BPIOClient("COM35")
>>> client.show_status()
StatusResponse:
  FlatBuffers version: 2.0
  Hardware version: 5 REV10
  Firmware version: 0.0
  Firmware git hash: unknown
  Firmware date: Aug 19 2025 13:07:05
  Available modes: HiZ, 1WIRE, UART, HDUART, I2C, SPI, 2WIRE, 3WIRE, DIO, LED, INFRARED, JTAG
  Current mode: I2C
  Mode bit order: MSB
  Pin labels: ON, SDA, SCL, , , , , , , GND
  Mode max packet size: 640 bytes
  Mode max write size: 512 bytes
  Mode max read size: 512 bytes
  Number of LEDs: 18
  Pull-up resistors enabled: True
  Power supply enabled: True
  PSU set voltage: 3299 mV
  PSU set current: 300 mA
  PSU measured voltage: 3300 mV
  PSU measured current: 3 mA
  PSU over current error: No
  IO ADC values (mV): 3312, 3316, 3312, 3304, 3300, 3291, 3280, 3285
  IO directions: IO0:IN, IO1:IN, IO2:IN, IO3:IN, IO4:IN, IO5:IN, IO6:IN, IO7:IN
  IO values: IO0:HIGH, IO1:HIGH, IO2:HIGH, IO3:HIGH, IO4:HIGH, IO5:HIGH, IO6:HIGH, IO7:HIGH
  Disk size: 97.69779205322266 MB
  Disk space used: 0.0 MB
```
### Client Get Status

You can also get the status as a dictionary, and access the individual fields.

```python
>>> from bpio_client import BPIOClient
>>> client = BPIOClient("COM35")
>>> status = client.status_request()
>>> print(status['error'])
None
```
{{% alert context="info" %}}
The ```error``` field will be populated if there is an error in the request. If the request is successful, it will be `None`.
{{% /alert %}}

```python 
>>> print(status)
{
   'error':None,
   'version_flatbuffers_major':2,
   'version_flatbuffers_minor':0,
   'version_hardware_major':5,
   'version_hardware_minor':10,
   'version_firmware_major':0,
   'version_firmware_minor':0,
   'version_firmware_git_hash':'unknown',
   'version_firmware_date':'Aug 19 2025 13:07:05',
   'modes_available':['HiZ','1WIRE','UART','HDUART','I2C','SPI','2WIRE','3WIRE','DIO','LED','INFRARED','JTAG'],
   'mode_current':'I2C',
   'mode_pin_labels':['ON','SDA','SCL','','','','','','','GND'],
   'mode_bitorder_msb':True,
   'mode_max_packet_size':640,
   'mode_max_write':512,
   'mode_max_read':512,
   'psu_enabled':True,
   'psu_set_mv':3299,
   'psu_set_ma':300,
   'psu_measured_mv':3329,
   'psu_measured_ma':2,
   'psu_current_error':False,
   'pullup_enabled':True,
   'adc_mv':[3320,3269,3267,3266,3283,3306,3309,3319],
   'io_direction':0,
   'io_value':255,
   'disk_size_mb':97.69779205322266,
   'disk_used_mb':0.0,
   'led_count':18
}
```

### Mode Change

```python
>>> from bpio_client import BPIOClient
>>> from bpio_i2c import BPIOI2C
>>> client = BPIOClient("COM35")
>>> i2c = BPIOI2C(client)
>>> i2c.configure(speed=400000, pullup_enable=True, psu_enable=True, psu_voltage_mv=3300, psu_current_ma=0)
True
>>>
```

There is a Python class for interacting with each mode such as I2C, 1-Wire and SPI. Initialize the mode class with a BPIOClient instance.

```python
i2c.configure(speed=400000, pullup_enable=True, psu_enable=True, psu_voltage_mv=3300, psu_current_ma=0)
```

To enter and configure a mode use the `configure()` function. configure() accepts arguments for the mode configuration and other hardware settings. Here we set the I2C speed to 400kHz, enable pull-ups, and set the power supply to 3.3volts with no current limit. The method returns `True` if the configuration was successful, or `False` if there was an error.

Mode configuration arguments are reused for multiple modes, and correspond to the FlatBuffer [mode configuration table]({{< relref "/docs/binmode-reference/protocol-bpio2/#modeconfiguration" >}}) names:

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `speed` | uint32 | 20000 | Speed in Hz or baud for the mode |
| `data_bits` | uint8 | 8 | Data bits for the mode (e.g., 8 for UART) |
| `parity` | bool | false | Parity for the mode (true for even parity, false for no parity) |
| `stop_bits` | uint8 | 1 | Stop bits for the mode (1 or 2) |
| `flow_control` | bool | false | Flow control for the mode (true for enabled, false for disabled) |
| `signal_inversion` | bool | false | Signal inversion for the mode (true for inverted, false for normal) |
| `clock_stretch` | bool | false | Clock stretching for I2C mode (true for enabled, false for disabled) |
| `clock_polarity` | bool | false | Clock idle polarity for SPI mode (true for high, false for low) |
| `clock_phase` | bool | false | Clock phase for SPI mode (false for leading edge, true for trailing edge) |
| `chip_select_idle` | bool | true | Chip select idle state for SPI and 3-wire modes (true for idle high, false for idle low) |
| `submode` | uint8 | - | Submode for LED and INFRARED modes |
| `tx_modulation` | uint32 | - | TX modulation frequency for INFRARED mode |
| `rx_sensor` | uint8 | - | RX sensor configuration for INFRARED mode|

Other hardware can be configured at the same time as the mode change, for example the power supply, and pull-up resistors. The parameter names are also identical to the FlatBuffer [configuration request table]({{< relref "/docs/binmode-reference/protocol-bpio2/#configuration-3">}}) names:

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `mode_bitorder_msb` | bool | - | Bit order MSB |
| `mode_bitorder_lsb` | bool | - | Bit order LSB |
| `psu_disable` | bool | - | Disable power supply |
| `psu_enable` | bool | - | Enable power supply |
| `psu_set_mv` | uint32 | - | Set voltage in millivolts (psu_enable must = true) |
| `psu_set_ma` | uint16 | 300 | Set current in milliamps, 0 for unlimited (psu_enable must = true) |
| `pullup_disable` | bool | - | Disable pull-up resistors |
| `pullup_enable` | bool | - | Enable pull-up resistors |
| `io_direction_mask` | uint8 | - | Bitmask for IO pin directions (1=modify this pin) |
| `io_direction` | uint8 | - | IO pin directions in 8 bit byte (1 output, 0 input) |
| `io_value_mask` | uint8 | - | Bitmask for IO pin values (1=modify this pin) |
| `io_value` | uint8 | - | IO pin values in 8 bit byte (1 high, 0 low) |
| `led_resume` | bool | - | Resume LED effect after setting with led_color |
| `led_color` | [uint32] | - | LED colors in RGB format (0xRRGGBB) |
| `print_string` | string | - | String to print in the Bus Pirate terminal (e.g. for debugging) |

### Mode Get Functions

Mode classes have getter functions that query Bus Pirate status information.

#### Get All Status Info
{{% alert context="danger" %}}
Each call to a getter function sends a request to the Bus Pirate and waits for a response. This can be slow. If you need a lot of status info it's faster to use `get_status()` which retrieves all status information in one go, and then access the specific fields from the returned dictionary.
{{% /alert %}}

```python
>>> status = i2c.get_status()
>>> print(status['mode_current'])
I2C
```

{{% alert context="info" %}}
The mode ```get_status()``` function returns a dictionary with all status information for the current mode. This is the same dictionary returned by `client.status_request()`. Each mode also has a `show_status()` function that prints all the status info in a human-readable format.
{{% /alert %}}

#### Version Information

| Method | Returns | Description |
|--------|---------|-------------|
| `get_version_flatbuffers_major()` | int | FlatBuffers version major number (BPIOx)|
| `get_version_flatbuffers_minor()` | int | FlatBuffers version minor number |
| `get_version_hardware_major()` | int | Hardware version major number |
| `get_version_hardware_minor()` | int | Hardware revision number |
| `get_version_firmware_major()` | int | Firmware version major number |
| `get_version_firmware_minor()` | int | Firmware version minor number |
| `get_version_firmware_git_hash()` | string | Git hash of the firmware build |
| `get_version_firmware_date()` | string | Date and time of firmware build |

#### Mode Status

| Method | Returns | Description |
|--------|---------|-------------|
| `get_modes_available()` | list | Array of all available mode names |
| `get_mode_current()` | string | Name of the currently active mode |
| `get_mode_pin_labels()` | list | Array of pin labels for current mode |
| `get_mode_bitorder_msb()` | bool | Current bit order (True for MSB first) |
| `get_mode_max_packet_size()` | int | Maximum FlatBuffers packet size for the current mode |
| `get_mode_max_write()` | int | Maximum number of bytes that can be written in one operation |
| `get_mode_max_read()` | int | Maximum number of bytes that can be read in one operation |


#### Power Supply Status

| Method | Returns | Description |
|--------|---------|-------------|
| `get_psu_enabled()` | bool | Whether power supply is enabled |
| `get_psu_set_mv()` | int | Set voltage in millivolts |
| `get_psu_set_ma()` | int | Set current limit in milliamps |
| `get_psu_measured_mv()` | int | Measured voltage in millivolts |
| `get_psu_measured_ma()` | int | Measured current in milliamps |
| `get_psu_current_error()` | bool | Over-current error status |

#### Hardware Status

| Method | Returns | Description |
|--------|---------|-------------|
| `get_pullup_enabled()` | bool | Whether pull-up resistors are enabled |
| `get_adc_mv()` | list | ADC measurements for each IO pin in mV |
| `get_io_direction()` | int | IO pin directions bitmask (1=output, 0=input) |
| `get_io_value()` | int | IO pin values bitmask (1=high, 0=low) |
| `get_led_count()` | int | Number of LEDs on the device |

#### Storage Status

| Method | Returns | Description |
|--------|---------|-------------|
| `get_disk_size_mb()` | float | Total disk size in megabytes |
| `get_disk_used_mb()` | float | Used disk space in megabytes |

#### Usage Examples

```python
>>> i2c = BPIOI2C(client)
>>> # Get hardware version
>>> print(f"Hardware: {i2c.get_version_hardware_major()}.{i2c.get_version_hardware_minor()}")
Hardware: 5.10
>>> # Get current mode
>>> print(f"Current mode: {i2c.get_mode_current()}")
Current mode: I2C
>>> # Get PSU voltage
>>> print(f"PSU voltage: {i2c.get_psu_measured_mv()}mV")
PSU voltage: 3300mV
>>> # Get IO pin directions
>>> print(f"IO directions: {i2c.get_io_direction():08b}")
IO directions: 00000000
```

All getter functions return `None` if there is an error or if the Bus Pirate is not properly configured.

### Mode Set Functions

Mode classes have setter functions that configure the Bus Pirate hardware and settings. 

#### Bit Order Configuration

| Method | Parameters | Description |
|--------|------------|-------------|
| `set_mode_bitorder_msb()` | None | Set mode bit order to MSB (Most Significant Bit) first |
| `set_mode_bitorder_lsb()` | None | Set mode bit order to LSB (Least Significant Bit) first |

#### Power Supply Control

| Method | Parameters | Description |
|--------|------------|-------------|
| `set_psu_disable()` | None | Disable the Bus Pirate power supply |
| `set_psu_enable(voltage_mv, current_ma)` | `voltage_mv` (int, default=3300)<br>`current_ma` (int, default=300) | Enable power supply with specified voltage and current limit |

{{% alert context="info" %}}
Power supply voltage is specified in millivolts, current in milliamps. Set current to 0 to disable the current limit.
{{% /alert %}}

#### Pull-up Resistor Control

| Method | Parameters | Description |
|--------|------------|-------------|
| `set_pullup_disable()` | None | Disable pull-up resistors |
| `set_pullup_enable()` | None | Enable pull-up resistors |

#### IO Pin Control

| Method | Parameters | Description |
|--------|------------|-------------|
| `set_io_direction(direction_mask, direction)` | `direction_mask` (int)<br>`direction` (int) | Set IO pin directions (1=output, 0=input) |
| `set_io_value(value_mask, value)` | `value_mask` (int)<br>`value` (int) | Set IO pin values (1=high, 0=low) |

{{% alert context="info" %}}
For IO operations, use bitmasks to specify which pins to modify. For example, to set pin 7 as output and drive it low, use `set_io_direction(0x80, 0x80)` and `set_io_value(0x80, 0x00)`.
{{% /alert %}}

#### LED Control

| Method | Parameters | Description |
|--------|------------|-------------|
| `set_led_resume()` | None | Resume previous LED effect after configuration using set_led_colors() |
| `set_led_color(colors)` | `colors` (list) | Set LED colors in RGB format (0xRRGGBB) |

#### Utility Functions

| Method | Parameters | Description |
|--------|------------|-------------|
| `set_print_string(string)` | `string` (str) | Print string on Bus Pirate terminal |
| `set_hardware_bootloader()` | None | Enter bootloader mode |
| `set_hardware_reset()` | None | Perform hardware reset of the device |
| `set_hardware_selftest()` | None | Perform self-test of the Bus Pirate hardware |


#### Usage Examples

```python
>>> i2c = BPIOI2C(client)
>>> # Enable power supply at 5V with 500mA limit
>>> i2c.set_psu_enable(voltage_mv=5000, current_ma=500)
True
>>> # Set IO pin 7 as output and drive it low
>>> i2c.set_io_direction(direction_mask=0x80, direction=0x80)
True
>>> i2c.set_io_value(value_mask=0x80, value=0x00)
True
>>> # Set all LEDs to red
>>> i2c.set_led_color([0xFF0000] * 18)
True
>>> # Print debug message
>>> i2c.set_print_string("Debug: I2C configured")
True
```

Setter functions return `True` if successful, `False` if there was an error, or `None` if not configured
 
### I2C Data

The `BPIOI2C` class provides support for I2C bus transactions.

#### Configuration

| Method | Parameters | Description |
|--------|------------|-------------|
| `configure(speed, clock_stretch, **kwargs)` | `speed` (int, default=400000)<br>`clock_stretch` (bool, default=False)<br>`**kwargs` (additional config) | Configure I2C mode with specified speed and clock stretching |

{{% alert context="info" %}}
Speed is specified in Hz (e.g., 400000 for 400kHz).
{{% /alert %}}  

#### I2C Operations

| Method | Parameters | Description |
|--------|------------|-------------|
| `start()` | None | Send I2C start condition |
| `stop()` | None | Send I2C stop condition |
| `write(data)` | `data` (list of bytes) | Write data bytes to I2C bus |
| `read(num_bytes)` | `num_bytes` (int) | Read specified number of bytes from I2C bus |
| `transfer(write_data, read_bytes)` | `write_data` (list, optional)<br>`read_bytes` (int, default=0) | Perform complete I2C transaction with start, write, restart, read, and stop |
| `scan(start_addr, end_addr)` | `start_addr` (int, default=0x00)<br>`end_addr` (int, default=0x7F) | Scan I2C bus for devices in specified address range |

{{% alert context="info" %}}
The first byte in `write_data` should be the 8 bit I2C device address, it will be used for both the write and read operation.
{{% /alert %}}

#### Basic Configuration
```python
>>> from bpio_client import BPIOClient
>>> from bpio_i2c import BPIOI2C
>>> client = BPIOClient("COM35")
>>> i2c = BPIOI2C(client)
>>> i2c.configure(speed=400000, clock_stretch=False)
True
```

#### Manual I2C Operations
```python
>>> i2c.start()                   # Send start condition
>>> i2c.write([0xA0, 0x00])       # Write device address and register
>>> i2c.stop()                    # Send stop condition
>>> i2c.start()                   # Send start condition again
>>> i2c.write([0xA1])             # Write read address
>>> data = i2c.read(2)            # Read 2 bytes
>>> i2c.stop()                    # Send stop condition
```

#### Complete Transaction
```python
>>> # Write to register 0x00 of device at address 0x50
>>> result = i2c.transfer(write_data=[0xA0, 0x00, 0x42])
>>> # Read 2 bytes from device at address 0x50, location 0x00 (e.g. 24x02 EEPROM)
>>> result = i2c.transfer(write_data=[0xA0, 0x00], read_bytes=2)
```

#### Bus Scanning
```python
>>> devices = i2c.scan()
Scanning I2C bus from 0x00 to 0x7F...
>>> print(f"Found devices: {[hex(addr) for addr in devices]}")
Found devices: ['0xa0', '0xa1']
```
### SPI Data

The `BPIOSPI` class provides support for SPI bus transactions.

#### Configuration

| Method | Parameters | Description |
|--------|------------|-------------|
| `configure(speed, clock_polarity, clock_phase, chip_select_idle, **kwargs)` | `speed` (int, default=1000000)<br>`clock_polarity` (bool, default=0)<br>`clock_phase` (bool, default=0)<br>`chip_select_idle` (bool, default=1)<br>`**kwargs` (additional config) | Configure SPI mode with clock settings and chip select polarity |

{{% alert context="info" %}}
Speed is specified in Hz (e.g., 1000000 for 1MHz).
{{% /alert %}}

#### SPI Operations

| Method | Parameters | Description |
|--------|------------|-------------|
| `select()` | None | Select SPI device|
| `deselect()` | None | Deselect SPI device|
| `write(data)` | `data` (list of bytes) | Write data bytes to SPI device |
| `read(num_bytes)` | `num_bytes` (int) | Read specified number of bytes from SPI device |
| `transfer(write_data, read_bytes)` | `write_data` (list of bytes)<br>`read_bytes` (int, optional) | Perform complete SPI transaction with select, write/read, and deselect |
| `transfer_duplex(write_data)` | `write_data` (list of bytes)<br>`read_bytes` (int, optional) | Perform full-duplex (read with write) SPI transaction with select, write/read, and deselect |

{{% alert context="info" %}}
The actual Chip Select pin state is set according to the SPI `chip_select_idle` state set during configuration.
{{% /alert %}}

#### Basic Configuration
```python
>>> from bpio_client import BPIOClient
>>> from bpio_spi import BPIOSPI
>>> client = BPIOClient("COM35")
>>> spi = BPIOSPI(client)
>>> spi.configure(speed=1000000, clock_polarity=False, clock_phase=False, chip_select_idle=True)
True
```

#### Manual SPI Operations
```python
>>> spi.select()                  # Pull chip select low
>>> spi.write([0x9F])             # Send command
>>> data = spi.read(3)            # Read response
>>> spi.deselect()                # Pull chip select high
```

#### Complete Transaction
```python
>>> # Send command 0x9F and read 3 bytes response
>>> result = spi.transfer(write_data=[0x9F], read_bytes=3)
>>> print(f"Device ID: {[hex(b) for b in result['data_read']]}")
Device ID: ['0xef', '0x40', '0x18']
```

### 1-Wire Data

The `BPIO1Wire` class provides support for 1-Wire bus transactions.

#### Configuration

| Method | Parameters | Description |
|--------|------------|-------------|
| `configure(**kwargs)` | `**kwargs` (configuration options) | Configure 1-Wire mode with additional hardware settings |

#### 1-Wire Operations

| Method | Parameters | Description |
|--------|------------|-------------|
| `reset()` | None | Reset the 1-Wire bus and check for device presence |
| `write(data)` | `data` (list of bytes) | Write data bytes to 1-Wire device |
| `read(num_bytes)` | `num_bytes` (int) | Read specified number of bytes from 1-Wire device |
| `transfer(write_data, read_bytes)` | `write_data` (list, optional)<br>`read_bytes` (int, default=0) | Perform complete 1-Wire transaction with reset, write, and read |


#### Basic Configuration
```python
>>> from bpio_client import BPIOClient
>>> from bpio_1wire import BPIO1Wire
>>> client = BPIOClient("COM35")
>>> ow = BPIO1Wire(client)
>>> ow.configure()
True
```

#### Manual 1-Wire Operations
```python
>>> ow.reset()                    # Reset bus and check for presence
>>> ow.write([0xCC])              # Skip ROM command
>>> ow.write([0x44])              # Start temperature conversion
>>> ow.reset()                    # Reset again
>>> ow.write([0xCC])              # Skip ROM command  
>>> ow.write([0xBE])              # Read scratchpad command
>>> data = ow.read(9)             # Read 9 bytes from scratchpad
```

#### Complete Transaction
```python
>>> # Read temperature from DS18B20
>>> result = ow.transfer(write_data=[0xCC, 0x44])  # Skip ROM + convert
>>> # Wait for conversion...
>>> result = ow.transfer(write_data=[0xCC, 0xBE], read_bytes=9)  # Read data
>>> print(f"Temperature data: {[hex(b) for b in result[:2]]}")
Temperature data: ['0x50', '0x05']
```

#### DS18B20 Temperature Sensor Example
```python
>>> # Complete temperature reading sequence
>>> ow.reset()
>>> ow.write([0xCC, 0x44])        # Skip ROM, start conversion
>>> # Wait 750ms for conversion
>>> import time
>>> time.sleep(0.75)
>>> ow.reset()
>>> ow.write([0xCC, 0xBE])        # Skip ROM, read scratchpad
>>> temp_data = ow.read(2)        # Read temperature bytes
>>> temp = (temp_data[1] << 8 | temp_data[0]) / 16.0
>>> print(f"Temperature: {temp}°C")
Temperature: 21.3125°C
```


### UART Data

The BPIO2 protocol supports full-duplex UART (Universal Asynchronous Receiver/Transmitter) communication, enabling both synchronous transactions and asynchronous data monitoring. The UART interface is accessed via the `BPIOUART` class in the `pybpio` Python library.

#### Features

- Configurable baud rate, data bits, parity, stop bits, flow control, and signal inversion
- Synchronous data write/read operations
- Asynchronous data monitoring (buffered or callback modes)
- Real-time event-driven or polling-based data handling

#### Configuration

|Method|Parameters|Description|
|------|----------|-----------|
|`configure(speed, data_bits, parity, stop_bits, flow_control, signal_inversion, async_callback, **kwargs)`|`speed` (int, default=115200)<br>`data_bits` (int, default=8)<br>`parity` (bool, default=False)<br>`stop_bits` (int, default=1)<br>`flow_control` (bool, default=False)<br>`signal_inversion` (bool, default=False)<br>`async_callback` (function or None)<br>`**kwargs` (configuration options) | Configure UART mode with specified parameters and optional async callback |

{{% alert context="info" %}}
Speed is specified in baud/bps (e.g., 115200).
{{% /alert %}} 

#### UART Operations

| Method | Parameters | Description |
|--------|------------|-------------|
| `write(data)` | `data` (bytes or list) | Write bytes to UART |
| `transfer(write_data, read_bytes)` | `write_data` (bytes or list)<br>`read_bytes` (int, optional) | Perform combined write/read UART transaction, 1 second read timeout |
| `read_async(clear_buffer)` | `clear_buffer` (boolean) | Read any available async data from UART buffer (buffered mode only) |

<!-- | `read(num_bytes)` | `num_bytes` (int) | Read specified number of bytes from UART, 1 second timeout |-->

{{% alert context="info" %}}
When using async callback mode, data is not buffered and must be handled in the callback function. In buffered mode, use `read_async()` to retrieve accumulated async data. See the async data monitoring section below for details.
{{% /alert %}}

#### Basic Configuration

```python
from pybpio.bpio_client import BPIOClient
from pybpio.bpio_uart import BPIOUART
client = BPIOClient('COM35')
uart = BPIOUART(client)
uart.configure(speed=115200, data_bits=8, parity=False, stop_bits=1, flow_control=False, signal_inversion=False, async_callback=None)
```
#### Synchronous Data Transfer

```python
response = uart.transfer(b"Ping", read_bytes=4)
if response and 'data_read' in response:
    print(response['data_read'])
```

Write bytes, then attempt to read 4 bytes with a 1 second timeout.

{{% alert context="info" %}}
Use a loop-back connection (RX connected to TX) to test from a single Bus Pirate.
{{% /alert %}}

#### Asynchronous Data Monitoring

{{% alert context="info" %}}
UART data can be received at any time, not just in response to a write or transfer operation. BPIO2 provides two modes for handling this asynchronous data: buffered mode and callback mode.
{{% /alert %}}

#### 1. Buffered Mode

```python
uart.configure(..., async_callback=None)  # No callback
# ...send data...
time.sleep(1)
data = uart.read_async()
if data:
    print("Async RX:", data)
```
Async data is accumulated in an internal buffer and can be read at any time.

#### 2. Callback Mode

```python
def on_uart_data(data):
    print("Received:", data)

uart.configure(..., async_callback=on_uart_data)
# ...send data...
# Callback is called automatically when data arrives
```

You can also provide your own callback function to process async data as it arrives in real time.

{{% alert context="info" %}}
When using async callback mode, data is not buffered and must be handled in the callback function you provide. In buffered mode, use `uart.read_async()` to retrieve accumulated data.
{{% /alert %}}

### LED Data

The `BPIOLED` class provides support for controlling RGB LEDs, including WS2812/SK6812/NeoPixel, APA102/SK9822, and the Bus Pirate's onboard RGB LED (also a SK6812).

#### Configuration

| Method | Parameters | Description |
|--------|------------|-------------|
| `configure(led_type, **kwargs)` | `led_type` (str or int)<br>`**kwargs` (additional config) | Configure LED mode with specified LED type: 'WS2812', 'APA102', or 'ONBOARD' (or 0, 1, 2) |

{{% alert context="info" %}}
**LED Types:**
- **WS2812** (0): WS2812/SK6812/NeoPixel compatible addressable LEDs (data on SDO pin)
- **APA102** (1): APA102/SK9822   addressable LEDs with brightness control (data on MOSI, clock on CLK)
- **ONBOARD** (2): Bus Pirate's built-in RGB LED
{{% /alert %}}

#### LED Operations

| Method | Parameters | Description |
|--------|------------|-------------|
| `write(data, start_main, stop_main)` | `data` (bytes or list) | Write raw data to LED device |
| `set_rgb(r, g, b, brightness)` | `r` (int, 0-255)<br>`g` (int, 0-255)<br>`b` (int, 0-255)<br>`brightness` (int, 0-31, default=31) | Set single LED to RGB color (brightness only for APA102) |
| `set_rgbw(r, g, b, w, brightness)` | `r` (int, 0-255)<br>`g` (int, 0-255)<br>`b` (int, 0-255)<br>`w` (int, 0-255)<br>`brightness` (int, 0-31, default=31) | Set single RGBW LED (WS2812 only) |
| `set_multiple_rgb(colors, brightness)` | `colors` (list of (r,g,b) tuples)<br>`brightness` (int, 0-31, default=31) | Set multiple LEDs with RGB values (brightness only for APA102) |
| `clear(num_leds)` | `num_leds` (int, default=1) | Turn off LEDs (set to black/off) |

{{% alert context="warning" %}}
Each method also accepts `start_main` and `stop_main` parameters that send the appropriate start and stop frames for the LED type
{{% /alert %}}

- ```start_main``` - RESET (WS2812/SK6812) or START FRAME (APA102) 
- ```stop_main``` - END FRAME (APA102) 

By default these are set to `True` so each call is treated as a full LED string update. Set to `False` for advanced users who want to manage the timing and framing themselves.


{{% alert context="info" %}}
For **APA102** LEDs, the `brightness` parameter controls individual LED brightness (0-31, where 31 is maximum brightness). For **WS2812** and **ONBOARD** LEDs, this value is ignored. 
{{% /alert %}}

#### Basic Configuration - Onboard LED
```python
>>> from bpio_client import BPIOClient
>>> from bpio_led import BPIOLED
>>> client = BPIOClient("COM35")
>>> led = BPIOLED(client)
>>> led.configure(led_type='ONBOARD')
True
```

#### Basic Configuration - WS2812 External LEDs
```python
>>> led = BPIOLED(client)
>>> led.configure(led_type='WS2812', psu_enable=True, psu_set_mv=5000, psu_set_ma=0)
True
```

{{% alert context="info" %}}
WS2812 LEDs typically require 5V power supply. Enable the Bus Pirate power supply with appropriate voltage when using external LEDs.
{{% /alert %}}

#### Basic Configuration - APA102 External LEDs
```python
>>> led = BPIOLED(client)
>>> led.configure(led_type='APA102', psu_enable=True, psu_set_mv=5000, psu_set_ma=0)
True
```

#### Single LED Control
```python
>>> # Set onboard LED to red
>>> led.configure(led_type='ONBOARD')
>>> led.set_rgb(255, 0, 0)

>>> # Set first WS2812 LED to green
>>> led.configure(led_type='WS2812', psu_enable=True, psu_set_mv=5000)
>>> led.set_rgb(0, 255, 0)

>>> # Set first APA102 LED to blue at 50% brightness
>>> led.configure(led_type='APA102', psu_enable=True, psu_set_mv=5000)
>>> led.set_rgb(0, 0, 255, brightness=15)
```

#### Multiple LED Control
```python
>>> # Rainbow pattern on 5 WS2812 LEDs
>>> led.configure(led_type='WS2812', psu_enable=True, psu_set_mv=5000)
>>> rainbow = [
...     (255, 0, 0),    # Red
...     (255, 165, 0),  # Orange
...     (255, 255, 0),  # Yellow
...     (0, 255, 0),    # Green
...     (0, 0, 255),    # Blue
... ]
>>> led.set_multiple_rgb(rainbow)

>>> # Same pattern on APA102 with brightness control
>>> led.configure(led_type='APA102', psu_enable=True, psu_set_mv=5000)
>>> led.set_multiple_rgb(rainbow, brightness=20)
```

#### RGBW LEDs (WS2812 only)

{{% alert context="danger" %}}
This is implemented in the Python library but not yet supported in the Bus Pirate firmware. Attempting to use RGBW functions with WS2812 LEDs will not work until the firmware is updated to support this feature.
{{% /alert %}}

```python
>>> led.configure(led_type='WS2812', psu_enable=True, psu_set_mv=5000)
>>> # Set RGBW LED with white channel
>>> led.set_rgbw(255, 0, 0, 128)  # Red + half white
```

{{% alert context="info" %}}
RGBW (Red, Green, Blue, White) LEDs have a dedicated white LED channel in addition to RGB. This is only supported by some WS2812 variants.
{{% /alert %}}

#### Clearing LEDs
```python
>>> # Turn off first LED
>>> led.clear(num_leds=1)

>>> # Turn off first 10 LEDs in a strip
>>> led.clear(num_leds=10)
```

#### Global Brightness Control (APA102)
```python
>>> led.configure(led_type='APA102', psu_enable=True, psu_set_mv=5000)
>>> # Test different brightness levels (0-31)
>>> for brightness in [31, 15, 7, 3, 1]:
...     led.set_rgb(255, 0, 0, brightness=brightness)
...     time.sleep(0.5)
```

{{% alert context="info" %}}
APA102 LEDs support hardware brightness control (0-31) independent of color values, allowing for smooth dimming without color shifts. WS2812 LEDs require dimming by reducing RGB values directly.
{{% /alert %}}

#### Write Raw Data to LEDs

|LED|Bytes per LED|Brightness Control|Color Format|
|---|-------------|------------------|------------|
|WS2812|3 bytes (GRB)|No|0xGGRRBB|
|ONBOARD|3 bytes (RGB)|No|0xRRGGBB|
|APA102|4 bytes (bBGB)|Yes (0xbb = 0-31)|0xbbBBGGRR with brightness byte|

Note that each supported LED has a different raw data format. 

**WS2812**
```python
>>> led.configure(led_type='WS2812', psu_enable=True, psu_set_mv=5000)
>>> # Example raw data for 2 LEDs (6 bytes for RGB)
>>> raw_data = [255, 0, 0, 0, 255, 0]  # First LED red, second LED green
>>> led.write(raw_data, start_main=True, stop_main=True)
```
**APA102**
```python
>>> led.configure(led_type='APA102', psu_enable=True, psu_set_mv=5000)
>>> # Example raw data for 2 LEDs (8 bytes for bBGB)
>>> raw_data = [0b11100000 | 31, 255, 0, 0, 0b11100000 | 15, 0, 255, 0]  # First LED bright red, second LED dim green
>>> led.write(raw_data, start_main=True, stop_main=True)
```

{{% alert context="danger" %}}
When writing raw data, you must manage the timing and framing according to the LED type specifications. For WS2812, ensure you send the correct reset timing before and after the data. For APA102, include the appropriate start and end frames.
{{% /alert %}}


## Debugging

{{< term>}}
[BPIO] Flatbuffer length: 64
[BPIO] Flatbuffer received, length: 64
[BPIO] Packet Type: 3
[Data Request] Start main condition: true
[Data Request] Start alternate condition: false
[Data Request] Data write vector is present
[Data Request] Data write vector length: 2
[Data Request] Data write: 0xA0 0x00
[Data Request] Bytes to read: 16
[Data Request] Stop main condition: true
[Data Request] Stop alternate condition: false
[Data Request] Protocol request
[I2C] Performing transaction
{{</ term>}}


{{% alert context="danger" %}}
Detailed debugging info can be displayed in the Bus Pirate terminal. Enable this by setting ```"bpio_debug_enable":1``` in your BPCONFIG.BP JSON file on the Bus Pirate internal storage. **Then reboot the Bus Pirate for this to take effect.**
{{% /alert %}}

Detailed debugging information can be displayed in the terminal when BPIO2 requests are processed. This can help you understand how the protocol works and troubleshoot any issues.

{{% alert context="warning" %}}
If you don't have a BPCONFIG.BP file, type configuration command ```c``` in the Bus Pirate terminal. At the prompt type x to exit, the configuration file will be created.
{{% /alert %}}

## FlatBuffers Tooling Download

Download precompiled FlatBuffer tooling, required includes, and demo libraries from the BPIO2 repo.
- [Download BPIO2 FlatBuffer Tooling and Libraries](https://github.com/DangerousPrototypes/BusPirate-BPIO2-flatbuffer-interface/tree/main)


{{% alert context="info" %}}
Most people won't need to interact with the FlatBuffer tooling directly. Ideally there will be a library that abstracts this away into simpler functions for common languages.
{{% /alert %}}

### Compile your own tooling

To generate your own tooling from the BPIO2 schema, you can use a FlatBuffers compiler with [bpio.fbs](https://github.com/DangerousPrototypes/BusPirate-BPIO2-flatbuffer-interface/blob/main/bpio.fbs).

#### C language tooling

```
flatcc -a bpio.fbs
```

To generate C tooling, use the [flatcc](https://github.com/dvidelabs/flatcc) compiler. This is the version we use to generate C tooling for the Bus Pirate firmware.

#### Other language tooling
```
flatc --python bpio.fbs
```

For C++, C#, Dart, Go, Java, JavaScript, Kotlin, Lobster, Lua, PHP, Python, Rust, Swift, TypeScript use [flatc](https://github.com/google/flatbuffers).

{{% alert context="info" %}}
Javasscript tooling was deprecated in recent versions of flatc. Transpile the TypeScript tooling to JavaScript using a TypeScript compiler.
{{% /alert %}}

### FlatBuffers Includes

In addition to the generated tooling, you will need to include the FlatBuffers support library for your language. Check the `/include/` folder in the BPIO2 repository for the required files.

## COBS Encoding

FlatBuffers request and response packets are encoded using COBS (Consistent Overhead Byte Stuffing) to ensure that the data can be transmitted over serial without issues. COBS encoding replaces zero bytes with a special marker. When data is sent 0x00 indicates the end of a packet. Most languages have a simple COBS library available, for example the [COBS Python library](https://pypi.org/project/cobs/) or the [C nanocobs implementation](https://github.com/charlesnicholson/nanocobs).

## Schema

BBIO2 uses **Request** and **Response** tables to communicate with the Bus Pirate. 
- The host device sends a **Request** to the Bus Pirate, which contains the operation to be performed.
- The Bus Pirate processes the request and sends back a **Response** containing the result of the operation.

There are currently several Request and Response pair 'tables':
- *StatusRequest/StatusResponse* - Used to check the status of the Bus Pirate and read pin states.
- *ConfigurationRequest/ConfigurationResponse* - Used to configure the Bus Pirate mode, settings and hardware.
- *DataRequest/DataResponse* - Used to send and receive data to/from the Bus Pirate.

Additionally there are wrapper tables for the requests and responses:
- *RequestPacket* - Contains the request type and the request data.
- *ResponsePacket* - Contains the response type and the response data.

There is a table for mode configuration:
- *ModeConfiguration* - Contains mode-specific settings, such as speed and other parameters.

### Request & Response Packets
- *RequestPacket* is the outermost table/wrapper for requests sent to the Bus Pirate.
- *ResponsePacket* is the outermost table/wrapper for responses sent by the Bus Pirate

#### RequestPacket

```flatbuffer
union RequestPacketContents { StatusRequest, ConfigurationRequest, DataRequest}

table RequestPacket {
  version_major:uint8;
  minimum_version_minor:uint16; // Minimum version minor for compatibility.
  contents:RequestPacketContents;
}
```

RequestPacket `contents` field contains one of the request tables (StatusRequest, ConfigurationRequest, DataRequest). This packet is sent from the host to the Bus Pirate.

`version_major` should be set to 2 for the current BPIO2 FlatBuffers tooling. version_major is used to indicate breaking changes in the protocol.

`minimum_version_minor` tells the Bus Pirate the minimum BPIO2 FlatBuffers tooling version required by the host. If the Bus Pirate firmware has a lower version, it will return an error in the ResponsePacket. This is used to provide clear compatibility error messages to the user, rather than silently failing or returning unexpected results.

{{% alert context="danger" %}}
The `minimum_version_minor` field is used to ensure compatibility between the host and the Bus Pirate. If the Bus Pirate tooling version is lower than the specified minimum version, it will return an error in the ResponsePacket. FlatBuffers **with the same version_major** are fully backwards compatible, so a host with older tooling will always be able to communicate with a Bus Pirate with newer tooling.  
{{% /alert %}}

#### ResponsePacket

```flatbuffer
union ResponsePacketContents {StatusResponse, ConfigurationResponse, DataResponse}

table ResponsePacket{
  error:string; // Error message if any.
  contents:ResponsePacketContents;
}
```

ResponsePacket `contents` field, which contains one of the response tables (StatusResponse, ConfigurationResponse, DataResponse). This packet is sent from the Bus Pirate to the host in response to a RequestPacket.

If there was an error processing the RequestPacket, the `error` field will contain a string describing the error. If there was no error, the `error` field will be empty.

Examples of errors that might be returned include:
- Invalid request type
- Packet size too large
- Timeout waiting for request
- FlatBuffers version_major or minimum_version_minor mismatch

### Status
- **StatusRequest** queries the current status of the Bus Pirate.
- **StatusResponse** contains the requested status information.

#### StatusRequest

```flatbuffers
enum StatusRequestTypes:byte{All, Version, Mode, Pullup, PSU, ADC, IO, Disk, LED}

table StatusRequest{
  query:[StatusRequestTypes]; // List of status queries to perform.
}
```

StatusRequest has a single field, `query`, which is an array of `StatusRequestTypes`. **All** returns everything, while the other types return specific queries which reduces the size and latency of the StatusResponse. 

{{% alert context="info" %}}
If no `query` is specified, all status information is returned.
{{% /alert %}} 

#### StatusResponse

```flatbuffers
// returns the status queries requested in StatusRequest
// if query is empty, then all queries are performed
table StatusResponse {
  error:string; // Error message if any.
  version_flatbuffers_major:uint8; // Flatbuffers version major.
  version_flatbuffers_minor:uint16; // Flatbuffers version minor.
  version_hardware_major:uint8; //HW version
  version_hardware_minor:uint8; //HW revision
  version_firmware_major:uint8;//FW version
  version_firmware_minor:uint8; //FW revision
  version_firmware_git_hash:string; //Git hash of the firmware.
  version_firmware_date:string; //Date of the firmware build.
  modes_available:[string]; // List of modes available on the device.
  mode_current:string; // Current mode name.
  mode_pin_labels:[string]; // Labels for the pins in the current mode.
  mode_bitorder_msb:bool; // Bit order for the current mode (true for MSB first, false for LSB first).
  mode_max_packet_size:uint32; // Maximum flat buffer packet size for the current mode.
  mode_max_write:uint32; // Maximum data write size for the current mode.
  mode_max_read:uint32; // Maximum data read size for the current mode.
  psu_enabled:bool; // Power supply enabled.
  psu_set_mv:uint32; // Power supply set voltage in millivolts.
  psu_set_ma:uint32; // Power supply set current in milliamps.
  psu_measured_mv:uint32; // Measured power supply voltage in millivolts.
  psu_measured_ma:uint32; // measured power supply current in milliamps.
  psu_current_error:bool; // Power supply fuse error.
  pullup_enabled:bool; // Pull-up resistors enabled.
  adc_mv:[uint32]; // IO pin ADC values in millivolts.
  io_direction:uint8; // IO pin directions (true for output, false for input).
  io_value:uint8; // IO pin values (true for high, false for low).
  disk_size_mb:float; // Size of the disk in megabytes.
  disk_used_mb:float; // Used space on the disk in megabytes.
  led_count:uint8; // Number of LEDs.
}
```

Depending on the query parameters, all of some of the fields in the `StatusResponse` will be populated. If an error occurs, the `error` field will contain a message describing the error.

#### Python Example

```python
"""Send a StatusRequest packet and return the response"""
"""Wrap contents in a RequestPacket"""

# Create a flatbuffers builder
builder = flatbuffers.Builder(1024)

# Create the query vector BEFORE starting the StatusRequest table
StatusRequest.StartQueryVector(builder, 1)
builder.PrependUint8(StatusRequestTypes.StatusRequestTypes.All)
query_vector = builder.EndVector()

# Create a StatusRequest
StatusRequest.Start(builder)
StatusRequest.AddQuery(builder, query_vector) # Add the query vector
status_request = StatusRequest.End(builder)

# Create a RequestPacket
RequestPacket.Start(builder)
RequestPacket.AddVersionMajor(builder, 2) 
RequestPacket.AddMinimumVersionMinor(builder, 0) # Update to match the minimum version tooling required
RequestPacket.AddContentsType(builder, RequestPacketContents.RequestPacketContents.StatusRequest) # Add the StatusRequest type
RequestPacket.AddContents(builder, status_request) # Add the StatusRequest
request_packet = RequestPacket.End(builder)

# Finish the builder and get the data
builder.Finish(request_packet)
data = builder.Output()

# COBS encode request and send to the serial port
resp_data = self.send_and_receive(data)

# Check for the response
if not resp_data:
    return False

# Decode ResponsePacket
resp_packet = ResponsePacket.ResponsePacket.GetRootAsResponsePacket(resp_data, 0)

# Check for ErrorResponse
if resp_packet.Error():
    print(f"Error: {resp_packet.Error().decode('utf-8')}")
    return False

# Confirm the response type matches expected
response_contents_type = resp_packet.ContentsType()
if response_contents_type != ResponsePacketContents.ResponsePacketContents.StatusResponse:
    print(f"Unexpected response type: {response_contents_type}")
    return False

# Decode StatusResponse
status_resp = StatusResponse.StatusResponse()
status_resp.Init(resp_packet.Contents().Bytes, resp_packet.Contents().Pos)

# Print hardware and firmware versions
print(f"  Flatbuffers version: {status_resp.VersionFlatbuffersMajor()}.{status_resp.VersionFlatbuffersMinor()}")
print(f"  Hardware version: {status_resp.VersionHardwareMajor()} REV{status_resp.VersionHardwareMinor()}")
print(f"  Firmware version: {status_resp.VersionFirmwareMajor()}.{status_resp.VersionFirmwareMinor()}")
print(f"  Firmware git hash: {status_resp.VersionFirmwareGitHash().decode('utf-8')}")
print(f"  Firmware date: {status_resp.VersionFirmwareDate().decode('utf-8')}")

# Print available modes
modes_available = [status_resp.ModesAvailable(i).decode('utf-8') for i in range(status_resp.ModesAvailableLength())]
print(f"  Available modes: {', '.join(modes_available)}")

```
The [complete example](https://github.com/DangerousPrototypes/BusPirate-BPIO2-flatbuffer-interface/blob/main/python/pybpio/docs_demo.py) is available in the BPIO2 FlatBuffers repo.

See [flatc](https://flatbuffers.dev/quick_start/) for language-specific usage instructions.

### Configuration
- A **ConfigurationRequest** configures the Bus Pirate settings and hardware. 
- A **ConfigurationResponse** contains any error message.

#### ConfigurationRequest

```flatbuffers
table ConfigurationRequest {
  mode:string; // Name of the mode to configure.
  mode_configuration:ModeConfiguration; // Configuration for the mode.
  mode_bitorder_msb:bool; // Bit order MSB.
  mode_bitorder_lsb:bool; // Bit order LSB.
  psu_disable:bool; // Disable power supply.
  psu_enable:bool; // Enable power supply.
  psu_set_mv:uint32; // Set voltage in millivolts (psu_enable must = true).
  psu_set_ma:uint16=300; // Set current in milliamps, 0 for unlimited (psu_enable must = true).
  pullup_disable:bool; // Disable pull-up resistors.
  pullup_enable:bool; // Enable pull-up resistors.
  io_direction_mask:uint8; // Bitmask for IO pin directions (1=modify this pin).
  io_direction:uint8; // IO pin directions in 8 bit byte (1 output, 0 input).
  io_value_mask:uint8; // Bitmask for IO pin values (1=modify this pin).
  io_value:uint8; // IO pin values in 8 bit byte (1 high, 0 low).
  led_resume:bool; // Resume LED effect after configuration.
  led_color:[uint32]; // LED colors in RGB format (0xRRGGBB).
  print_string:string; // string to print on terminal 
  hardware_bootloader:bool; // Enter bootloader mode.
  hardware_reset:bool; // Hardware reset the device.
  hardware_selftest:bool; // Perform a self-test on the device.
}
```

The `ConfigurationRequest` table configures Bus Pirate settings and hardware. 

{{% alert context="warning" %}}
Fields are processed in the order they are listed in the table. This means a single request can be used to enable a mode, set the power supply voltage, enable pull-up resistors, and configure pin directions in one go.
{{% /alert %}}

#### ModeConfiguration

```flatbuffer
table ModeConfiguration {
  speed:uint32=20000; // Speed in Hz or baud for the mode.
  data_bits:uint8=8; // Data bits for the mode (e.g., 8 for UART).
  parity:bool=false; // Parity for the mode (true for even parity, false for no parity).
  stop_bits:uint8=1; // Stop bits for the mode (1 or 2).
  flow_control:bool=false; // Flow control for the mode (true for enabled, false for disabled).
  signal_inversion:bool=false; // Signal inversion for the mode (true for inverted, false for normal).
  clock_stretch:bool=false; // Clock stretching for I2C mode (true for enabled,  false for disabled).
  clock_polarity:bool=false; // Clock idle polarity for SPI mode (true for high, false for low).
  clock_phase:bool=false; // Clock phase for SPI mode (false for leading edge, true for trailing edge).
  chip_select_idle:bool=true; // Chip select idle (0=idle low, 1=idle high) for SPI and 3-wire modes.
  submode:uint8; // Submode for LED and INFRARED modes (e.g., "RGB", "IR TX", "IR RX").
  tx_modulation:uint32; // TX modulation for INFRARED mode 
  rx_sensor:uint8; // RX sensor for INFRARED mode 
}
```
A ModeConfiguration table must be provided when changing modes. Pass the name of the mode in the `mode` field of the ConfigurationRequest, and include a `ModeConfiguration` table in the `mode_configuration` field.

#### ConfigurationResponse

```flatbuffer
table ConfigurationResponse{
  error:string; // Error message if any.
}
```

The `ConfigurationResponse` table `error` string will contain a message if there was a problem processing the configuration request. The `error` field will be empty if configuration was successful.

#### Python Example
```python
"""Create a BPIO ConfigurationRequest packet"""
builder = flatbuffers.Builder(1024)

# Create a mode string
mode_string = builder.CreateString("SPI")

# Create a ModeConfiguration
ModeConfiguration.Start(builder)
ModeConfiguration.AddSpeed(builder, 1000000)
ModeConfiguration.AddChipSelectIdle(builder, True)
ModeConfiguration.AddClockPhase(builder, False)
ModeConfiguration.AddClockPolarity(builder, False)
ModeConfiguration.AddDataBits(builder, 8)
mode_config = ModeConfiguration.End(builder)

# Set the LED colors
led_colors = [0xFF0000, 0x00FF00, 0x0000FF, 0xFFFF00, 0xFF00FF, 0x00FFFF] * 3
ConfigurationRequest.StartLedColorVector(builder, len(led_colors))
for color in reversed(led_colors):
    builder.PrependUint32(color)
led_color_vector = builder.EndVector()    

# Create the ConfigurationRequest
ConfigurationRequest.Start(builder)
ConfigurationRequest.AddMode(builder, mode_string)
ConfigurationRequest.AddModeConfiguration(builder, mode_config)
ConfigurationRequest.AddPsuEnable(builder, True)
ConfigurationRequest.AddPsuSetMv(builder, 3300)
ConfigurationRequest.AddPsuSetMa(builder, 300)
ConfigurationRequest.AddPullupEnable(builder, True)
ConfigurationRequest.AddLedColor(builder, led_color_vector) 
config_request = ConfigurationRequest.End(builder)

# Create a RequestPacket
RequestPacket.Start(builder)
RequestPacket.AddVersionMajor(builder, 2) 
RequestPacket.AddMinimumVersionMinor(builder, 0) # Update to match the minimum version tooling required
RequestPacket.AddContentsType(builder, RequestPacketContents.RequestPacketContents.ConfigurationRequest) # Add the ConfigRequest type
RequestPacket.AddContents(builder, config_request) # Add the ConfigRequest
request_packet = RequestPacket.End(builder)

# Finish the builder and get the data
builder.Finish(request_packet)
data = builder.Output()

# COBS encode request and send to the serial port
resp_data = self.send_and_receive(data)

# Check for the response
if not resp_data:
    return False

# Decode ResponsePacket
resp_packet = ResponsePacket.ResponsePacket.GetRootAsResponsePacket(resp_data, 0)

# Check for ErrorResponse
if resp_packet.Error():
    print(f"Error: {resp_packet.Error().decode('utf-8')}")
    return False     

# Confirm the response type matches expected
response_contents_type = resp_packet.ContentsType()
if response_contents_type != ResponsePacketContents.ResponsePacketContents.ConfigurationResponse:
    print(f"Unexpected response type: {response_contents_type}")
    return False        

# Decode ConfigurationResponse
config_resp = ConfigurationResponse.ConfigurationResponse()
config_resp.Init(resp_packet.Contents().Bytes, resp_packet.Contents().Pos)

# Print the error message if any
if config_resp.Error():
    print(f"Configuration error: {config_resp.Error().decode('utf-8')}")
```
The [complete example](https://github.com/DangerousPrototypes/BusPirate-BPIO2-flatbuffer-interface/blob/main/python/pybpio/docs_demo.py) is available in the BPIO2 FlatBuffers repo.

See [flatc](https://flatbuffers.dev/quick_start/) for language-specific usage instructions.

### Data
- The **DataRequest** table requests a data transaction in the currently selected mode.
- The **DataResponse** table contains any errors or data received while processing the request.

#### DataRequest

```flatbuffer
table DataRequest {
  start_main:bool; // Start condition.
  start_alt:bool; // Alternate start condition.
  data_write:[ubyte]; // Data to write
  bytes_read:uint16; // Number of bytes to read.
  stop_main:bool; // Stop condition.
  stop_alt:bool; // Alternate stop condition.
}
```

The `DataRequest` table has fields that mimic the general Bus Pirate bus syntax/commands: start, write, read, stop.

The goal is to do a complete transaction in a single request, such as writing and reading an I2C or SPI device. However, you have complete control over the transaction, so you can write, read, start or stop individually as well.

{{% alert context="warning" %}}
The maximum number of bytes in the `data_write` field is reported by the `mode_max_write` value in the StatusResponse. If you try to write more data than the maximum, the request will fail with an error.
{{% /alert %}}

|Field|Bus Pirate Syntax|Description|
|---|---|---|
|start_main|`[`|Any mode specific "start condition": 1-Wire RESET, I2C START, SPI Chip Select, etc |
|start_alt|`{`|Any mode specific "alternate start condition": SPI Chip Select Read with Write mode, 2WIRE Reset Pin, etc.|
|data_write|`0x00`|Write data (array) to the currently configured bus.|
|bytes_read|`r`|Read this many bytes from the currently configured bus.|
|stop_main|`]`|Any mode specific "stop condition": I2C STOP, SPI Chip Deselect, etc.|
|stop_alt|`}`|Any mode specific "alternate stop condition": currently unused.|

#### DataResponse

```flatbuffer
table DataResponse {
  error:string; // Error message if any.
  data_read:[ubyte]; // Data read from device
  is_async: bool = false;  // NEW 2.2: marks this as unsolicited async data
}
```

The `DataResponse` table `error` string will contain a message if there was a problem processing the data request. The `data_read` field will contain the data read from the device, if any.

**New in 2.2**: The `is_async` field marks this response as an unsolicited asynchronous data packet. This allows the Bus Pirate to send data to the host without a corresponding request, which is useful for modes like UART where data can be received at any time.

{{% alert context="warning" %}}
The maximum number of bytes in `data_read` reported by the `mode_max_read` value in the StatusResponse. If you try to read more bytes than the maximum, the request will fail with an error.
{{% /alert %}}

####  Python Example
```python
"""Create a BPIO DataRequest packet"""
builder = flatbuffers.Builder(1024)

# Define the data to write
data_write = [0x9F]
data_write_vector = builder.CreateByteVector(bytes(data_write))

# Create a DataRequest
DataRequest.Start(builder)
DataRequest.AddStartMain(builder, True)
DataRequest.AddDataWrite(builder, data_write_vector)
DataRequest.AddBytesRead(builder, 3)
DataRequest.AddStopMain(builder, True)
data_request = DataRequest.End(builder)

# Create a RequestPacket
RequestPacket.Start(builder)
RequestPacket.AddVersionMajor(builder, 2)
RequestPacket.AddMinimumVersionMinor(builder, 0) # Update to match the minimum version tooling required
RequestPacket.AddContentsType(builder, RequestPacketContents.RequestPacketContents.DataRequest) # Add the DataRequest type
RequestPacket.AddContents(builder, data_request) # Add the DataRequest
request_packet = RequestPacket.End(builder)

# Finish the builder and get the data
builder.Finish(request_packet)
data = builder.Output()

# COBS encode request and send to the serial port
resp_data = self.send_and_receive(data)

# Check for the response
if not resp_data:
    return False        

# Decode ResponsePacket
resp_packet = ResponsePacket.ResponsePacket.GetRootAsResponsePacket(resp_data, 0)

# Check for ErrorResponse
if resp_packet.Error():
    print(f"Error: {resp_packet.Error().decode('utf-8')}")
    return False        

# Confirm the response type matches expected
response_contents_type = resp_packet.ContentsType()
if response_contents_type != ResponsePacketContents.ResponsePacketContents.DataResponse:
    print(f"Unexpected response type: {response_contents_type}")
    return False     

# Decode DataResponse
data_resp = DataResponse.DataResponse()
data_resp.Init(resp_packet.Contents().Bytes, resp_packet.Contents().Pos)

# Print the error message if any
if data_resp.Error():
    print(f"Data request error: {data_resp.Error().decode('utf-8')}")
    return False

# Return data read, if any
if data_resp.DataReadLength() > 0:
    data_bytes = data_resp.DataReadAsNumpy()
    print(f"Data read: {' '.join(f'{b:02x}' for b in data_bytes)}")
```

The [complete example](https://github.com/DangerousPrototypes/BusPirate-BPIO2-flatbuffer-interface/blob/main/python/pybpio/docs_demo.py) is available in the BPIO2 FlatBuffers repo.

See [flatc](https://flatbuffers.dev/quick_start/) for language-specific usage instructions.

#### I2C DataRequest

Start, stop, write and read can all be done individually, or as a complete I2C write/read transaction. I2C data requests have a few special considerations:

- If `start_main` is true, the Bus Pirate will send a start condition 
- In a full transaction the first byte of `data_write` is used as the **8 bit**  I2C address. The I2C Read/Write bit is set and cleared automatically.
- If `start_main` is true and `data_write` has more than one byte (the I2C address), the Bus Pirate will send the first byte as the I2C address and write the rest of the bytes as data.
- If `data_write` has more than one byte **and** `bytes_read` is greater than 0, the Bus Pirate will send an I2C RESTART. 
- If `start_main` is true **or** an I2C RESET was sent: when `bytes_read` is greater than 0, the Bus Pirate will send the I2C Read address (`data_write` byte 0) and then read the requested bytes from the I2C device. If `stop_main` is true, the Bus Pirate will NACK the last byte read.
- If `stop_main` is true, the Bus Pirate will send a stop condition.

This is a bit confusing at first, but it allows you to do a complete I2C transaction in a single request, or to control the transaction manually by sending partial requests.
