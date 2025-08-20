from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    """
    Handles all of the logic for the scoreboard

    Methods:
    - display_level
    - update_level
    - game_over
    """

    def __init__(self):
        # Gets the init function from Turtle
        super().__init__()

        self.penup()
        self.color("Black")
        self.hideturtle()
        self.level = 1

    def display_level(self):
        """Displays current level in the top left"""
        self.goto(-210, 250)
        self.write(f"Level: {self.level}", move=False, align="center", font=FONT)
        return self.level

    def update_level(self):
        """
        Updates the scoreboard by clearing it, adding the level and calling
        the display
        """
        self.clear()
        self.level += 1
        self.display_level()

    def game_over(self):
            """Displays game over text"""
            self.goto(0, 0)
            self.write(f"GAME OVER", move=False, align="center", font=FONT)