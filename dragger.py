import pygame
from const import *

class Dragger:
    def __init__(self):
        self.piece = None
        self.dragging = False
        self.x_coordinate = 0
        self.y_coordinate = 0
        self.initial_row = 0
        self.initial_col = 0

    def update_position(self, surface):
        self.piece.set_image_url()
        image_url = self.piece.image_url
        img = pygame.image.load(image_url)
        img_center = (self.x_coordinate, self.y_coordinate)
        self.piece.image_rect = img.get_rect(center=img_center)
        surface.blit(img, self.piece.image_rect)

    def update_mouse_coordinate(self, pos):
        self.x_coordinate, self.y_coordinate = pos

    def save_initial_position(self, pos):
        self.initial_row = pos[1] // SQSIZE
        self.initial_col = pos[0] // SQSIZE

    def drag_piece(self, piece):
        self.piece = piece
        self.dragging = True

    def undrag_piece(self):
        self.piece = None
        self.dragging = False
