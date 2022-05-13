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
        self.bg_color = (251, 248, 241)

        # Earth Settings
        self.Earth_Width, self.Earth_Height = 200, 200
        self.rotation_speed = 0.1

        # Human Settings
        self.human_Width, self.human_Height = 50, 50