import serial
import time
# replace with the USB port that you are connecting on 

device = 'COM3'

connection = serial.Serial(device, 1200)#, timeout=0, parity=serial.PARITY_EVEN, rtscts=1)

def write_delay(data, delay=0.5):
	connection.write(data.encode("ASCII"))
	time.sleep(delay)

def print_smiley(): 
	write_delay('\x13')
	write_delay('\x1F')

def advance_paper(): 
	# move paper up / cursor down
	for i in range (0, 10):
	    connection.write(b'\x75')
	    time.sleep(0.5)

def demo(): 
	advance_paper()
	print_smiley()
	advance_paper()

#TODO: use time parameter instead of fixed value
def alarm(time):
	connection.write(b"\xaa\xff")

def read():
	pass

#demo()

while True:
 	print(connection.read())
