import pygame
from piece import Piece

class King(Piece):
    def __init__(self, position, colour):
        super().__init__("king", position, colour, 100.0)
