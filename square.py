class Square:
    def __init__(self, row, col, piece=None):
        self.row = row
        self.col = col
        self.piece = piece

    def __eq__(self, other):
        return self.row == other.row and self.col == other.col and self.piece == other.piece

    def has_piece(self):
        return self.piece != None

    def is_empty(self):
        return not self.has_piece()

    def has_team_piece(self, colour):
        return self.has_piece() and self.piece.colour == colour

    def has_rival_piece(self, colour):
        return self.has_piece() and self.piece.colour != colour


    def empty_or_rival(self, colour):
        return self.is_empty() or self.has_rival_piece(colour)

    @staticmethod
    def is_within_bounds(*args):
        for arg in args:
            if arg < 0 or arg > 7:
                return False
        return True
