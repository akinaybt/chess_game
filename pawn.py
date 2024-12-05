import pygame
from piece import Piece

class Pawn(Piece):
    def __init__(self, colour, position=None):
        self.direction = -1 if self.colour == 'white' else self.direction = 1
        super().__init__('pawn', position, colour, 1.0)
