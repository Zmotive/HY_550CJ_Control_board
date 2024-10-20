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

ser = serial.Serial('/dev/ttyACM0', 57200)
rem = serial.Serial('/dev/ttyUSB0', 57200)
rtcm3 = bytes()
rtcm3_len = 0
ublox = bytes()
ublox_len = 0

def process_ublox(msg: bytes) -> Nav_SVIN:
    return Nav_SVIN._make(struct.unpack('<BBBBHBxxxIIiiibbbxIIbbxxBB', msg))

while True:
    char = ser.read()

    #Standard Serial Msgs
    if char == b'$':
        line = char + ser.read_until()
        print(line)
        continue
        
    #RTCM3 Messages
    if char == b'\xd3':
        char += ser.read(2)
        data = bitstruct.unpack('u8u6u10', char)
        rtcm3_len = data[2]
        rtcm3 = char + ser.read(rtcm3_len + 3)
        print(f'RTCM3: {rtcm3}')
        rem.write(rtcm3)
        rcm3 = bytes()
        continue

    char += ser.read()
    #U-Blox Msgs
    if char == b'\xb5b':
        char += ser.read(4)
        swaplen = bitstruct.byteswap('2', char, 4)
        ublox_len = bitstruct.unpack('u16', swaplen)[0]
        ublox = char + ser.read(ublox_len + 2)
        msg = process_ublox(ublox)
        if msg.active == 0:
            rem.write(b'$NA\r\n')
        if msg.valid == 0:
            rem.write(b'$I\r\n')
        ublox = bytes()
        

