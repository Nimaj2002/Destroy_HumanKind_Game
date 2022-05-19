import os
from math import sin, cos, atan2, pi

import pygame


class AlienShip:
    def __init__(self, ba_game):
        """Initilize the Ship and set its starting position"""
        self.screen = ba_game.screen
        self.screen_rect = ba_game.screen.get_rect()
        self.settings = ba_game.settings

        # Load the Ship image and get its rect.
        self.Ship_image = pygame.image.load(os.path.join("./Assets/images", "ufo.png")).convert_alpha()
        self.Ship_image = pygame.transform.scale(self.Ship_image,
                                                 (self.settings.Ship_Width, self.settings.Ship_Height))
        self.rect = self.Ship_image.get_rect()

        # Start Each new Ship at the top format
        self.rect.centerx = self.screen_rect.centerx + (self.settings.Earth_Width / 2 + 100)
        self.rect.centery = self.screen_rect.centery

        # Storing angle and location of Ship
        self.spining_angel = 0

        self.x, self.y = float(self.rect.x), float(self.rect.y)

        # Rotating Flag
        self.clockwise_rotating = False
        self.anti_clockwise_rotating = False

    def update(self):
        if self.clockwise_rotating:
            self.spining_angel += round(1/360, 4)

        if self.anti_clockwise_rotating:
            self.spining_angel -= round(1/360, 4)

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.rect.centerx = self.screen_rect.centerx + cos(self.spining_angel) * (self.settings.Earth_Width / 2 + 150)
        self.rect.centery = self.screen_rect.centery + sin(self.spining_angel) * (self.settings.Earth_Height / 2 + 150)

    def blitme(self):
        old_center = self.rect.center

        angle_in_radian = round(
            atan2((self.settings.screen_height / 2) - self.y, (self.settings.screen_width / 2) - self.x),
            2
        )
        angle_in_degrees = angle_in_radian * round(180/pi, 2)
        new_Ship_image = pygame.transform.rotate(self.Ship_image, 90 - angle_in_degrees)

        new_rect = new_Ship_image.get_rect()
        new_rect.center = old_center
        self.screen.blit(new_Ship_image, new_rect)
