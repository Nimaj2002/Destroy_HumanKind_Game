import os
from math import sin, cos

import pygame


class AlienShip:
    def __init__(self, ba_game):
        """Initilize the Ship and set its starting position"""
        self.screen = ba_game.screen
        self.screen_rect = ba_game.screen.get_rect()
        self.setting = ba_game.settings

        # Load the Ship image and get its rect.
        self.Ship_image = pygame.image.load(os.path.join("images", "ufo.png"))
        self.Ship_image = pygame.transform.scale(self.Ship_image,
                                                 (self.setting.Ship_Width, self.setting.Ship_Height))
        self.rect = self.Ship_image.get_rect()

        # Start Each new Ship at the top format
        self.rect.centerx = self.screen_rect.centerx + (self.setting.Earth_Width / 2 + 100)
        self.rect.centery = self.screen_rect.centery

        self.spining_angel = 0
        self.rotation_angel = -90

        # Rotating Flag
        self.clockwise_rotating = False
        self.anti_clockwise_rotating = False

    def update(self):
        if self.clockwise_rotating:
            self.spining_angel += 0.01
            self.rotation_angel -= 0.01

        if self.anti_clockwise_rotating:
            self.spining_angel -= 0.01
            self.rotation_angel += 0.01

        self.rect.centerx = self.screen_rect.centerx + cos(self.spining_angel) * (self.setting.Earth_Width / 2 + 150)
        self.rect.centery = self.screen_rect.centery + sin(self.spining_angel) * (self.setting.Earth_Height / 2 + 150)


    def blitme(self):
        old_center = self.rect.center
        new_Ship_image = pygame.transform.rotate(self.Ship_image, self.rotation_angel)
        # new_Ship_image = self.Ship_image
        new_rect = new_Ship_image.get_rect()
        new_rect.center = old_center
        self.screen.blit(new_Ship_image, new_rect)
