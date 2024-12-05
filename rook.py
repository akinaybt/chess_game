import pygame
from piece import Piece

class Rook(Piece):
    def __init__(self, position, colour):
        super().__init__("rook", position, colour, 5.0)
