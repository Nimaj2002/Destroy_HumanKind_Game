import os.path
from math import sin, cos

import pygame


class Human:
    def __init__(self, ba_game):
        self.screen = ba_game.screen
        self.screen_rect = ba_game.screen.get_rect()
        self.setting = ba_game.settings

        # Load human image and get its rect
        self.human_image = pygame.image.load(os.path.join("images", "ball.png"))
        self.human_image = pygame.transform.scale(self.human_image,
                                                  (self.setting.human_Width, self.setting.human_Height))
        # self.human_image = pygame.transform.rotate(self.human_image, -90)
        self.rect = self.human_image.get_rect()

        # Store a decimal value for the Human's angel.
        self.spining_angel = -90
        self.rotation_angel = 0

        # Rotating Flag
        self.clockwise_rotating = False
        self.anti_clockwise_rotating = False

    def update(self):
        """Updating rotation of human"""
        if self.clockwise_rotating:
            self.spining_angel = float(self.spining_angel + 0.0017) % 360
            # self.rotation_angel = float(self.rotation_angel - 0.001) % 360
            # print(self.spining_angel, "    ", self.rotation_angel)
        elif self.anti_clockwise_rotating:
            self.spining_angel = (self.spining_angel - 0.001) % 360
            # self.rotation_angel = (self.rotation_angel + 0.1) % 360

    def blitme(self):
        # new_human_image = pygame.transform.rotate(self.human_image, cos(self.rotation_angel)+sin(self.rotation_angel))
        new_human_image = self.human_image
        new_rect = new_human_image.get_rect()
        # rotation of human around Earth
        new_rect.centerx = self.screen_rect.centerx + cos(self.spining_angel) * (self.setting.Earth_Width / 2)
        new_rect.centery = self.screen_rect.centery + sin(self.spining_angel) * (self.setting.Earth_Height / 2)
        self.screen.blit(new_human_image, new_rect)
