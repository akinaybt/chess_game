import pygame
from pygame import display, mouse

from const import *
from move import Move
from move_operations import CalculateMoves
from pawn import Pawn
from knight import Knight
from bishop import Bishop
from rook import Rook
from queen import Queen
from king import King
from square import Square
from button import Button

class Board:
    """
       Represents the chessboard for the game, managing its state and providing utility methods
       for game actions such as moves, castling, pawn promotion, and piece placement.

       Attributes:
           screen : The display surface for the chessboard.
           squares : A list representing the squares of the chessboard, each holding a Square object.
           last_move: The last move made on the board.
           fill : Background color for the chessboard.

       Methods:
           check_promotion(piece, final):
               Handles the logic for pawn promotion when a pawn reaches the last rank.
           castling(initial, final):
               Checks if a move qualifies as a castling move.
           move(piece, move):
               Executes a move on the board, updating its state.
           valid_move(piece, move):
               Validates whether a given move is legal for a piece.
           _create():
               Initializes the board by creating square objects for each position.
           _add_pieces(colour):
               Places pieces on the board for the specified color ('white' or 'black').
       """
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.squares = [[0, 0, 0, 0, 0, 0, 0, 0] for col in range(COLS)]
        self.last_move = None
        self._create()
        self._add_pieces('white')
        self._add_pieces('black')
        self.fill = (0, 0, 0)
        self.boardhistoryhashes = []

    def check_promotion(self, piece, final):
        """The function handles pawn promotion logic."""
        if final.row == 0 or final.row == 7:
            promotion_screen = True

            BUTTON_QUEEN = Button(180, 180, 160, 160, (255, 250, 250),
                                  (255, 255, 255), "monospace", (0, 0, 0), "Queen")
            BUTTON_ROOK = Button(350, 180, 160, 160, (255, 255, 255),
                                 (255, 255, 255), "monospace", (0, 0, 0), "Rook")
            BUTTON_BISHOP = Button(180, 350, 160, 170, (255, 255, 255),
                                   (255, 255, 255), "monospace", (0, 0, 0), "Bishop")
            BUTTON_KNIGHT = Button(350, 350, 160, 170, (255, 255, 255),
                                   (255, 255, 255), "monospace", (0, 0, 0), "Knight")

            while promotion_screen:
                self.screen.fill((0, 0, 0))
                BUTTON_QUEEN.showButton(self.screen)
                BUTTON_ROOK.showButton(self.screen)
                BUTTON_BISHOP.showButton(self.screen)
                BUTTON_KNIGHT.showButton(self.screen)

                mouse_pos = mouse.get_pos()
                mouse_click = mouse.get_pressed()

                if BUTTON_QUEEN.focusCheck(mouse_pos, mouse_click):
                    self.squares[final.row][final.col].piece = Queen(piece.colour)
                    promotion_screen = False
                elif BUTTON_ROOK.focusCheck(mouse_pos, mouse_click):
                    self.squares[final.row][final.col].piece = Rook(piece.colour)
                    promotion_screen = False
                elif BUTTON_BISHOP.focusCheck(mouse_pos, mouse_click):
                    self.squares[final.row][final.col].piece = Bishop(piece.colour)
                    promotion_screen = False
                elif BUTTON_KNIGHT.focusCheck(mouse_pos, mouse_click):
                    self.squares[final.row][final.col].piece = Knight(piece.colour)
                    promotion_screen = False

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()

                display.update()


    def castling(self, initial, final):
        """The function checks if the move is a castling move."""
        return abs(initial.col - final.col) == 2

    def check(self, piece, move):
        pass

    def move(self, piece, move):
        """The function executes a move on the board."""
        initial = move.initial
        final = move.final

        # Console board move update
        self.squares[initial.row][initial.col].piece = None
        self.squares[final.row][final.col].piece = piece

        # Pawn promotion
        if isinstance(piece, Pawn):
            self.check_promotion(piece, final)


        # King castling
        if isinstance(piece, King):
            if self.castling(initial, final):
                #If castling to the left, rook is on initial.col 0
                if move.final.col == 2:  # Correct condition for left castling
                    rook = piece.left_rook
                    rook_move = Move(Square(initial.row, 0), Square(final.row, final.col + 1))
                #If castling to the right, rook is on initial.col 7
                if move.final.col == 6:
                    rook = piece.right_rook
                    rook_move = Move(Square(initial.row, 7), Square(final.row, final.col - 1))

                self.squares[rook_move.initial.row][rook_move.initial.col].piece = None
                self.squares[rook_move.final.row][rook_move.final.col].piece = rook
                rook.made_move = True

        piece.made_move = True

        piece.clear_moves()

        self.last_move = move

    def valid_move(self, piece, move):
        """The function checks if a move is valid."""
        if not move in piece.moves:
            return False

        if not Square.is_within_bounds(move.final.row, move.final.col):
            return False
        # Basic check - prevent moving to a square with a friendly piece
        if self.squares[move.final.row][move.final.col].piece and self.squares[move.final.row][move.final.col].piece.colour == piece.colour:
            return False
        return True

    def _create(self):
        """The function creates the board squares."""
        for row in range(ROWS):
            for col in range(COLS):
                self.squares[row][col] = Square(row, col)

    def _add_pieces(self, colour):
        """The function adds pieces to the board."""
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

    def get_king(self, colour):
        for row in self.squares:
            for square in row:
                piece = square.piece
                if isinstance(piece, King) and piece.colour == colour:
                    return piece
        raise ValueError(f"King of colour {colour} not found on the board")

    @staticmethod
    def game_over(self):
        """checks if the game is over."""
        try:
            self.get_king(colour="white")
            self.get_king(colour="black")
        except ValueError:
            return True
        return False