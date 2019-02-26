# from erika.connect_to_erika import Erika

"""
Record any printing and movement calls to Erika in a 2D array for testing purposes: 

    x
    ===>
y ||
  ||
  \/

This way, rendering algorithms can be tested.
"""

"""ASSUMPTIONS: page dimensions for Erika"""
ERIKA_PAGE_WIDTH = 65
ERIKA_PAGE_HEIGHT = 150


# class ErikaMock(Erika):
class ErikaMock():  # Erika):

    def __init__(self, width=ERIKA_PAGE_WIDTH, height=ERIKA_PAGE_HEIGHT):
        self.canvas = []
        for y in range(height):
            new_list = []
            for x in range(width):
                new_list.append(" ")
            self.canvas.append(new_list)
        self.canvas_x = 0
        self.canvas_y = 0

    def __enter__(self):
        return self

    def __exit__(self, *args):
        pass

    def readConversionTable(self):
        pass

    def write_delay(self, data, delay=0.5):
        pass

    def write_byte_delay(self, data, delay=0.5):
        raise Exception('User is not supposed to call connection.write directly')

    def advance_paper(self):
        self.canvas_y += 10

    def alarm(self, time):
        pass

    def read(self):
        # reading not needed for current tests
        pass

    def print_ascii(self, text):
        for c in text:
            self.canvas[self.canvas_y][self.canvas_x] = c
            self.canvas_x += 1

    def print_raw(self, data):
        raise Exception('User is not supposed to call print_raw directly')

    def move_up(self):
        self.canvas_y -= 1

    def move_down(self):
        self.canvas_y += 1

    def move_left(self):
        self.canvas_x -= 1

    def move_right(self):
        self.canvas_x += 1

    def test_debug_helper_print_canvas(self):
        """for debugging: print the current canvas to stdout"""
        for line in self.canvas:
            print(line)
