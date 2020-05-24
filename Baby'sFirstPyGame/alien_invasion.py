import sys
import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion!")

        # Set the background color.
        self.bg_color = (35, 96, 105)

        self.ship = Ship(self)
        # ^^ The self argument here refers to the current instance of AlienInvasion.

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            # ^^ The above calls a helper method!
            self.ship.update()
            # ^^ Ship's position will be updated after checking for keyboard events!
            self._update_screen()
            # ^^ Same here!

    def _check_events(self):
        # This is a helper method, for refactoring practice!!
        # Helper methods are indicated via the single starting "_".
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            # pygame.event.get() will access events that Pygame detects.
            # This function returns a list of events that have taken place
            # since the last time this function was called.
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False


    def _update_screen(self):
        """Update images on the screen, and flip to a new screen."""
        # Set the background color.
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        # ^^ Here we fill the screen with the background color using the fill()
        # method, which acts on a surface and takes only one argument: a color.

        self.ship.blitme()

        # Make the most recently drawn screen visible.
        pygame.display.flip()
        # ^^ When we move the game elements around, pygame.display.flip() continually
        # updates the display to show the new positions of game elements and hides
        # the old ones, creating the illusion of smooth movement.


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
    # ^^ Here we create an instance of the game, and then call run_game(). We place run_game()
    # in an if block that only runs if the file is called directly.
