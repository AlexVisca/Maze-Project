Copyright (C) 2021, BCIT  

# Amaze game

## Dependencies:
pygame
pytest
json

## Introduction to Amaze game
Amaze game is a simple game using the PyGame library where a player must complete a maze and collect loot along the way. The game records player scores and publishes them to a web server

## **STEP 1**: Start the game application server
Start by running `api.py` at ./Web/api.py

## **STEP 2**: Start the game
Then run `main.py` at ./Maze/main.py

## **STEP 3**: Play the game
Game ruleset:
* The game will request a name. Defaults to "GUEST"  
* Controls with the arrow keys.  
* Crossing a loot item will automatically collect it and display the number of items in the backpack.  
* ***The player must collect all loot items before reaching the exit***

## **STEP 4**: Repeat and compete
When the game ends, replay by running `./Maze/main.py` again.  
Scores are posted `@localhost` on the listed port.

---

## Development Team
For development project notes and test plan, see documentation in `./Docs/project.md`.  

ACIT2515 Object-Oriented Programming in Python
Group Members|Job Description
------------|------------------------
Alex Visca | Development team leader
John Maloney| Developer, Documentation
Sukhmanpreet| Developer, QA and testing
