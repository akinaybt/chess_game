import pygame
from piece import Piece

class Queen(Piece):
    def __init__(self, colour):
        super().__init__("queen", colour, 9.0)