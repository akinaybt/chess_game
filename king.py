from piece import Piece

class King(Piece):
    """Class King inherits from base class Piece."""
    def __init__(self, colour):
        self.left_rook = None
        self.right_rook = None
        super().__init__("king", colour, 100.0)
