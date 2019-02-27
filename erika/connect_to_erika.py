#%%
import serial
import time
from string import ascii_lowercase
import json


# replace with the USB port that you are connecting on

class Erika:
	conversion_table_path = "charTranslation.json"

	def __init__(self, com_port, *args, **kwargs):
		self.com_port = com_port
		self.connection = serial.Serial(com_port, 1200)  # , timeout=0, parity=serial.PARITY_EVEN, rtscts=1)
		self.ascii_2_ddr = {}
		self.ddr_2_ascii = {}
		self.readConversionTable()

	def __enter__(self):
		return self

	# self.connection.open()

	def __exit__(self, *args):
		self.connection.close()

	def readConversionTable(self):
		"""read conversion table from file and populate 2 dicts"""
		with open(self.conversion_table_path, encoding="UTF-8") as f:
			self.ascii_2_ddr = json.load(f)
		self.ddr_2_ascii = {value: key for key, value in self.ascii_2_ddr.items()}

	def write_delay(self, data, delay=0.5):
		self.write_byte_delay(data.encode("ASCII"), delay)

	def write_byte_delay(self, data, delay=0.5):
		self.connection.write(bytes.fromhex(data))
		time.sleep(delay)

	def print_smiley(self):
		self.write_delay('\x13')
		self.write_delay('\x1F')

	def advance_paper(self):
		# move paper up / cursor down
		for i in range(0, 10):
			self.connection.write(b'\x75')
			time.sleep(0.5)

	def demo(self):
		self.advance_paper()
		self.print_smiley()
		self.advance_paper()

	# TODO: use time parameter instead of fixed value
	def alarm(self, time):
		self.connection.write(b"\xaa\xff")

	def read(self):
		key_id = self.connection.read()
		return self.ddr_2_ascii.get(key_id.hex().upper(),key_id.hex())

	def print_ascii(self, text):
		for c in text:
			key_id = self.ascii_2_ddr[c]
			self.write_byte_delay(key_id)

	def print_raw(self, data):
		self.connection.write(bytes.fromhex(data))

	def move_up(self):
		self.print_raw("76")
		self.print_raw("76")

	def move_down(self):
		self.print_raw("75")
		self.print_raw("75")

	def move_left(self):
		self.print_raw("74")
		self.print_raw("74")

	def move_right(self):
		self.print_raw("73")
		self.print_raw("73")

	def crlf(self):
		self.print_raw("78")
		self.print_raw("9F")



with Erika("COM3") as meine_erika:
	meine_erika.print_ascii("Hallo")
	# meine_erika.print_ascii("#")
	# meine_erika.move_up()
	# meine_erika.move_up()
	# meine_erika.print_ascii("^")
	# meine_erika.move_right()
	# meine_erika.move_right()
	# meine_erika.print_ascii("#")
	# meine_erika.move_right()
	# meine_erika.move_right()
	# meine_erika.print_ascii("#")

	# meine_erika.move_down()
	# meine_erika.move_down()
	# meine_erika.print_ascii("#")

	# meine_erika.move_left()
	# meine_erika.move_left()

	# meine_erika.move_left()
	# meine_erika.move_left()
	# meine_erika.print_ascii("#")


	#meine_erika.demo()
#     # meine_erika.alarm(None)
# 	meine_erika.print_ascii("\r")
#     #meine_erika.print_ascii(input("Geben Sie Text ein:"))
# 	while True:
# 	 	print(meine_erika.read())#, end='', flush=True)
#%%
# with open("charTranslation.json", encoding="UTF-8") as f:
#            test = json.load(f)

#%%
