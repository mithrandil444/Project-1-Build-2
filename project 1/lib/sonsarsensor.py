from machine import UART

uart = UART(1, 9600)
uart.init(9600, bits=8, parity=None, stop=1, timeout_chars=100, pins=('P3', 'P4'))

while True:
    header_bytes = uart.read(1)
    while(header_bytes != b'\xff'):
        header_bytes = uart.read(1)
    HIGH = int(uart.read(1)[0])
    LOW = int(uart.read(1)[0])
    SUM = int(uart.read(1)[0]) + 1

    if(HIGH + LOW == SUM):
        distance = (HIGH*256)+LOW
        print("Distance is: mm")
        print(distance)
