class Square:
    """
        Representation of chess squares.

        Attributes:
            row : The row index of the square.
            col : The column index of the square.
            piece : The piece on the square.
            alphabet : The alphabetic representation of the square.

        Methods:
            has_piece():
            Checks if the square has a piece.
            is_empty():
            Checks if the square is empty.
            has_team_piece(colour):
            Checks if the square has a piece of the given colour.
            has_rival_piece(colour):
            Checks if the square has a piece of the opposite colour.
            empty_or_rival(colour):
            Checks if the square is empty or has a piece of the opposite colour.
            is_within_bounds(*args):
            Checks if the given arguments are within the bounds of the board.
            get_alphabet(col):
            Method to get the alphabetic representation of a column index.
    """
    ALPHABET = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H'}

    def __init__(self, row, col, piece=None):
        self.row = row
        self.col = col
        self.piece = piece
        self.alphabet = self.ALPHABET[col]

    def __eq__(self, other):
        return self.row == other.row and self.col == other.col and self.piece == other.piece

    def has_piece(self):
        """Checks if the square has a piece."""
        return self.piece is not None

    def is_empty(self):
        """Checks if the square is empty."""
        return not self.has_piece()

    def has_team_piece(self, colour):
        """Checks if the square has a piece of the given colour."""
        return self.has_piece() and self.piece.colour == colour

    def has_rival_piece(self, colour):
        """Checks if the square has a piece of the opposite colour."""
        return self.has_piece() and self.piece.colour != colour


    def empty_or_rival(self, colour):
        """Checks if the square is empty or has a piece of the opposite colour."""
        return self.is_empty() or self.has_rival_piece(colour)

    @staticmethod
    def is_within_bounds(*args):
        """Checks if the given arguments are within the bounds of the board."""
        for arg in args:
            if arg < 0 or arg > 7:
                return False
        return True

    @staticmethod
    def get_alphabet(col):
        """Method to get the alphabetic representation of a column index."""
        ALPHABET = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H'}
        return ALPHABET[col]