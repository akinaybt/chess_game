import pygame
from piece import Piece

class Pawn(Piece):
    def __init__(self, colour, position=None):
        self.colour = colour
        self.direction = -1 if self.colour == 'white' else  1
        super().__init__('pawn', position, colour, 1.0)
