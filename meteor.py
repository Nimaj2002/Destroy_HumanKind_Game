import os.path
import random
from math import cos, sin, pi

import pygame
from pygame.sprite import Sprite


class Meteor(Sprite):
    """A class to represent a single meteor in the fleet."""

    def __init__(self, ba_game):
        """Initialize the alien and set its starting position."""
        super().__init__()

        self.screen = ba_game.screen
        self.screen_rect = ba_game.screen.get_rect()
        self.settings = ba_game.settings

        # loading meteor image and get its rect
        # using image name instead of meteor_image because of sprite
        self.image = pygame.image.load(os.path.join("./Assets/images", "meteor.png")).convert_alpha()
        self.image = pygame.transform.scale(self.image,
                                            (self.settings.Meteor_Width, self.settings.Meteor_Height))
        self.rect = self.image.get_rect()

        # Start Each meteor at TOP or DOWN , RIGHT or LEFT
        self.starting_locations = ["TOP", "DOWN", "RIGHT", "LEFT"]
        self.startfrom = random.choice(self.starting_locations)

        # movement angel
        self.movement_angel_in_degrees = random.randint(20, 160)
        self.movement_angel_in_radians = (self.movement_angel_in_degrees * pi / 180)

        # Locating the meteor and rotating it
        if self.startfrom == "TOP":
            self.rect.centerx = random.randint(0, self.settings.screen_width)
            self.rect.centery = -self.settings.Meteor_Height
            # rotating meteor in the movement angel
            self.image = pygame.transform.rotate(self.image, -(90 + self.movement_angel_in_degrees))

        if self.startfrom == "DOWN":
            self.rect.centerx = random.randint(0, self.settings.screen_width)
            self.rect.centery = self.settings.screen_height + self.settings.Meteor_Height
            # rotating meteor in the movement angel
            if self.movement_angel_in_degrees < 90:
                self.image = pygame.transform.rotate(self.image, -(90 - self.movement_angel_in_degrees))

            elif self.movement_angel_in_degrees >= 90:
                self.image = pygame.transform.rotate(self.image, self.movement_angel_in_degrees - 90)

        if self.startfrom == "RIGHT":
            self.rect.centerx = self.settings.screen_width + self.settings.Meteor_Width
            self.rect.centery = random.randint(0, self.settings.screen_height)
            # rotating meteor in the movement angel
            self.image = pygame.transform.rotate(self.image, 180 - self.movement_angel_in_degrees)

        if self.startfrom == "LEFT":
            self.rect.centerx = -self.settings.Meteor_Width
            self.rect.centery = random.randint(0, self.settings.screen_height)
            # rotating meteor in the movement angel
            self.image = pygame.transform.rotate(self.image, -(180 - self.movement_angel_in_degrees))

        # Store the meteor's exact horizontal and vertical position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        """Moving meteor randomly"""
        if self.startfrom == "TOP":
            self.x += self.settings.Meteor_Speed * cos(self.movement_angel_in_radians)
            self.y += self.settings.Meteor_Speed * abs(sin(self.movement_angel_in_radians))
        if self.startfrom == "DOWN":
            self.x += self.settings.Meteor_Speed * cos(self.movement_angel_in_radians)
            self.y -= self.settings.Meteor_Speed * abs(sin(self.movement_angel_in_radians))
        if self.startfrom == "RIGHT":
            self.x -= self.settings.Meteor_Speed * abs(sin(self.movement_angel_in_radians))
            self.y += self.settings.Meteor_Speed * cos(self.movement_angel_in_radians)
        if self.startfrom == "LEFT":
            self.x += self.settings.Meteor_Speed * abs(sin(self.movement_angel_in_radians))
            self.y += self.settings.Meteor_Speed * cos(self.movement_angel_in_radians)

        self.rect.x = self.x
        self.rect.y = self.y
