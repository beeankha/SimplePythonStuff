import pygame

class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        # In Pygame, "rect" = rectangles.

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom
        # "midbottom" is one of the shortcut properties you can use to place game
        # elements; alternatively you can use x- and y-coordinates.
        # In Pygame, the origin (0, 0) is at the top-left corner of the screen, 
        # and coordinates increase as you go down and to the right. 

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
        # The position is specified by self.rect.

