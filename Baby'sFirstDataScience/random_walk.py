from random import choice

class RandomWalk:
    """A class to generate random walks."""

    def __init__(self, num_points=5000):
        """Initialize attributes of a walk."""
        self.num_points = num_points

        # All walks start at (0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        direction = choice([1, -1])
        # We decide with the above "Will the walk go right or left?""
        distance = choice([0, 1, 2, 3, 4])
        # We decide with the above "How far will the walk go?"
        step = direction * distance
        return step

    def fill_walk(self):
        """Calculate all the points in the walk."""

        # Keep taking steps until the walk reaches the desired length
        while len(self.x_values) < self.num_points:
        # ^^ This is setting up a loop that runs until the walk is filled with
        # the correct number of points.

            # The below is commented out in favor of the refactoring into get_step()
            # method above! Showing here just to display what was refactored.
            # x_direction = choice([1, -1])
            # x_distance = choice([0, 1, 2, 3, 4])
            # x_step = x_direction * x_distance
            #
            # y_direction = choice([1, -1])
            # y_distance = choice([0, 1, 2, 3, 4])
            # y_step = y_direction * y_distance

            x_step = self.get_step()
            y_step = self.get_step()

            # Reject moves that go nowhere
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the new position
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)
