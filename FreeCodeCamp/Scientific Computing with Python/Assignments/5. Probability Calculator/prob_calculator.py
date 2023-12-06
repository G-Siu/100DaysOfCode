import copy
import random
# Consider using the modules imported above.
# Determine probability of drawing certain balls randomly


class Hat:
    def __init__(self, *kwargs):
        # self.colour_dict = dict()
        # for item, value in kwargs:
            # self.colour_dict["item"] = value
        self.colour_dict = kwargs
        return self.colour_dict

    # Arguments should be converted to contents instance variable
    # List of strings representing the ball colour, and as many of that colour

    # Accepts argument as number of balls to be drawn
    def draw(self):
        # Remove ball from contents at random, return those balls as list of
        # strings
        # Should not go back into hat during draw
        # If draws exceed number of balls in hat, return all balls
        pass


# Returns probability
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    # hat: object containing balls to be copied inside the function
    # expected_balls: Indicates exact group of balls to draw from hat
    # num_balls_drawn: Number of balls to be drawn
    # num_experiments: Number of experiments to perform (more runs, higher
    # accuracy
    pass
