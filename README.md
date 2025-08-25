# Turtle Crossing
## Overview
This is a turtle crossing game similar to Frogger or Crossy Road. 

Written in Python, this game utilizes the built in Turtle graphics module, documentation for this can be found below.
The game is played by moving the Turtle up and down the screen via the arrow keys. If the turtle touches a car the game is over. The level the player is on is displayed in the top left of the screen. If the player reaches the top of the screen, the player's position is reset to the start, the next level is displayed and the cars begin to speed up. The cars are randomly generated in color and position.

## Files
This game utilizes 4 different files:
- **main**: The role of the main file is to hold all the logic for the game. Main is essentially the game itself and utilizes the other classes to run the game.

- **player**: The player file holds the player class. The player is the turtle seen on the screen and is controlled by the player to move only up and down via the up and down arrow keys. Once the player has reached the top of the screen, it is reset to the original starting position to continue to the next level.

- **car_manager**: This holds the car_manager class or in the main file, the car. The car_manager creates a random color car and generates that car in a random spot in the range of the screen. The car is sped up each time a new level is reached.

- **scoreboard**: The scoreboard holds the scoreboard class and handles the display of the current level, and the game over sign.

## Demo
![Gif of game example](<2025-08-21 13-04-57 - Trim.mkv(1).gif>)


## Documentation
- [Turtle Graphics](https://docs.python.org/3/library/turtle.html)