import unittest

from tests.erika_mock import ErikaMock


def assert_print_output(test_case, my_erika, expected_array_of_joined_lines):
    for line in range(len(expected_array_of_joined_lines)):
        expected_line_joined = expected_array_of_joined_lines[line]
        expected_line = list(expected_line_joined)
        actual_line = my_erika.canvas[line]
        test_case.assertEqual(expected_line, actual_line)


class ErikaMockTest(unittest.TestCase):
    def testWriteBack(self):
        """simple test that the ErikaMock records what is written to it"""
        my_erika = ErikaMock(width=5, height=3)
        my_erika.print_ascii("Hello")
        my_erika.move_down()
        my_erika.move_down()
        my_erika.move_left()
        my_erika.move_left()
        my_erika.move_left()
        my_erika.print_ascii("!")
        my_erika.move_up()
        my_erika.move_left()
        my_erika.move_left()
        my_erika.move_left()
        my_erika.print_ascii("World")
        # my_erika.test_debug_helper_print_canvas()
        assert_print_output(self, my_erika, ["Hello", "World", "  !  "])


def main():
    unittest.main()


if __name__ == '__main__':
    main()
