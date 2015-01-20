__author__ = 'marcel'

import unittest
from .boards import Board


class BoardTests(unittest.TestCase):
    def test_rows_generated_correctly(self):
        square_board = Board('testplayer', rows=4, columns=4)

        # Grid should be 2 long, 2 deep
        number_of_rows = len()


if __name__ == '__main__':
    unittest.main()
