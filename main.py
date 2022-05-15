import sys

import pygame

from Earth import Earth, Earth_center
from Human import Human
from alienShip import AlienShip
from bullets import Bullet
from game_stats import Gamestats
from score_board import Scoreboard
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
        self.Earth_center = Earth_center(self)
        self.Human = Human(self)
        self.Ship = AlienShip(self)
        self.bullets = pygame.sprite.Group()

        self.total_level = 1
        self.clock = pygame.time.Clock()
        self.stats = Gamestats()
        self.sb = Scoreboard(self)


    def run(self):
        """Start the main loop for the game."""
        # Limiting FPS
        self.clock.tick(30)

        while True:
            self._check_events()
            self._level_manager()
            self._Human_movement()
            self.Human.update()
            self.Earth.update()
            self.Ship.update()
            self._update_bullets()
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.Ship.clockwise_rotating = True
        elif event.key == pygame.K_LEFT:
            self.Ship.anti_clockwise_rotating = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.Ship.clockwise_rotating = False
        elif event.key == pygame.K_LEFT:
            self.Ship.anti_clockwise_rotating = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positions.
        self.bullets.update()

        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if self.Human.rect.colliderect(bullet):
                self.stats.score += 1
                self.sb.prep_score()
                self.bullets.remove(bullet)
            elif self.Earth_center.rect.colliderect(bullet):
                self.bullets.remove(bullet)

    def _level_manager(self):
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
        self.Ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.move()
            bullet.draw_bullet()
        # Draw the score information.
        self.sb.show_score()
        self.Earth.blitme()
        self.Human.blitme()
        # Make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == "__main__":
    beAlien = BeAlien()
    beAlien.run()
