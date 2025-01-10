import pygame

class Sound:
    """
       Represents sound in the game. Responsible for laying the path to the file of the sound and
       creates a sound object and begins it playback.

       Attributes:
           path: path to the sound file.
           sound: creates a sound object.

       Methods:
            play(self):
                plays the sound.
        """
    def __init__(self, path):
        self.path = path
        self.sound = pygame.mixer.Sound(path)

    def play(self):
        pygame.mixer.Sound.play(self.sound)