import unittest
from erika.erika_image_renderer import *
from tests.erika_mock import *


class RendererTest(unittest.TestCase):
    def testRenderLineByLineConnect(self):
        """simple test that printing line by line works"""
        with ErikaMock(6, 6) as my_erika:
            rendering_strat = LineByLineErikaImageRenderingStrategy()
            renderer = ErikaImageRenderer(my_erika, rendering_strat)
            renderer.renderAsciiArtFile('/home/hoobert/Documents/machBar/repos/Erika3004/tests/test_resources/test_ascii_art_small.txt')
            self.assertPrintOutput(my_erika,
                                   ["abcdef", "ghijkl", "mnopqr", "stuvwx", "yzäöüß", "!?#'\"/"])


    # TODO extract test util + DRY code
    def assertPrintOutput(self, my_erika, expected_array_of_joined_lines):
        for line in range(len(expected_array_of_joined_lines)):
            expected_line_joined = expected_array_of_joined_lines[line]
            expected_line = list(expected_line_joined)
            actual_line = my_erika.canvas[line]
            self.assertEqual(expected_line, actual_line)


def main():
    unittest.main()

if __name__ == '__main__':
    main()
