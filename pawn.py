from piece import Piece

class Pawn(Piece):
    def __init__(self, colour):
        self.colour = colour
        self.direction = -1 if self.colour == 'white' else  1
        # self.en_passant = False
        super().__init__('pawn', colour, 1.0)
