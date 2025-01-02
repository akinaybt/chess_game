from piece import Piece

class Knight(Piece):

    def __init__(self, colour):
        super().__init__("knight", colour, 3.0)
