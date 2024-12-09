from const import *
from pawn import Pawn
from knight import Knight
from bishop import Bishop
from rook import Rook
from queen import Queen
from king import King
from square import Square
from piece import Piece

class Board:
    def __init__(self):
        self.squares = [[0, 0, 0, 0, 0, 0, 0, 0,] for col in range(COLS)]

        self._create()
        self._add_pieces('white')
        self._add_pieces('black')

    def _create(self):
        for row in range(ROWS):
            for col in range(COLS):
                self.squares[row][col] = Square(row, col)

    def _add_pieces(self, colour):
        row_pawn, row_other = (6, 7) if colour == 'white' else (1, 0)

        # row of pawns
        for col in range(COLS):
            self.squares[row_pawn][col] = Square(row_pawn, col, Pawn(colour))

        # knights
        for col in range(COLS):
            self.squares[row_other][1] = Square(row_other, 1, Knight(colour))
            self.squares[row_other][6] = Square(row_other, 6, Knight(colour))

        # bishops
        for col in range(COLS):
            self.squares[row_other][2] = Square(row_other, 2, Bishop(colour))
            self.squares[row_other][5] = Square(row_other, 5, Bishop(colour))

        # rooks
        for col in range(COLS):
            self.squares[row_other][0] = Square(row_other, 0, Rook(colour))
            self.squares[row_other][7] = Square(row_other, 7, Rook(colour))

        # queen
        for col in range(COLS):
            self.squares[row_other][3] = Square(row_other, 3, Queen(colour))

        # kings
        for col in range(COLS):
            self.squares[row_other][4] = Square(row_other, 4, King(colour))



