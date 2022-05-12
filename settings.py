import os

import pygame


class Settings:
    """A Class to store all settings for BeAlien"""
    def __init__(self):
        """Initialize the game's static settings."""

        # Screen Settings
        self.screen_width, self.screen_height = 1200, 800
        self.bg_color = (230, 230, 230)
        self.space = pygame.transform.scale(
            pygame.image.load(os.path.join("images", "space.jpg")),
            (self.screen_width, self.screen_height)
        )