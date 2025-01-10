import pygame
import os

from sound import Sound

class Config:
    """
        Represents a couple of configuration attributes of the sound and font.

        Attributes:
            font: the name of the font to use, its size.
            move_sound: responsible for the sound of moving figures on the board.
            capture_sound: responsible for the sound of capturing figures during the game.
        """
    def __init__(self):
        self.font = pygame.font.SysFont("monospace", 15, bold=True)
        self.move_sound = Sound(
            os.path.join('sounds/sounds_move.wav')
        )
        self.capture_sound = Sound(
            os.path.join('sounds/sounds_capture.wav')
        )