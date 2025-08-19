from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    """
    Handles all of the logic for the cars passing on the screen

    Methods:
    - move_car
    """
    def __init__(self):
        # Gets the init function from Turtle
        super().__init__()

        # Creates the car, sets the shape and gets a random position and color for it
        self.shape("square")
        self.penup()
        self.left(180)
        self.color(random.choice(COLORS))
        self.shapesize(stretch_wid=1, stretch_len=2)
        # self.goto(300, random.randrange(-240, 280 + 1))
        self.goto(300, -240)

    def move_car(self):
        """Moves the car left by the global defined amount"""
        # Subtract the move distance because it starts at positive 300
        self.goto(self.xcor() - STARTING_MOVE_DISTANCE, self.ycor())
