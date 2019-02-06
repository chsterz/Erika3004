import serial
import time
from string import ascii_lowercase
# replace with the USB port that you are connecting on 

device = 'COM3'

connection = serial.Serial(device, 1200)#, timeout=0, parity=serial.PARITY_EVEN, rtscts=1)

def write_delay(data, delay=0.5):
	write_byte_delay(data.encode("ASCII"),delay)

def write_byte_delay(data, delay = 0.5):
	connection.write(data)
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

def print_ascii(text):
	for c in text:
		key_id = dict[c]
		write_byte_delay(key_id)

# demo()
# alarm(None)

# dict = {}
# for char in ascii_lowercase:
# 	dict[char] = connection.read()
# 	print(char)


import pickle

# with open("charTranslation.pkl","wb") as outf:
# 	pickle.dump(dict, outf)
dict = {}
with open("charTranslation.pkl","rb") as inf:
	dict = pickle.load(inf)

# while True:
# 	tmp = connection.read()
# 	real_char = [key for key,value in dict.items() if value == tmp ]
# 	print(real_char)
# connection.close()

print_ascii("halloweltaufderschreibmaschine")