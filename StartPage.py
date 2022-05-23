import os

import pygame


class StartScreen:
    def __init__(self, ba_game):
        self.screen = ba_game.screen
        self.screen_rect = ba_game.screen.get_rect()
        self.settings = ba_game.settings
        self.stats = ba_game.stats

        # Fonts
        pygame.font.init()
        self.Big_font = pygame.font.SysFont("comicsans", 50)
        self.Small_font = pygame.font.SysFont("comicsans", 30)

        # Load Keyboard img
        self.keyboard_image = pygame.image.load(os.path.join("Assets/images/", "buttons.png"))
        self.keyboard_image = pygame.transform.scale(self.keyboard_image, (200, 200))

        # Creat play button Rect
        self.play_btn = pygame.Rect(self.settings.screen_width // 2 - 50, self.settings.screen_height - 100, 120, 80)

    def blitme(self):
        self.screen.fill(self.settings.dark_Beige_color)
        self.write_text("Be Alien!", "big", self.settings.blue_color, (self.settings.screen_width // 2 - 100, 40))

        self.write_text("Movements:", "small", self.settings.blue_color, (self.settings.screen_width // 2 - 200, 200))
        self.screen.blit(self.keyboard_image, (self.settings.screen_width // 2 + 10, 150))

        self.write_text("High Score:", "small", self.settings.blue_color, (self.settings.screen_width // 2 - 200, 400))
        self.write_text(f"{self.stats.high_score}", "small", self.settings.blue_color,
                        (self.settings.screen_width // 2 + 100, 400))

        pygame.draw.rect(self.screen, self.settings.dark_Beige_color, self.play_btn)
        self.write_text("Play!", "big", self.settings.blue_color,
                        (self.settings.screen_width // 2 - 40, self.settings.screen_height - 100))

    def write_text(self, text, font_weight, color, location=(0, 0)):
        draw_text = ""
        if font_weight.lower() == "big":
            draw_text = self.Big_font.render(text, 1, color)
        elif font_weight.lower() == "small":
            draw_text = self.Small_font.render(text, 1, color)

        self.screen.blit(draw_text, location)
