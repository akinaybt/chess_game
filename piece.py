import pygame
import os

class Piece():
    def __init__(self, name, position, colour, value, image_url=None, board=None):
        self.name = name
        self.position = position
        self.x = position[0]
        self.y = position[1]
        self.colour = colour
        self.board = board
        self.value = value
        self.image_url = image_url
        self.set_image_url()
        self.made_move = False

    def set_image_url(self):
        self.image_url = os.path.join(
            f'imgs/{self.colour}_{self.name}.png'
        )

    def move(self, new_position):
        self.position = new_position

    def possible_moves(self, board):
        raise NotImplementedError("This method should be redefined in derived classes.")

    def is_valid_move(self, position, board):
        return position in self.possible_moves(board)




