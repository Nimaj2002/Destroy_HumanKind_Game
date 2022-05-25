# Color Palet https://colorhunt.co/palette/fbf8f1f7ecdee9dac154bab9
# rgb(251, 248, 241)
# rgb(247, 236, 222)
# rgb(233, 218, 193)
# rgb(84, 186, 185)

class Settings:
    """A Class to store all settings for BeAlien"""

    def __init__(self):
        """Initialize the game's static settings."""

        # Screen Settings
        self.screen_width, self.screen_height = 600, 700

        # Earth Settings
        self.Earth_Width, self.Earth_Height = 200, 200
        self.earth_rotation_speed = 2

        # Human Settings
        self.human_Width, self.human_Height = 30, 50
        self.human_rotation_speed = 0.05

        # Ship Settings
        self.Ship_Width, self.Ship_Height = 50, 50

        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)

        # Meteor settings
        self.Meteor_Width, self.Meteor_Height = 50, 50
        self.Meteor_Speed = 0.1

        # colors
        self.light_Beige_color = (206, 192, 171)
        self.dark_Beige_color = (233, 218, 193)
        self.blue_color = (84, 186, 185)

        # How quickly the game speeds up
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.human_rotation_speed = 0.05
        self.earth_rotation_speed = 2

    def increase_speed(self):
        """Increase speed settings."""
        self.human_rotation_speed += 0.05
        self.earth_rotation_speed += 1
