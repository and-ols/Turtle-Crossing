from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    """
    Handles all of the logic for the cars passing on the screen

    Methods:
    - add_car
    - move_car
    - increase_speed
    """

    def __init__(self):
        self.cars = []
        self.move_speed = .1

    def add_car(self):
        """
        Creates a car, gives it a random color, and location and adds it to
        the list of cars
        """
        # This random number limits the number of cars spawning, so it is not so saturated. 
        # So rather then spawning in every .1 seconds it now every 1 in 6 of .1 seconds 
        random_num = random.randint(1, 6)
        if random_num == 1:
            new_car = Turtle(shape="square")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.goto(320, random.randrange(-240, 240 + 1))
            self.cars.append(new_car)

    def move_car(self):
        """Moves the car left by the global defined amount"""
        for car in self.cars:
            # Move backwards because it starts at positive 300
            car.backward(STARTING_MOVE_DISTANCE)

    def increase_speed(self):
        """Increases the speed of the cars"""
        # Divide because the smaller the time number, the faster the time
        self.move_speed /= MOVE_INCREMENT

