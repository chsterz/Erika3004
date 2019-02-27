import unittest

from erika.erika_image_renderer import *
from tests.erika_mock import *
from tests.erika_mock_unittest import assert_print_output


class RendererTest(unittest.TestCase):
    def testRenderLineByLineConnect(self):
        """simple test that printing line by line works"""
        with ErikaMock(6, 6) as my_erika:
            rendering_strat = LineByLineErikaImageRenderingStrategy()
            renderer = ErikaImageRenderer(my_erika, rendering_strat)
            renderer.render_ascii_art_file('tests/test_resources/test_ascii_art_small.txt')
            assert_print_output(self, my_erika, ["abcdef", "ghijkl", "mnopqr", "stuvwx", "yzäöüß", "!?#'\"/"])


def main():
    unittest.main()


if __name__ == '__main__':
    main()
