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
            self.contents = balls_drawn
        return balls_drawn


# Returns probability
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    # hat: object containing balls to be copied inside the function
    # expected_balls: Indicates exact group of balls to draw from hat
    # num_balls_drawn: Number of balls to be drawn
    # num_experiments: Number of experiments to perform (more runs, higher
    # accuracy

    counter = 0
    for _ in range(num_experiments):
        count = 0
        # To avoid using same hat every iteration
        hat_copy = copy.deepcopy(hat)
        balls_drawn = Counter(hat_copy.draw(num_balls_drawn))
        # Check if expected balls are in balls drawn
        for key in expected_balls.keys():
            # print(key, balls_drawn[key], expected_balls[key])
            count += 1
            if key in balls_drawn and balls_drawn[key] >= expected_balls[key]:
                continue
            count = 0
            break
        counter += count / len(expected_balls)
    probability = counter / num_experiments
    return probability
