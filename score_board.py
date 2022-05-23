import pygame.font


class Scoreboard:
    """A class to report scoring information."""

    def __init__(self, ba_game):
        """Initialize scorekeeping attributes."""
        self.screen = ba_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ba_game.settings
        self.stats = ba_game.stats

        # attributes needed in next parts
        self.missed_rect = None
        self.missed_image = None
        self.score_rect = None
        self.score_image = None
        self.high_image = None

        # Font settings for scoring information.
        self.text_color = (30, 30, 30)
        self.font = pygame.font.Font("./Assets/glitched.otf", 48)

        # Prepare the initial score image.
        self.prep_score()

    def prep_score(self):
        """Turn the score into a rendered image."""
        score_str = f"Scored {str(self.stats.score)}"
        self.score_image = self.font.render(score_str, True, self.settings.blue_color, self.settings.light_Beige_color)
        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

        missed_str = f"Missed {str(self.stats.missed)}"
        self.missed_image = self.font.render(missed_str, True, self.settings.blue_color,
                                             self.settings.light_Beige_color)
        # Display the score at the bottom of the score string.
        self.missed_rect = self.missed_image.get_rect()
        self.missed_rect.right = self.screen_rect.right - 20
        self.missed_rect.top = 60

        high_score = f"high Score {str(self.stats.high_score)}"
        self.high_image = self.font.render(high_score, True, self.settings.blue_color, self.settings.light_Beige_color)
        # Display the score at the top left of the score string.
        self.high_rect = self.high_image.get_rect()
        self.high_rect.left = self.screen_rect.left + 20
        self.high_rect.top = 20

    def show_score(self):
        """Draw score to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.missed_image, self.missed_rect)
        self.screen.blit(self.high_image, self.high_rect)
