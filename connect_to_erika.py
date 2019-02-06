import serial
import time
from string import ascii_lowercase
import json

# replace with the USB port that you are connecting on 

class Erika:

	conversion_table_path = "charTranslation.json"
	
	def __init__(self, com_port, *args, **kwargs):
		self.com_port = com_port
		self.connection = serial.Serial(com_port, 1200)#, timeout=0, parity=serial.PARITY_EVEN, rtscts=1)
		self.readConversionTable()
		self.ascii_2_ddr = {}
		self.ddr_2_ascii = {}
	
	def readConversionTable(self):
		"""read conversion table from file and populate 2 dicts"""	
		with open(self.conversion_table_path) as f:
			self.ascii_2_ddr = json.load(f)
		self.ddr_2_ascii = {value:key for key,value in ascii_2_ddr}

	def write_delay(self,data, delay=0.5):
		self.write_byte_delay(data.encode("ASCII"),delay)

	def write_byte_delay(self,data, delay = 0.5):
		self.connection.write(data)
		time.sleep(delay)

	def print_smiley(self): 
		self.write_delay('\x13')
		self.write_delay('\x1F')

	def advance_paper(self): 
		# move paper up / cursor down
		for i in range (0, 10):
			self.connection.write(b'\x75')
			time.sleep(0.5)

	def demo(self): 
		self.advance_paper()
		self.print_smiley()
		self.advance_paper()

	#TODO: use time parameter instead of fixed value
	def alarm(self,time):
		self.connection.write(b"\xaa\xff")

	def read():
		pass

	def print_ascii(self,text):
		for c in text:
			key_id = dict[c]
			self.write_byte_delay(key_id)

meine_erika = Erika("COM3")
meine_erika.demo()
meine_erika.alarm()
# demo()
# alarm(None)

# dict = {}
# for char in ascii_lowercase:
# 	dict[char] = connection.read()
# 	print(char)




