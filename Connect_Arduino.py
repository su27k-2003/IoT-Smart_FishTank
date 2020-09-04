import serial
import time

while True:
	ser = serial.Serial('/dev/ttyUSB1',9600)
	# ser.write("b")
	time.sleep(1)
	data = ser.readline()
	print data
