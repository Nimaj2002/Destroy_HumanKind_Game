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
