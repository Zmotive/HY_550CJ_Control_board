# U-Blox Simple Translator for RTK
# Author: Zack Tokarczyk
#
# This Catches RTCM3 Messages (RTK offsets) and sends them to the machines. It also captures 
# Nav SVIN messages which is information on if the base station has set its reference point and
# Transmits only a subset of messages to the devices. 
#
# The Devices should receieve a message once per second so they will know if they do not have communication.
#
# This will also be used for collecting telemetery from  the devices and will need to be encrypted and
# compressed. This will be refactored later as a communication service.
#
# This is meant to be ran as a linux service with a simple service file and built into a package.
#
# Ublox documentation is here: https://content.u-blox.com/sites/default/files/LAP120_Interfacedescription_UBX-20046191.pdf

import serial
import bitstruct
import struct
from collections import namedtuple

Nav_SVIN = namedtuple('Nav_SVIN', [
        'header1',
        'header2',
        'uclass',
        'id',
        'len',
        'version',
        'iTOW',
        'dur',
        'meanX',
        'meanY',
        'meanZ',
        'meanXHP',
        'meanYHP',
        'meanZHP',
        'meanAcc',
        'obs',
        'valid',
        'active',
        'CK_A',
        'CK_B'
        ])

ser = serial.Serial('/dev/ttyACM0', 57200)  # GPS Set to Base station with learn position set
rem = serial.Serial('/dev/ttyUSB0', 57200)  # Radio Serial
rtcm3 = bytes()
rtcm3_len = 0
ublox = bytes()
ublox_len = 0

def process_ublox(msg: bytes) -> Nav_SVIN:
    return Nav_SVIN._make(struct.unpack('<BBBBHBxxxIIiiibbbxIIbbxxBB', msg))

while True:
    #Read a character at a time
    char = ser.read()

    #Standard Serial Msgs
    if char == b'$':
        line = char + ser.read_until()
        print(line)
        continue
        
    #RTCM3 Messages
    if char == b'\xd3': #RTCM3 Messages begin with 0xD3
        char += ser.read(2)
        data = bitstruct.unpack('u8u6u10', char) 
        rtcm3_len = data[2]
        rtcm3 = char + ser.read(rtcm3_len + 3)
        print(f'RTCM3: {rtcm3}')
        rem.write(rtcm3)
        rcm3 = bytes()
        continue
    
    #If we got here we need 2 chars to know if the message is something we can process.
    char += ser.read()
    #U-Blox Msgs
    if char == b'\xb5b':
        char += ser.read(4)
        swaplen = bitstruct.byteswap('2', char, 4)
        ublox_len = bitstruct.unpack('u16', swaplen)[0]
        ublox = char + ser.read(ublox_len + 2)
        msg = process_ublox(ublox)
        if msg.active == 0:
            rem.write(b'$NA\r\n') # Let the devices know that it isn't active
        if msg.valid == 0:
            rem.write(b'$I\r\n')  # Let the devices know that it isn't valid
        ublox = bytes()
        

