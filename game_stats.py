import json


class Gamestats:
    def __init__(self, ba_game):
        """Initialize statistics."""
        self.settings = ba_game.settings
        self.reset_stats()

        # Start game in an inactive state.
        self.game_active = False

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.score = 0
        self.missed = 0
        self.total_level = 1
        self.get_high_score()

    def get_high_score(self):
        try:
            with open("highscore.json", "r") as file:
                json_data = json.load(file)
                self.high_score = json_data["high_score"]

        except FileNotFoundError:
            self.high_score = 0

    def save_high_score(self):
        if self.score > self.high_score:
            # Data to be written
            dictionary = {
                "high_score": self.score
            }

            with open("highscore.json", "w") as file:
                json.dump(dictionary, file, indent=4)
