import sys

import pygame

from Earth import Earth
from settings import Settings


class BeAlien:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        pygame.display.set_caption("Be Alien :D")
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )

        self.Earth = Earth(self)

        self.total_level = 2
        self.clock = pygame.time.Clock()

    def run(self):
        """Start the main loop for the game."""
        # Limiting FPS
        self.clock.tick(60)

        while True:
            self._check_events()
            self._Earth_movement()
            self.Earth.update()
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _Earth_movement(self):
        """This function is for rotating Earth in difrent rotations"""
        if self.total_level == 1:
            self.Earth.clockwise_rotating = True
        elif self.total_level == 2:
            self.Earth.anti_clockwise_rotating = True

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.Earth.blitme()
        # Make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == "__main__":
    beAlien = BeAlien()
    beAlien.run()
