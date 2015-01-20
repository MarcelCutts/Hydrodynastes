__author__ = 'marcel'

import unittest
from boards import Board


class BoardTests(unittest.TestCase):
    def test_rows_on_square_board_generated_correctly(self):
        square_board = Board('testplayer', rows=2, columns=2)

        # Grid should be 2 long, 2 deep
        number_of_rows = len(square_board.grid)
        number_of_columns = len(square_board.grid[0])

        self.assertEqual(number_of_columns, 2)
        self.assertEqual(number_of_rows, 2)

    def test_rows_on_wide_board_generated_correctly(self):
        wide_board = Board('testplayer', rows=2, columns=6)

        # Grid should be 6 long, 2 deep
        number_of_rows = len(wide_board.grid)
        number_of_columns = len(wide_board.grid[0])

        self.assertEqual(number_of_columns, 6)
        self.assertEqual(number_of_rows, 2)


    def _generate_and_test_board_dimensions(expected_row_quantyt, expected_column_):
        pass
        # Oops getting off train



if __name__ == '__main__':
    unittest.main()
