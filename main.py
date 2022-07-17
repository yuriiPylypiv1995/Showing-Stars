# tasks 13.1 and 13.2

import pygame
import sys
from settings import Settings
from star import Star
from random import randint

class Stars:
    """The main class of the game"""
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.stars = pygame.sprite.Group()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Showing Stars")
        self._create_group_stars()

    def run_game(self):
        """The main method for game running"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.settings.screen_bg)
            self.stars.draw(self.screen)
            pygame.display.flip()

    def _create_group_stars(self):
        star_object = Star(self)
        one_star_width, one_star_height = star_object.rect.size
        available_space = self.settings.screen_width - (2 * one_star_width)
        star_numbers_x = available_space // (2 * one_star_width)

        available_space_y = self.settings.screen_height
        rows_number = available_space_y // (2 * one_star_height)

        for row_number in range(rows_number):
            for one_star in range(star_numbers_x):
                star_object = Star(self)
                random_number = randint(-10, 10)
                one_star_x = (one_star_width + 2 * one_star_width * one_star) + random_number
                star_object.rect.x = one_star_x
                star_object.rect.y = (star_object.rect.height + 2 * one_star_height * row_number) + random_number
                self.stars.add(star_object)

if __name__ == "__main__":
    star = Stars()
    star.run_game()
