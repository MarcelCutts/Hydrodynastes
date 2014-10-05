"""
Defines the logic held in the board object. Its responsibilities include
displaying itself, arranging and maintaining ships, and knowing whether
or not it is in a "finished" or "playing" state.
"""

import pprint


class Board(object):

    def __init__(self, rows=5, columns=5):
        """
        Initialises new board object and sets
        the symbols, size of the board.
        Params:
            rows: Board's number of rows deep.
            coulumns: Boards number of columns wide.
        """
        self.unknown_space = "O"
        self.empty_space = "X"
        self.grid = self.__generate_grid(rows, columns)

    def display(self):
        current_row = "A"
        current_column = 1

        # Print the top board markers
        # Starting with a space and climbing alphabetically

        # Classic method
        current_row = "A"
        top_line = "   "
        for column in self.grid[0]:
            top_line += current_row + " "
            current_row = chr(ord(current_row)+1)
        print top_line

        # Functional method
        current_row = "A"
        letters = map(lambda x: chr(ord(current_row)+x), range(0, len(self.grid[0])))
        print "   " + " ".join(letters)

        # Both output "   A B C D E"
        for row in self.grid:
            print(str(current_column) + "| " + " ".join(row))
            current_column += 1

    def place_ship(ship):
        pass

    def is_board_still_in_play():
        pass

    def __print_board_state_as_string():
        pass

    def __generate_grid(self, rows, columns):
        """

        try:
            return [[self.unknown_space for x in xrange(columns)] for x in xrange(rows)]
        except ValueError:
            print("Grid rows and columns must be at least an integer of 1 in size")


