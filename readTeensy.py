import serial
import csv   
f = open("logfile.txt", "wb")


with serial.Serial('/dev/tty.usbmodem70062901', baudrate=2000000, timeout=1) as ser:
	# read 10 lines from the serial output
	lastTime = 0
	print('Begin Samples')
	for i in range(100000):
		try:
			line = ser.read(10)
			# print(line[5])
			f.write(line)
		except Exception as E:
			print(E)


f.close()