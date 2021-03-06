import os.path
from math import sin, cos, atan2, pi

import pygame


class Human:
    def __init__(self, ba_game):
        self.screen = ba_game.screen
        self.screen_rect = ba_game.screen.get_rect()
        self.settings = ba_game.settings

        # Load human image and get its rect
        self.human_image = pygame.image.load(os.path.join("./Assets/images", "human.png")).convert_alpha()
        self.human_image = pygame.transform.scale(self.human_image,
                                                  (self.settings.human_Width, self.settings.human_Height))
        self.rect = self.human_image.get_rect()

        # Store a decimal value for the Human positions.
        self.spining_angel_in_degrees = -90

        self.x, self.y = float(self.rect.x), float(self.rect.y)

        # Rotating Flag
        self.clockwise_rotating = True

    def update(self):
        """Updating rotation of human"""
        if self.clockwise_rotating:
            self.spining_angel_in_degrees += self.settings.human_rotation_speed

        elif not self.clockwise_rotating:
            self.spining_angel_in_degrees -= self.settings.human_rotation_speed

        self.x, self.y = float(self.rect.x), float(self.rect.y)

        # rotation of human around Earth
        spining_angel_in_radians = (self.spining_angel_in_degrees * pi) / 180
        self.rect.centerx = self.screen_rect.centerx + cos(spining_angel_in_radians) * (self.settings.Earth_Width / 2)
        self.rect.centery = self.screen_rect.centery + sin(spining_angel_in_radians) * (self.settings.Earth_Height / 2)

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
