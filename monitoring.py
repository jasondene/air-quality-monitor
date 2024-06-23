import serial, time
from Adafruit_IO import Client
aio = Client(‘your-adafruit-username’, ‘your- adafruit-key’)
ser = serial.Serial(‘/dev/ttyUSB0’)

while True: data = []
for index in range(0,10): datum = ser.read() data.append(datum)
pmtwofive = int.from_bytes(b’’.join(data[2:4]), byteorder=’little’) / 10
aio.send(‘kingswoodtwofive’, pmtwofive)
pmten = int.from_bytes(b’’.join(data[4:6]), byteorder=’little’) / 10
aio.send(‘kingswoodten’, pmten) time.sleep(10)
