import pygame
from piece import Piece

class Bishop(Piece):
    def __init__(self, position, colour):
        super().__init__("bishop", position, colour, 3.0)

    def possible_moves(self, board):
        