import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    """The class for stars creating"""
    def __init__(self, star_game):
        super().__init__()
        self.screen = star_game.screen
        self.screen_rect = self.screen.get_rect()

        self.image = pygame.image.load("images/star.bmp").convert()
        self.rect = self.image.get_rect()




