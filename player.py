from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    """
    Handles all of the logic for the player controlled turtle

    Methods:
    - move_up
    - move_down
    - reached_top
    """

    def __init__(self):
        # Gets the init function from Turtle
        super().__init__()

        # Creates the turtle, sets the position and orients it the proper direction
        self.shape("turtle")
        self.penup()
        self.return_to_start()
        self.left(90)
    
    def return_to_start(self):
        """Moves the turtle back to the start"""
        self.goto(STARTING_POSITION)

    def move_up(self):
        """Moves the turtle up by the global defined amount"""
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def move_down(self):
        """Moves the turtle down by the global defined amount"""
        self.goto(self.xcor(), self.ycor() - MOVE_DISTANCE)

    def reached_top(self):
        """Resets the turtle to the start when it hits the top of the screen"""
        if self.ycor() == FINISH_LINE_Y:
            self.return_to_start()
            return True