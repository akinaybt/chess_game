import os

class Piece:
    def __init__(self, name, colour, value, image_url=None, image_rect=None):
        self.name = name
        self.colour = colour
        self.value = value
        self.image_url = image_url
        self.set_image_url()
        self.moves = []
        self.made_move = False
        self.image_rect = image_rect

    def set_image_url(self):
        self.image_url = os.path.join(
            f'imgs/{self.colour}_{self.name}.png'
        )

    def add_move(self, move):
        self.moves.append(move)

    def clear_moves(self):
        self.moves = []
