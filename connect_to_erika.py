import serial
import time
# replace with the USB port that you are connecting on 

device = '/dev/ttyACM0'

connection = serial.Serial(device, 1200, timeout=0, parity=serial.PARITY_EVEN, rtscts=1)

def print_smiley(): 
	connection.write(b'\x13')
	time.sleep(0.2)
	connection.write(b'\x1F')
	time.sleep(0.2)

def advance_paper(): 
	# move paper up / cursor down
	for i in range (0, 10):
	    connection.write(b'\x75')
	    time.sleep(0.2)

def demo(): 
	advance_paper()
	print_smiley()
	advance_paper()

demo()
