import pygame
from piece import Piece

class King(Piece):
    def __init__(self, colour):
        super().__init__("king", colour, 100.0)
