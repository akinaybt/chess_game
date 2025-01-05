from const import *
from pawn import Pawn
from knight import Knight
from bishop import Bishop
from rook import Rook
from queen import Queen
from king import King
from square import Square

class Board:
    def __init__(self):
        self.squares = [[0, 0, 0, 0, 0, 0, 0, 0] for col in range(COLS)]
        self.last_move = None
        self._create()
        self._add_pieces('white')
        self._add_pieces('black')

    def move(self, piece, move):
        initial = move.initial
        final = move.final

        # console board move update
        self.squares[initial.row][initial.col].piece = None
        self.squares[final.row][final.col].piece = piece

        piece.made_move = True

        piece.clear_moves()

        self.last_move = move

    def valid_move(self, piece, move):
        if not move in piece.moves:
            return False
        if not Square.is_within_bounds(move.final.row, move.final.col):
            return False
        # Basic check - prevent moving to a square with a friendly piece
        if (self.squares[move.final.row][move.final.col].piece and
                self.squares[move.final.row][move.final.col].piece.colour == piece.colour):
            return False
        return True

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
        self.squares[row_other][1] = Square(row_other, 1, Knight(colour))
        self.squares[row_other][6] = Square(row_other, 6, Knight(colour))

        # bishops
        self.squares[row_other][2] = Square(row_other, 2, Bishop(colour))
        self.squares[row_other][5] = Square(row_other, 5, Bishop(colour))

        # rooks
        self.squares[row_other][0] = Square(row_other, 0, Rook(colour))
        self.squares[row_other][7] = Square(row_other, 7, Rook(colour))

        # queens
        self.squares[row_other][3] = Square(row_other, 3, Queen(colour))

        # kings
        self.squares[row_other][4] = Square(row_other, 4, King(colour))
