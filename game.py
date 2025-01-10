import pygame

from board import Board
from dragger import Dragger
from const import *
from config import Config
from square import Square


class Game:
    """
        Represents a game of chess and manages its visual representation, player turns, and gameplay elements.

        Attributes:
            next_player: Tracks the player whose turn it is to move ('white' or 'black').
            board: Board object representing the chessboard.
            dragger: Dragger object handles the logic for dragging and dropping chess pieces.
            config: Config object stores game configuration such as fonts and sounds.

        Methods:
            show_bg(surface):
            Method to draw the chessboard.
            show_pieces(surface):
            Method to draw the pieces on the board.
            show_moves(surface):
            Method to draw the possible moves for the currently dragged piece.
            show_last_move(surface):
            Method to draw the last move made on the board.
            next_turn():
            Method to switch to the next player's turn.
            play_sound(captured=False):
            Method to play a sound based on the captured or made move.
    """
    def __init__(self):
        self.next_player = 'white'
        self.board = Board()
        self.dragger = Dragger()
        self.config = Config()

    def show_bg(self, surface):
        """Method to draw the chessboard."""
        for row in range(ROWS):
            for col in range(COLS):
                if (row +col ) % 2 == 0:
                    colour = (255, 255, 255) #white
                else:
                    colour = (0,0,0) #black

                rect =(col * SQSIZE, row * SQSIZE, SQSIZE, SQSIZE)

                pygame.draw.rect(surface, colour, rect)

                if col == 0:
                    colour = (0, 0, 0) if row % 2 == 0 else (255, 255, 255)
                    label = self.config.font.render(str(ROWS - row), 1, colour)
                    label_position = (5, 5 + row * SQSIZE)
                    surface.blit(label,  label_position)
                if row == 7:
                    colour = (0, 0, 0) if (row + col) % 2 == 0 else (255, 255, 255)
                    label = self.config.font.render(Square.get_alphabet(col), 1, colour)
                    label_position = (col * SQSIZE + SQSIZE - 19, HEIGHT - 19)
                    surface.blit(label, label_position)

    def show_pieces(self, surface):
        """Method to draw the pieces on the board."""
        for row in range(ROWS):
            for col in range(COLS):
                if self.board.squares[row][col].has_piece():
                    piece = self.board.squares[row][col].piece

                    if piece is not self.dragger.piece:
                        img = pygame.image.load(piece.image_url)
                        img_center = col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2
                        piece.image_rect = img.get_rect(center=img_center)
                        surface.blit(img, piece.image_rect)

    def show_moves(self, surface):
        """Method to draw the possible moves for the currently dragged piece."""
        if self.dragger.dragging:
            piece = self.dragger.piece

            for move in piece.moves:
                colour = "#f03f32" if (move.final.row + move.final.col) % 2 == 0 else "#d12e21"
                rect = (move.final.col * SQSIZE, move.final.row * SQSIZE, SQSIZE, SQSIZE)

                pygame.draw.rect(surface, colour, rect)

    def show_last_move(self, surface):
        """Method to draw the last move made on the board."""
        if self.board.last_move:
            initial = self.board.last_move.initial
            final = self.board.last_move.final

            for pos in [initial, final]:
                colour = (244, 247, 116) if (pos.row + pos.col) % 2 == 0 else (172, 195, 151)
                rect = (pos.col * SQSIZE, pos.row * SQSIZE, SQSIZE, SQSIZE)

                pygame.draw.rect(surface, colour, rect)

    def next_turn(self):
        """Method to switch to the next player's turn.'"""
        self.next_player = 'black' if self.next_player == 'white' else 'white'

    def play_sound(self, captured=False):
        """Method to play a sound based on the captured or made move."""
        if captured:
            self.config.capture_sound.play()
        else:
            self.config.move_sound.play()