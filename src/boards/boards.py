"""
Defines the logic held in the board object. Its responsibilities include
displaying itself, arranging and maintaining ships, and knowing whether
or not it is in a "finished" or "playing" state.
"""

import pprint


class Board(object):

    def __init__(self, player, rows=5, columns=5):
        """
        Initialises new board object and sets
        the symbols, size of the board.
        Params:
            rows: Board's number of rows deep.
            coulumns: Boards number of columns wide.
        """
        self.player = player
        self.unknown_space = "O"
        self.empty_space = "X"
        self.grid = self.__generate_grid(rows, columns)

    def display(self):
        current_row = "A"
        current_column = 1

        # Print the top board markers
        # Starting with a space and climbing alphabetically

        # Classic method
        top_line = "   "
        for column in self.grid[0]:
            top_line += current_row + " "
            current_row = chr(ord(current_row)+1)
        print top_line

        # Both output "   A B C D E"
        for row in self.grid:
            print(str(current_column) + "| " + " ".join(row))
            current_column += 1

    def place_ship(self, ship):
        pass

    def is_board_still_in_play(self):
        pass

    def __generate_grid(self, rows, columns):
        return [[self.unknown_space for x in xrange(columns)] for x in xrange(rows)]



class AiBoard(Board):

    def __init__(self, player):
        Board.__init__(self, player)
        self.attempted_locations = []

    def take_turn(self):
        """
        Takes a turn for the AI by randomly choosing a grid location
        Returns a 1x2 tuple
        """



        # Add location to attempted locations
        attempt_location = (row_location, column_location)
        if attempt_location in attempted_locations:
            self.take_turn()
        else:
            attempted_locations.append(attempt_location)

        print ("AI attempting " + str(attempt_location))
        return attempt_location


    def _generate_random_location():

        number_of_rows = len(self.grid)
        number_of_columns = len(self.gird[0])
        row_location = randint(0, number_of_rows - 1)
        column_location =randint(0, number_of_columns - 1)

        return (column_location, row_location)




