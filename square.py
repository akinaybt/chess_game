class Square:

    ALPHABET = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H'}

    def __init__(self, row, col, piece=None):
        self.row = row
        self.col = col
        self.piece = piece
        self.alphabet = self.ALPHABET[col]

    def __eq__(self, other):
        return self.row == other.row and self.col == other.col

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

    @staticmethod
    def get_alphabet(col):
        ALPHABET = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H'}
        return ALPHABET[col]