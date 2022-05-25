import os

import pygame


class StartScreen:
    def __init__(self, ba_game):
        pygame.font.init()

        self.screen = ba_game.screen
        self.screen_rect = ba_game.screen.get_rect()
        self.settings = ba_game.settings
        self.stats = ba_game.stats

        # Background
        self.Back_ground = pygame.image.load(os.path.join("Assets/images/", "background.png"))
        self.Back_ground = pygame.transform.scale(self.Back_ground,
                                                  (self.settings.screen_width, self.settings.screen_height))

        # Fonts
        self.Big_font = pygame.font.Font(os.path.join("Assets/MaldiniBold.ttf"), 50)
        self.Small_font = pygame.font.Font(os.path.join("Assets/MaldiniStyle.ttf"), 50)

        # Logos
        self.logo = pygame.image.load(os.path.join("Assets/images/", "logo.png"))
        self.logo = pygame.transform.scale(self.logo, (400, 200))

        # Load Keyboard img
        self.keyboard_image = pygame.image.load(os.path.join("Assets/images/", "buttons.png"))
        self.keyboard_image = pygame.transform.scale(self.keyboard_image, (200, 160))

        # Creat play button Rect
        self.play_btn = pygame.image.load(os.path.join("Assets/images/", "start.png"))
        self.play_btn = pygame.transform.scale(self.play_btn, (200, 80))
        self.play_rect = self.play_btn.get_rect()
        self.play_rect.center = (self.settings.screen_width // 2, self.settings.screen_height - 100)

    def blitme(self):
        self.screen.blit(self.Back_ground, (0, 0))
        self.screen.blit(self.logo, (self.settings.screen_width // 2 - 200, 20))

        self.write_text("High Score", "small", self.settings.blue_color, (self.settings.screen_width // 2 - 100, 210))
        self.write_text(f"{self.stats.high_score}", "small", self.settings.blue_color,
                        (self.settings.screen_width // 2 - 20, 260))

        self.write_text("Guid for Noobs", "small", self.settings.blue_color,
                        (self.settings.screen_width // 2 - 150, 330))
        self.screen.blit(self.keyboard_image, (self.settings.screen_width // 2 - 100, 380))

        self.screen.blit(self.play_btn, self.play_rect)

    def write_text(self, text, font_weight, color, location=(0, 0)):
        draw_text = ""
        if font_weight.lower() == "big":
            draw_text = self.Big_font.render(text, 1, color)
        elif font_weight.lower() == "small":
            draw_text = self.Small_font.render(text, 1, color)

        self.screen.blit(draw_text, location)
