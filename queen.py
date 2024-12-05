import pygame
from piece import Piece

class Queen(Piece):
    def __init__(self, position, colour):
        super().__init__("queen", position, colour, 9.0)