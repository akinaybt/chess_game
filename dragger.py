import pygame
from const import *

class Dragger:
    """
        Represents the dragging of pieces.

        Attributes:
            piece : The piece being dragged.
            dragging : Whether the piece is currently being dragged.
            x_coordinate : The x-coordinate of the mouse position.
            y_coordinate : The y-coordinate of the mouse position.
            initial_row : The initial row of the piece being dragged.
            initial_col : The initial column of the piece being dragged.

        Methods:
            update_position(surface):
            Updates the position of the piece on the board.
            update_mouse_coordinate(pos):
            Updates the mouse position.
            save_initial_position(pos):
            Saves the initial position of the piece being dragged.
            drag_piece(piece):
            Method to start dragging a piece.
            return_piece():
            Returns the piece to its original position.
            undrag_piece():
            Method to end dragging a piece.
    """
    def __init__(self):
        self.piece = None
        self.dragging = False
        self.x_coordinate = 0
        self.y_coordinate = 0
        self.initial_row = 0
        self.initial_col = 0

    def update_position(self, surface):
        """Method to update the position of the piece on the board."""
        self.piece.set_image_url()
        image_url = self.piece.image_url
        img = pygame.image.load(image_url)
        img_center = (self.x_coordinate, self.y_coordinate)
        self.piece.image_rect = img.get_rect(center=img_center)
        surface.blit(img, self.piece.image_rect)

    def update_mouse_coordinate(self, pos):
        """Method to update the mouse position."""
        self.x_coordinate, self.y_coordinate = pos

    def save_initial_position(self, pos):
        """Method to save the initial position of the piece being dragged."""
        self.initial_row = pos[1] // SQSIZE
        self.initial_col = pos[0] // SQSIZE

    def drag_piece(self, piece):
        """Method to start dragging a piece."""
        self.piece = piece
        self.dragging = True

    def return_piece(self):
        """Method to return the piece to its original position."""
        self.piece.row = self.initial_row
        self.piece.col = self.initial_col
        self.undrag_piece()

    def undrag_piece(self):
        """Method to end dragging a piece."""
        self.piece = None
        self.dragging = False
