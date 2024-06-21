import serial
import time

# Function to write data to a file
def write_to_file(filename, pmtwofive, pmten):
    with open(filename, 'a') as file:
        file.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')}, PM2.5: {pmtwofive}, PM10: {pmten}\n")

# Initialize serial connection
ser = serial.Serial('/dev/ttyUSB0')

while True:
    data = []
    
    # Read 10 bytes from the serial port
    for index in range(0, 10):
        datum = ser.read()
        data.append(datum)
    
    # Extract PM2.5 data
    pmtwofive = int.from_bytes(b''.join(data[2:4]), byteorder='little') / 10
    # Extract PM10 data
    pmten = int.from_bytes(b''.join(data[4:6]), byteorder='little') / 10
    
    # Write the data to a file
    write_to_file('sensor_data.txt', pmtwofive, pmten)
    
    # Wait for 10 seconds before the next reading
    time.sleep(10)
