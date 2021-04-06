# Maze Game Project

## Purpose and Scope
This application aims to create a simple game where a player must solve a maze. The game records a players score, and publishes these scores to a web browser.

## Gameplay
**Start screen**:  
Requests the player's name. Defaults to 'GUEST'  
Shows previous player scores.  

Press ENTER to continue to the game screen

**Game screen**:  
Player controls:
*   Arrow keys to move  

Map  
*   Cannot pass through brick walls.  
*   All coins are placed randomly, and **must be picked up before using the exit**

Coins and backpack  
*   ***Player must collect all 4 coins before reaching the exit in order to win the game!***  
*   Number of coins collected in the player's backpack is shown in the top left corner.

Timer  
*   Player muct complete the maze before the timer runs out, otherwise they lose the game.
*   The time it takes for the player to complete the maze is measured to affect a player score.
