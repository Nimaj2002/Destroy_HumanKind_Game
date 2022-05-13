import sys

import pygame

from Earth import Earth
from Human import Human
from settings import Settings


# Color Palet https://colorhunt.co/palette/fbf8f1f7ecdee9dac154bab9
# rgb(251, 248, 241)
# rgb(247, 236, 222)
# rgb(233, 218, 193)
# rgb(84, 186, 185)

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
        self.Human = Human(self)

        self.total_level = 1
        self.clock = pygame.time.Clock()


    def run(self):
        """Start the main loop for the game."""
        # Limiting FPS
        self.clock.tick(30)

        while True:
            self._check_events()
            self._Earth_movement()
            self._Human_movement()
            self.Human.update()
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

    def _Human_movement(self):
        """This function is for rotating Earth in difrent rotations"""
        if self.total_level == 1:
            self.Human.clockwise_rotating = True
        elif self.total_level == 2:
            self.Human.anti_clockwise_rotating = True

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.Human.blitme()
        self.Earth.blitme()

        # Make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == "__main__":
    beAlien = BeAlien()
    beAlien.run()
