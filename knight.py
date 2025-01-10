from piece import Piece

class Knight(Piece):
    """Class Knight inherits from base class Piece."""
    def __init__(self, colour):
        super().__init__("knight", colour, 3.0)
