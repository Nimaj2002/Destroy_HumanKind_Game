import os.path
from math import sin, cos, atan2, pi

import pygame


class Human:
    def __init__(self, ba_game):
        self.screen = ba_game.screen
        self.screen_rect = ba_game.screen.get_rect()
        self.settings = ba_game.settings

        # Load human image and get its rect
        self.human_image = pygame.image.load(os.path.join("images", "human.png"))
        self.human_image = pygame.transform.scale(self.human_image,
                                                  (self.settings.human_Width, self.settings.human_Height))

        self.rect = self.human_image.get_rect()

        # Store a decimal value for the Human positions.
        self.spining_angel = -90

        self.x, self.y = float(self.rect.x), float(self.rect.y)

        # Rotating Flag
        self.clockwise_rotating = False
        self.anti_clockwise_rotating = False

    def update(self):
        """Updating rotation of human"""
        if self.clockwise_rotating:
            self.spining_angel = float(self.spining_angel + 0.0017) % 360

        elif self.anti_clockwise_rotating:
            self.spining_angel = (self.spining_angel - 0.001) % 360

        self.x, self.y = float(self.rect.x), float(self.rect.y)

        # rotation of human around Earth
        self.rect.centerx = self.screen_rect.centerx + cos(self.spining_angel) * (self.settings.Earth_Width / 2)
        self.rect.centery = self.screen_rect.centery + sin(self.spining_angel) * (self.settings.Earth_Height / 2)

    def blitme(self):
        old_center = self.rect.center

        # Rotating Human based on Earth position
        angle_in_radian = round(
            atan2((self.settings.screen_height / 2) - self.y, (self.settings.screen_width / 2) - self.x),
            2
        )
        angle_in_degrees = angle_in_radian * round(180 / pi, 2)
        new_human_image = pygame.transform.rotate(self.human_image, 90 - angle_in_degrees)

        new_rect = new_human_image.get_rect()
        new_rect.center = old_center

        self.screen.blit(new_human_image, new_rect)
