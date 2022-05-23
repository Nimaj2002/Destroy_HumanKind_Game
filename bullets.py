from math import atan2, cos, sin

import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, ba_game):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.dy = None
        self.dx = None
        self.screen = ba_game.screen
        self.settings = ba_game.settings
        self.color = self.settings.bullet_color

        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ba_game.AlienShip.rect.center

        # Store the bullet's position as a decimal value.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet toward the Earth."""
        # Update the decimal position of the bullet.
        # get angle to center in rafians
        angle = atan2((self.settings.screen_height/2)-self.y, (self.settings.screen_width/2)-self.x)
        self.dx = cos(angle)*0.5
        self.dy = sin(angle)*0.5
        # Update the rect position.
        # self.rect.y = self.y + self.dy
        self.rect.x -= self.dx

    def move(self):
        self.x = self.x + self.dx
        self.y = self.y + self.dy
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.circle(self.screen, self.color, (self.rect.x, self.rect.y), 5, 0)