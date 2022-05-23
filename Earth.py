import os.path
from math import pi

import pygame.image


# 556 599

class Earth:
    """A class to manage Earth and its Ball"""

    def __init__(self, ba_game):
        """Initilize the Earth and set its starting position"""
        self.screen = ba_game.screen
        self.screen_rect = ba_game.screen.get_rect()
        self.settings = ba_game.settings

        # Load the Earth image and get its rect.
        self.Earth_image = pygame.image.load(os.path.join("./Assets/images", "Earth.png")).convert_alpha()
        self.Earth_image = pygame.transform.scale(self.Earth_image,
                                                  (self.settings.Earth_Width, self.settings.Earth_Height))
        self.rect = self.Earth_image.get_rect()

        # Start Each new Earth at the center
        self.rect.center = self.screen_rect.center

        # Store a decimal value for the Earth's angel_in_degrees.
        self.angel_in_degrees = 0

        # Rotation Flag
        self.clockwise_rotating = False
        self.anti_clockwise_rotating = False

    def update(self):
        """Updating rotation of Earth"""
        if self.clockwise_rotating:
            self.angel_in_degrees -= self.settings.earth_rotation_speed
        elif self.anti_clockwise_rotating:
            self.angel_in_degrees += self.settings.earth_rotation_speed

    def blitme(self):
        """draw the Eart at the new rotation"""
        old_center = self.rect.center
        angel_in_radian = (self.angel_in_degrees * pi) / 180
        new_Earth_image = pygame.transform.rotate(self.Earth_image, angel_in_radian)

        new_rect = new_Earth_image.get_rect()
        new_rect.center = old_center
        self.screen.blit(new_Earth_image, new_rect)


class EarthCenter:
    """This Class represents earth's Center for bullet collison"""

    def __init__(self, ba_game):
        self.screen = ba_game.screen
        self.screen_rect = ba_game.screen.get_rect()
        self.setting = ba_game.settings

        self.rect = pygame.Rect(self.setting.screen_width / 2 - 50, self.setting.screen_height / 2 - 50, 100, 100)

    def blitme(self):
        pygame.draw.rect(self.screen, (0, 0, 0), self.rect)
