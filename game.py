#screen
import pygame

from board import Board
from const import *
class Game:
    def __init__(self):
        self.board = Board()

    def show_bg(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                if (row +col ) % 2 == 0:
                    colour = (255, 255, 255) #white
                else:
                    colour = (0,0,0) #black

                rect =(col * SQSIZE, row * SQSIZE, SQSIZE, SQSIZE)

                pygame.draw.rect(surface, colour, rect)
    def show_pieces(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                if self.board.squares[row][col].has_piece():
                    piece = self.board.squares[row][col].piece

                    img = pygame.image.load(piece)
                    img = col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2

                    surface.blit(img, img)