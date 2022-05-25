import os.path
import sys
from time import sleep

import pygame

from Earth import Earth, EarthCenter
from Human import Human
from StartPage import StartScreen
from alienShip import AlienShip
from bullets import Bullet
from game_stats import Gamestats
from meteor import Meteor
from score_board import Scoreboard
from settings import Settings


class BeAlien:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        pygame.display.set_caption("Destroy Human Kind")
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )

        self.back_ground = pygame.image.load(os.path.join("Assets/images/", "background.png"))
        self.back_ground = pygame.transform.scale(self.back_ground,
                                                  (self.settings.screen_width, self.settings.screen_height))

        self.Earth = Earth(self)
        self.Earth_center = EarthCenter(self)
        self.Human = Human(self)
        self.AlienShip = AlienShip(self)
        self.bullets = pygame.sprite.Group()
        self.meteors = pygame.sprite.Group()

        self.total_level = 1
        self.starting_meteor = 10

        self.clock = pygame.time.Clock()
        self.stats = Gamestats(self)
        self.sb = Scoreboard(self)
        self.startpage = StartScreen(self)

        for _ in range(5):
            self._create_a_meteor()

    def run(self):
        """Start the main loop for the game."""
        # Limiting FPS
        self.clock.tick(30)

        while True:
            self._check_events()
            self._level_manager()
            if self.stats.game_active:
                self._Human_movement()
                self.Human.update()
                self.Earth.update()
                self.AlienShip.update()
                self._update_bullets()
                self._update_meteors()
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_point = pygame.mouse.get_pos()
                self._check_play_btn(mouse_point)

    def _check_play_btn(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        button_clicked = self.startpage.play_rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # Reset the game settings.
            self.stats.game_active = True
            self.sb.prep_score()

            # Get rid of any remaining aliens and bullets.
            self.meteors.empty()
            self.bullets.empty()

            # Create a new fleet and center the ship.
            for _ in range(5):
                self._create_a_meteor()
            self.AlienShip.reset_alien()

            # Hide the mouse cursor.
            pygame.mouse.set_visible(False)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_RIGHT or event.key == pygame.K_d and self.stats.game_active:
            self.AlienShip.clockwise_rotating = True
        elif event.key == pygame.K_LEFT or event.key == pygame.K_a and self.stats.game_active:
            self.AlienShip.anti_clockwise_rotating = True
        elif event.key == pygame.K_SPACE and self.stats.game_active:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            self.AlienShip.clockwise_rotating = False
        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
            self.AlienShip.anti_clockwise_rotating = False

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
                self.stats.missed += 1
                self.sb.prep_score()
                self.bullets.remove(bullet)

        if pygame.sprite.groupcollide(self.bullets, self.meteors, True, True):
            self._create_a_meteor()

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

    def _check_meteor_collission(self):
        """check collision of each meteor with Ship & walls & Earth and creat another meteor if"""
        for meteor in self.meteors:
            offset = (int(self.AlienShip.x - meteor.rect.x), int(self.AlienShip.y - meteor.rect.y))
            if self.AlienShip.Ship_mask.overlap(meteor.image_mask, offset):
                self._ship_hit()

            elif self.Earth_center.rect.colliderect(meteor):
                self.meteors.remove(meteor)
                self._create_a_meteor()

            elif meteor.rect.x <= -100 or \
                    meteor.rect.x >= self.settings.screen_width + 100 or \
                    meteor.rect.y <= -100 or \
                    meteor.rect.y >= self.settings.screen_height + 100:
                self.meteors.remove(meteor)
                self._create_a_meteor()

    def _ship_hit(self):
        """Respond to the ship being hit by a meteor and showing start screen"""
        self.stats.save_high_score()
        self.stats.reset_stats()
        sleep(1)
        self.stats.game_active = False
        pygame.mouse.set_visible(True)

    def _create_a_meteor(self):
        """ creates only one meteor """
        meteor = Meteor(self)
        self.meteors.add(meteor)

    def _update_meteors(self):
        """updates meteors locations"""
        self._check_meteor_collission()
        self.meteors.update()

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.blit(self.back_ground, (0, 0))

        # Drawing Bullets
        for bullet in self.bullets.sprites():
            bullet.move()
            bullet.draw_bullet()

        # Draw the score information.
        self.sb.show_score()

        # Drawing AlienShip,meteors ,Earth & Human
        self.AlienShip.blitme()
        self.meteors.draw(self.screen)
        self.Earth.blitme()
        self.Human.blitme()

        # Draw the StartScreen if the game is inactive.
        if not self.stats.game_active:
            self.startpage.blitme()

        # Make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == "__main__":
    beAlien = BeAlien()
    beAlien.run()
