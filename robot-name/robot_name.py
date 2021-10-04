import string
import random


class Robot():

    def __init__(self):
        self.name = Robot.name()

    def name():
        robot_name = ""
        for caracter_position in range(5):
            if caracter_position < 2:
                robot_name += random.choice(string.ascii_uppercase)
            else:
                robot_name += str(random.randrange(10))
        return robot_name

    def reset(self):
        random.seed()
        self.name = Robot().name
