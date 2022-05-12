import os

import pygame


class Settings:
    """A Class to store all settings for BeAlien"""
    def __init__(self):
        """Initialize the game's static settings."""

        # Screen Settings
        self.screen_width, self.screen_height = 600, 700
        self.bg_color = (251, 248, 241)