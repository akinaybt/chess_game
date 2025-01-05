import pygame
import os

from sound import Sound

class Config:
    def __init__(self):
        self.font = pygame.font.SysFont("monospace", 15, bold=True)
        self.move_sound = Sound(
            os.path.join('sounds/sounds_move.wav')
        )
        self.capture_sound = Sound(
            os.path.join('sounds/sounds_capture.wav')
        )