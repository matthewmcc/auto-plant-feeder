import serial
import os.path

from datetime import datetime

ser = serial.Serial('/dev/ttyUSB0',9600)

while True:
	read_serial = ser.readline()
	readTime = datetime.now()
	newReadsFilename = str(readTime.date()) + ".txt"

	if (not os.path.isfile(newReadsFilename)):
		open(newReadsFilename, 'w+').close()

	with open(newReadsFilename, "a") as outputFile:
		outputFile.write(read_serial.rstrip() + ", Time: " + str(datetime.now()))
		outputFile.write("\n")
