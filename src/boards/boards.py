"""
Defines the logic held in the board object. Its responsibilities include
displaying itself, arranging and maintaining ships, and knowing whether
or not it is in a "finished" or "playing" state.
"""

import pprint


class BaseBoard(object):
    """
    Base board object storing key attributes, properties and methods
    that are to be used by all board types that wil be played in the game
    """

    def __init__(self, player, columns=5, rows=5):
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
        self.shipe_space = "S"
        self.grid = self.__generate_grid(columns=columns, rows=rows)

    def display(self):
        """
        Prints (prettily) an ASCII-style representation of the
        game board, featuring current state of play on a particular
        board as defined by the internal grid variable.
        Returns: 
            ASCII-style board as string to display
        """
        current_row = "A"
        current_column = 1

        # Decided to use a simpler-to-read loop here as opposed to 
        # a higher order functional approach, as it was terrible to read
        # This prints the letters at the top of the grid denoting location
        top_line = "   "
        for column in self.grid[0]:
            top_line += current_row + " "
            current_row = chr(ord(current_row)+1)
        print top_line

        # Print the numbers on the left column of the grid
        for row in self.grid:
            print(str(current_column) + "| " + " ".join(row))
            current_column += 1
 

    def is_board_still_in_play(self):
        """
        Checks whether a board is still in play by checking whether
        any grid position still holds a ship. If any ship is still 
        found, the board is still in play.
        :returns: True if still in play, else False
        """
        for row in self.grid:
            if row.contains(self.shipe_space):
                return True

        return False    

    def __generate_grid(self, columns, rows):
        """
        Creates the internal grid which act similar to squares 
        or individual playing spaces on a game board. As a collective
        these make up the board or play-space for a player. A list
        comprehension within a list comprehension is used. The initial
        comprehension is the "width" or "column" while how many of those
        generated constitute the "height" or "rows.
        Returns:
            Nested lists representing playing field.
        """
        return [[self.unknown_space for x in xrange(columns)] 
                for x 
                in xrange(rows)]


class AiBoard(Board):
    """
    Holds the state of the AI player's board, and exposes methods to progress it
    """

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


class PlayerBoard(BaseBoard):
    """
    Board containing state and methods to act upon the board by a player
    """

    def __init__(self):
        """
        """
        pass



