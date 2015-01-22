__author__ = 'marcel'

import unittest
from boards import Board


class BoardTests(unittest.TestCase):
    def test_grid_on_square_board_generated_correctly(self):
        square_board = self._generate_and_test_board_dimensions(expected_column_quantity=2,
                                                                expected_row_quantity=2)

    def test_grid_on_wide_board_generated_correctly(self):
        wide_board = self._generate_and_test_board_dimensions(expected_column_quantity=6,
                                                              expected_row_quantity=2)

    def test_grid_on_tall_board_generated_correctly(self):
        tall_board = self._generate_and_test_board_dimensions(expected_column_quantity=2,
                                                              expected_row_quantity=6)

    def _generate_and_test_board_dimensions(self, expected_column_quantity, expected_row_quantity):
        test_board = Board('testplayer', rows=expected_column_quantity, columns=expected_column_quantity)

        # Grid should match the column, row values from arguments
        number_of_rows = len(test_board.grid)
        number_of_columns = len(test_board.grid[0])

        self.assertEqual(number_of_columns, expected_column_quantity)
        self.assertEqual(number_of_rows, expected_row_quantity)




if __name__ == '__main__':
    unittest.main()
