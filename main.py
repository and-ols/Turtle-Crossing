import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()

"""           SCREEN GRID
                 Y| 300
                  |
                  |
-300              |                300
X-----------------|------------------
                  |
                  |
                  |
                  | -300
"""
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car = CarManager()


# Detects the arrow keys being pressed
screen.listen()
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")


game_is_on = True
while game_is_on:
    time.sleep(car.move_speed)
    screen.update()

    # Displays the scoreboard
    scoreboard.display_level()

    # Spawns cars
    car.add_car()

    # If the player has reached the top of the screen, reset the player to the
    # bottom and increase the speed
    if player.reached_top():
        scoreboard.update_level()
        car.increase_speed()

    # Continual move the cars
    car.move_car()

    # Checks each cars distance from the player, if it is within 25px, stop the
    # game loop and display the game over sign
    for vic in car.cars:
        if player.distance(vic) < 20:
            game_is_on = False
            scoreboard.game_over()

        if vic.xcor() == -320:
            car.cars.remove(vic)
            


#Keeps the screen open until the user closes it
screen.exitonclick()