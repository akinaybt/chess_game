import pygame
from piece import Piece

class Rook(Piece):
    def __init__(self, colour):
        super().__init__("rook", colour, 5.0)
