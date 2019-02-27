import unittest
from erika.connect_to_erika import Erika

# TODO make parameter dynamic
COM_PORT = "COM3"


class ConnectTest(unittest.TestCase):
    def testConnect(self):
        """simple test that there is no exception when connecting"""
        with Erika(COM_PORT) as myErika:
            pass
        self.assertTrue(True)

    def testMovement(self):
        """simple test to test cursor movement - validation is manual check of cursor movement"""
        with Erika(COM_PORT) as myErika:
            myErika.move_down()
            myErika.move_right()
            myErika.move_up()
            myErika.move_left()
        self.assertTrue(True)


def main():
    unittest.main()

if __name__ == '__main__':
    main()
