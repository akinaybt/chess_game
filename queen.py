from piece import Piece

class Queen(Piece):
    """Class Queen inherits from base class Piece"""
    def __init__(self, colour):
        super().__init__("queen", colour, 9.0)
