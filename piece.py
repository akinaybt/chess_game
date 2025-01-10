import os

class Piece:
    """
        Represents a chess piece, including its attributes, state, and functionality
        related to moves and images.

        Attributes:
            name : The name of the piece (e.g., 'pawn', 'rook').
            colour : The color of the piece ('white' or 'black').
            value : The point value of the piece, used in game logic.
            image_url : The file path to the image representing the piece.
            image_rect : The rectangle object for the piece's image, used for positioning.
            moves : A list of valid moves available to the piece.
            made_move : Indicates if the piece has made a move during the game.

        Methods:
            set_image_url():
                Sets the image URL for the piece based on its color and name.
            add_move(move):
                Adds a valid move to the piece's list of moves.
            clear_moves():
                Clears the list of valid moves for the piece.
        """
    def __init__(self, name, colour, value, image_url=None, image_rect=None):
        self.name = name
        self.colour = colour
        self.value = value
        self.image_url = image_url
        self.set_image_url()
        self.moves = []
        self.made_move = False
        self.image_rect = image_rect

    def set_image_url(self):
        """Sets the image URL for the piece based on its color and name."""
        self.image_url = os.path.join(
            f'imgs/{self.colour}_{self.name}.png'
        )

    def add_move(self, move):
        """Adds a valid move to the piece's list of moves."""
        self.moves.append(move)

    def clear_moves(self):
        """Clears the list of valid moves for the piece."""
        self.moves = []
