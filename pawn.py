import pygame
from piece import Piece

class Pawn(Piece):
    def __init__(self, position, colour):
        if colour == 'white':
            self.direction = -1
        else:
            self.direction = 1
        super().__init__('pawn', position, colour, 1.0)
