from piece import Piece

class Rook(Piece):
    """Class Rook inherits from base class Piece."""
    def __init__(self, colour):
        super().__init__("rook", colour, 5.0)
