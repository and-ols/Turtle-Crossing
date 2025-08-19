import time
from turtle import Screen
from player import Player
from car_manager import CarManager

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
car = CarManager()

# Detects the arrow keys being pressed
screen.listen()
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    player.pos_reset()
    car.move_car()

    if player.distance(car) < 25:
        game_is_on = False
        
