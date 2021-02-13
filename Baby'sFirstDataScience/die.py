from random import randint

class Die:
    """A class representint a single die."""

    def __init__(self, num_sides=6):
        """Assume a six-sided die."""
        # If an argument is included, that value will set the number of sides
        # on the die
        self.num_sides = num_sides

    def roll(self):
        """Return a random value between 1 and number of sides."""
        return randint(1, self.num_sides)
