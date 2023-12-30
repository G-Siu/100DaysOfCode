import copy
import random
from collections import Counter

# Determine probability of drawing certain balls randomly


class Hat:
    def __init__(self, **kwargs):
        self.colour_dict = dict(kwargs)
        # Arguments converted to contents instance variable represented by
        # one item for each ball in the hat
        self.contents = [colour for colour in self.colour_dict.keys() for _
                         in range(self.colour_dict[colour])]

    def __repr__(self):
        return str(self.contents)

    # Accepts argument as number of balls to be drawn
    def draw(self, balls_to_draw):
        # Remove ball from contents at random, return those balls as list of
        # strings
        balls_drawn = []
        try:
            for _ in range(balls_to_draw):
                ball_drawn = random.choice(self.contents)
                # Should not go back into hat during draw
                self.contents.remove(ball_drawn)
                balls_drawn.append(ball_drawn)
        # If draws exceed number of balls in hat, return all balls
        except IndexError:
            print("Invalid: not enough balls in hat.\nProgram stopped.")
            quit()
        return balls_drawn


# Returns probability
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    # hat: object containing balls to be copied inside the function
    # expected_balls: Indicates exact group of balls to draw from hat
    # num_balls_drawn: Number of balls to be drawn
    # num_experiments: Number of experiments to perform (more runs, higher
    # accuracy

    count = 0
    for iteration in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        balls_drawn = Counter(Hat.draw(hat_copy, num_balls_drawn))
        # Check if expected balls are in balls drawn
        if set(expected_balls.items()).issubset(set(balls_drawn.items())):
            count += 1
    probability = count / num_experiments
    return probability
