class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (104, 130, 158)
        # ^^ (1200, 800) is a tuple that defines dimensions of game window, in pixels.
        # The object we assigned to self.screen is called a "surface". Each element
        # the game is its own surface.
