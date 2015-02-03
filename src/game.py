
from boards.boards import PlayerBoard, AiBoard


class Game(object):
    """
    The main game class that holds the state of the game
    currently in play. Decides on turns, win conditions and
    delegates set up of the players on startup
    """
    
    def __init__(player_name):
    	"""
  		Sets up the game for a player vs AI match.
  		#TODO: Set up for a PvP match as an option
  		params: player_name - Name of the human player
  		"""

  		# Generate the boards
  		player_board = PlayerBoard(player_name='Joe')
  		Ai_board = AiBoard()





Game()




