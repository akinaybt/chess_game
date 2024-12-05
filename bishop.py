import pygame
from piece import Piece

class Bishop(Piece):
    def __init__(self, colour):
        super().__init__("bishop", colour, 3.0)

    # def possible_moves(self, board):
        