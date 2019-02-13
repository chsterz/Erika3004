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
		self.ascii_2_ddr = {}
		self.ddr_2_ascii = {}
		self.readConversionTable()

	def __enter__(self):
		return self
		#self.connection.open()

	def __exit__(self, *args):
		self.connection.close()
	
	def readConversionTable(self):
		"""read conversion table from file and populate 2 dicts"""	
		with open(self.conversion_table_path,encoding="UTF-8") as f:
			self.ascii_2_ddr = json.load(f)
		self.ddr_2_ascii = {value:key for key,value in self.ascii_2_ddr.items()}

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

	def read(self):
		key_id = self.connection.read()
		return self.ddr_2_ascii[key_id.hex()]

	def print_ascii(self,text):
		for c in text:
			key_id = self.ascii_2_ddr[c]
			self.write_byte_delay(key_id)


with Erika("COM3") as meine_erika:
	# meine_erika.demo()
	# meine_erika.alarm(None)
	
	meine_erika.print_ascii(input("Geben Sie Text ein:"))




