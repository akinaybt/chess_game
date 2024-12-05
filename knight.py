import pygame
from piece import Piece

class Knight(Piece):
    def __init__(self, colour):
        super().__init__("knight", colour, 3.0)

    def possible_moves(self, board):
        moves = []
        knight_moves = [
            (2, 1), (2, -1),
            (-2, 1), (-2, -1),
            (-1, 2), (-1, -2),
            (1, 2), (1, -2),
        ]

        # for dx, dy in knight_moves:
        #     new_x, new_y = x + dx, y + dy
        #



