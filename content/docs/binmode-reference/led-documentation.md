### LED Data

The `BPIOLED` class provides support for controlling RGB LEDs, including WS2812/NeoPixel, APA102/DotStar, and the Bus Pirate's onboard RGB LED.

#### Configuration

| Method | Parameters | Description |
|--------|------------|-------------|
| `configure(led_type, **kwargs)` | `led_type` (str or int)<br>`**kwargs` (additional config) | Configure LED mode with specified LED type: 'WS2812', 'APA102', or 'ONBOARD' (or 0, 1, 2) |

{{% alert context="info" %}}
**LED Types:**
- **WS2812** (0): WS2812/WS2812B/NeoPixel compatible addressable LEDs (data on SDO pin)
- **APA102** (1): APA102/DotStar addressable LEDs with brightness control (data on MOSI, clock on CLK)
- **ONBOARD** (2): Bus Pirate's built-in RGB LED
{{% /alert %}}

#### LED Operations

| Method | Parameters | Description |
|--------|------------|-------------|
| `write(data)` | `data` (bytes or list) | Write raw data to LED device |
| `set_rgb(r, g, b, brightness)` | `r` (int, 0-255)<br>`g` (int, 0-255)<br>`b` (int, 0-255)<br>`brightness` (int, 0-31, default=31) | Set single LED to RGB color (brightness only for APA102) |
| `set_rgbw(r, g, b, w, brightness)` | `r` (int, 0-255)<br>`g` (int, 0-255)<br>`b` (int, 0-255)<br>`w` (int, 0-255)<br>`brightness` (int, 0-31, default=31) | Set single RGBW LED (WS2812 only) |
| `set_multiple_rgb(colors, brightness)` | `colors` (list of (r,g,b) tuples)<br>`brightness` (int, 0-31, default=31) | Set multiple LEDs with RGB values (brightness only for APA102) |
| `clear(num_leds)` | `num_leds` (int, default=1) | Turn off LEDs (set to black/off) |

{{% alert context="info" %}}
For **APA102** LEDs, the `brightness` parameter controls individual LED brightness (0-31, where 31 is maximum brightness). For **WS2812** and **ONBOARD** LEDs, brightness is controlled by adjusting the RGB values directly.
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

#### Brightness Control (APA102)
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
