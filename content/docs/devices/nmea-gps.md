+++
weight = 40903
title = 'NMEA GPS module UART'
+++  

![](images/docs/demo/gps-map-screenshot.png)

GPS modules generally communicate over TTL serial and can be used to add GPS functionality to a variety of projects.

{{% alert context="info" %}}    
These GPS devices use a protocol called [`NMEA`](https://en.wikipedia.org/wiki/NMEA_0183), consisting of ASCII "sentences" (messages).  The Bus Pirate can decode these sentences and can be used to test or explore a GPS module.
{{% /alert %}}

{{% readfile "/_common/_footer/_footer-cart.md" %}}

## Connections
GPS modules will usually have at least 4 connections: `VCC`, `GND`, `TX`, and `RX`.  The actual location and order of these connections can vary from module to module and should be verified by the datasheet or silkscreen labels on the board.  The GPS module may have additional signals, but only the4 listed above are needed.

![](images/docs/demo/gps-rear.png)
![](images/docs/demo/gps-front.png)

|Bus Pirate|GPS Module|Description| 
|-|-|-|
|Vout|VCC|3.3 volt power supply|
|IO4/TX|RX|Transmit from Bus Pirate to GPS receive|
|IO5/RX|TX|Transmit from GPS to Bus Pirate receive|
|GND|GND|Ground|

The connections can be made with the Bus Pirate cable, clips, or "dupont" style jumpers.

![](images/docs/demo/gps-with-bp.png)

## See it in action

{{< asciicast src="/screencast/gps-cast.json" poster="npt:0:22"  idleTimeLimit=2 >}}

## Setup 
#### Mode setup

{{< termfile source="static/snippets/gps-command-setup.html" >}}

Communications to GPS modules are TTL serial, so start by setting the Bus Pirate mode to UART.  The data format for most of these modules is 9600 buad, 8 bits, no parity, and one stop bit.  Set as appropriate.

- `m uart` to change to [**UART**]({{< relref "/docs/command-reference/#uart" >}}) [mode]({{< relref "/docs/command-reference/#m-set-bus-mode" >}}).
If current data format is not 9600/8/n/1:
- 'n' to change communications parameters
- `9600` to select **9600** baud
- `8` to select **8** data bits
- `1` to select **None** parity
- `1` to select **1** stop bit
- `1` to select **None** hardware flow control
- `1` to select **Non-inverted** signal levels
#### Power supply setup
Most GPS modules operate at `3.3Volts`, but check the datasheet to be sure.

{{< termfile source="static/snippets/gps-power-setup.html" >}}

- `W 3.3` to turn on the Bus Pirate's power supply and set to **3.3** volts.  Current limit will be set to the default **300** milliamp current limit.

The power supply voltage and actual output current will be displayed

{{% alert context="warning" %}}

Verify actual voltage requirements to your GPS module and replace the `3.3` with the appropriate value!
{{% /alert %}}

## GPS command

{{< termfile source="static/snippets/gps-gps-command.html" >}} 

The [**gps**]({{< relref "/docs/command-reference/#gps-decoding-gps-nmea-sentences" >}}) command will set the UART to begin receiving sentences from the GPS module.  The Bus Pirate will decode the sentences as they come in.

Press any key to stop the command.

## NMEA sentence definitions
#### General
NMEA sentences begin with a `$` dollar sign, have one or more comma-delimited fields, and end with an optional checksum and `\r\n` return/newline combination.

There is repetition of data in the various sentences; many GPS modules can be configured to only transmit the desired sentences.  This is not intended to be a full primer on NMEA, but to define common sentences and how the Bus Pirate's `gps` command decodes them.

Partial list of NMEA sentences (this is not a comprehensive list)
|Message|Description|
|--|--|
|$GPGGA|Time, position, and fix type data|
|$GPGLL|Latitude, longtitude, UTC time of position fix and status|
|$GPGSA|GPS receiver mode, satellites used, DOP values|
|$GPGSV|Number of satellites in view, satellite ID, elevation, azimuth, and SNR|
|$GPRMC|Time, date, position, course, and speed data|
|$GPVTG|Course and speed relative to ground|

Format and example of each of those messages is given below
#### $GPGGA
Example `GGA` message from capture above:
```
$GPGGA,141458.00,4300.16985,N,08754.25421,W,1,06,1.38,190.7,M,-34.1,M,,*61
```
|Name|Value|Description|
|--|--|--|
|Message ID|$GPGGA|GGA header|
|UTC Time|141458.00|UTC time in hhmmss.ss format; 2:14:58.00 pm|
|Latitude|4300.16985|Latitude in the format of ddmm.mmmmm; 43° 00.16985'|
|N/S Indicator|N|N=north, S=South|
|Longitude|08754.25421|Longitude in the format of ddmm.mmmmm; 87° 54.25421'|
|E/W Indicator|W|E=east, W=west|
|Position Fix Indicator|1|0=fix not valid, 1=GPS SPS mode fix value, 2=Differential GPS SPS mode fix valid|
|Satellites used|06|range 0 to 12 satellites|
|HDOP|1.38|Horizontal dilution of precision|
|MSL altitude|190.7|Altitude above sea level (units below)|
|Units|M|units for MSL measurement; meters|
|Geoid separations|-34.1|Geoid-to-ellipsoid separation|
|Units|M|units for Geoid separation measurement; meters|
|Age of differential correction|(NULL)|Differential GPS correction in seconds|
|Differential station ID|(NULL}|Station ID|
|Checksum|0x61|checksum is the XOR of lower 7-bits of characters between `$` and `*`|
|`<CR><LF>`| |End of message terminator|

The Bus Pirate's `gps` command decodes this to display the fix quality:
```
$xxGGA: fix quality: 1
```
#### $GPGLL
Example `GLL` message from capture above:
```
$GPGLL,4300.16985,N,08754.25421,W,141458.00,A,A*7C
```
|Name|Value|Description|
|--|--|--|
|Message ID|$GPGLL|GLL header|
|Latitude|4300.16985|Latitude in the format of ddmm.mmmmm; 43° 00.16985'|
|N/S Indicator|N|N=north, S=South|
|Longitude|08754.25421|Longitude in the format of ddmm.mmmmm; 87° 54.25421'|
|E/W Indicator|W|E=east, W=west|
|UTC Time|141458.00|UTC time in hhmmss.ss format; 2:14:58.00 pm|
|Status|A|A=data valid, V=data not valid|
|Mode|A|A=autonomous, D=DGPS, E=DR|
|Checksum|0x7C|checksum is the XOR of lower 7-bits of characters between `$` and `*`|
|`<CR><LF>`| |End of message terminator|

The BUs Pirate's gps command does not decode this message

#### $GPGSA
Example `GGSA` message from capture above:
```
$GPGSA,A,3,23,10,24,32,18,15,,,,,,,2.62,1.38,2.23*07
```
|Name|Value|Description|
|--|--|--|
|Message ID|$GPGSA|GSA header|
|Mode 1|A|A=automatic (auto switch between 2D/3D), M=manual (forced to 2D or 3D)|
|Mode 2|3|1=fix not available, 2=2D( < 4 satellites), 3=3D( > 3 satellites)|
|Satellite used|23|Satallite ID on channel 1|
|Satellite used|10|Satallite ID on channel 2|
|Satellite used|24|Satallite ID on channel 3|
|Satellite used|32|Satallite ID on channel 4|
|Satellite used|18|Satallite ID on channel 5|
|Satellite used|15|Satallite ID on channel 6|
|Satellite used|(several NULLS)|Satallite ID on channel 7-12|
|PDOP|2.62|Position dilution of precision|
|HDOP|1.38|Horizontal dilution of precision|
|VDOP|2.23|Vertical dilution of precision|
|Checksum|0x07|checksum is the XOR of lower 7-bits of characters between `$` and `*`|
|`<CR><LF>`| |End of message terminator|

The Bus Pirate's gps command does not decode this message

#### $GPGSV
Example `GGSV` message from capture above:
```
$GPGSV,3,1,09,02,03,324,,08,13,301,14,10,58,314,24,15,17,062,22*71
```
|Name|Value|Description|
|--|--|--|
|Message ID|$GPGSV|GSV header|
|Number of messages|3|total number of `$GPGSV` messages for this fix|
|Message number|1|this message of total; 1 of 3|
|Satellites in view|9|Total number of satellites|
|Satellite ID|02|ID of channel 1 satellite|
|Elevation|03|Elevation [degrees] of channel 1 satellite|
|Azimuth|324|Azimuth [degrees] of channel 1 satellite|
|SNR|(NULL)|Signal-to-noise ratio [dBHz] of channel 1 satellite|
|Satellite ID|08|ID of channel 2 satellite|
|Elevation|13|Elevation [degrees] of channel 2 satellite|
|Azimuth|301|Azimuth [degrees] of channel 2 satellite|
|SNR|14|Signal-to-noise ratio [dBHz] of channel 2 satellite|
|Satellite ID|10|ID of channel 3 satellite|
|Elevation|58|Elevation [degrees] of channel 3 satellite|
|Azimuth|314|Azimuth [degrees] of channel 3 satellite|
|SNR|24|Signal-to-noise ratio [dBHz] of channel 3 satellite|
|Satellite ID|15|ID of channel 4 satellite|
|Elevation|17|Elevation [degrees] of channel 4 satellite|
|Azimuth|062|Azimuth [degrees] of channel 4 satellite|
|SNR|22|Signal-to-noise ratio [dBHz] of channel 4 satellite|
|Checksum|0x71|checksum is the XOR of lower 7-bits of characters between `$` and `*`|
|`<CR><LF>`| |End of message terminator|

The Bus Pirate's `gps` command decodes this to display the satellite info:
```
$xxGSV: message 1 of 3
$xxGSV: satellites in view: 9
$xxGSV: sat nr 2, elevation: 3, azimuth: 324, snr: 0 dbm
$xxGSV: sat nr 8, elevation: 13, azimuth: 301, snr: 14 dbm
$xxGSV: sat nr 10, elevation: 58, azimuth: 314, snr: 24 dbm
$xxGSV: sat nr 15, elevation: 17, azimuth: 62, snr: 22 dbm
```

#### $GPRMC
Example `RMC` message from capture above:
```
$GPRMC,141458.00,A,4300.16985,N,08754.25421,W,1.481,,151025,,,A*6B
```
|Name|Value|Description|
|--|--|--|
|Message ID|$GPRMC|RMC header|
|UTC Time|141458.00|UTC time in hhmmss.ss format; 2:14:58.00 pm|
|Status|A|A=data valid, V=data not valid|
|Latitude|4300.16985|Latitude in the format of ddmm.mmmmm; 43° 00.16985'|
|N/S Indicator|N|N=north, S=South|
|Longitude|08754.25421|Longitude in the format of ddmm.mmmmm; 87° 54.25421'|
|E/W Indicator|W|E=east, W=west|
|Speed over ground|1.481|speed of movement in knots|
|Course over ground|(NULL)|course in degrees|
|Date|151025|Date in ddmmyy; October 15th, 2025|
|Magnetic variation|(NULL)|degrees of variation|
|E/W Indicator|(NULL)|E=east, W=west|
|Mode|A|A=autonomous, D=DGPS, E=DR|
|Checksum|0x6b|checksum is the XOR of lower 7-bits of characters between `$` and `*`|
|`<CR><LF>`| |End of message terminator|

The Bus Pirate's `gps` command decodes this to:
```
$xxRMC: raw coordinates and speed: (430016985/100000,-875425421/100000) 1481/1000
$xxRMC fixed-point coordinates and speed scaled to three decimal places: (4300170,-8754254) 1481
$xxRMC floating point degree coordinates and speed: (43.002831,-87.904236) 1.481000
```
*Note - GPS module was stationary when this reading was taken*

#### $GPVTG
Example `VTG` message from capture above:
```
$GPVTG,,T,,M,1.481,N,2.744,K,A*2A
```
|Name|Value|Description|
|--|--|--|
|Message ID|$GPVTG|VTG header|
|Course|(NULL)|degrees measured heading|
|Reference|T|True north|
|Course|(NULL)|degrees measured heading|
|Reference|M|Magnetic north|
|Speed|1.481|Measured horizontal speed in knots|
|Units|N|Knots|
|Speed|2.744|Measured horizontal speed in k/h|
|Units|K|Kilometers per hour|
|Mode|A|A=autonomous, D=DGPS, E=DR|
|Checksum|0x2a|checksum is the XOR of lower 7-bits of characters between `$` and `*`|
|`<CR><LF>`| |End of message terminator|

The Bus Pirate's `gps` command decodes this to:
```
$xxVTG: true track degrees = nan
        magnetic track degrees = nan
        speed knots = 1.481000
        speed kph = 2.744000
```

## Open street map usage
The longitude/latitude data can be used to locate the GPS fix in [Open Street Maps](https://openstreetmap.org) by pasting the values into the search box in the upper left.  Southern latitudes and western longitudes should be entered as negative values:
![](images/docs/demo/gps-osm.png)

The map for the coordinates (43.002813, -87.904311) in the samples above:

{{< openstreetmap
x="43.002813"
y="-87.904311"
bbox="-87.90812373161317,43.000064904318585,-87.9004740715027,43.005596484095825" >}}
