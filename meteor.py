import pygame


class meteor:
    """A class to represent a single meteor in the fleet."""
    def __init__(self, ba_game):
        """Initialize the alien and set its starting position."""
        self.screen = ba_game.screen
        self.settings = ba_game.settings
        self.rect = pygame.Rect(self.settings.screen_width/2-45, self.settings.screen_height/2-45, 90, 90)

    def draw(self):
        pygame.draw.circle(self.screen, self.settings.meteor_color, (self.rect.x, self.rect.y), 5, 0)


