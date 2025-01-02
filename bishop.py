from piece import Piece

class Bishop(Piece):
    def __init__(self, colour):
        super().__init__("bishop", colour, 3.0)
