import pygame
from pygame.locals import *
# Contoller imports
from controllers.player_controller import PlayerController
from controllers.maze_controller import MazeController 
from controllers.end_controller import EndController
# Model imports
from models.score import Score

# -- CONTROLLER --
"""
Game Controller is the master Controller of the game. It creates an instance of the MazeController
and the PlayerController and controls how the Maze and Player interact
"""
class GameController:
    
    def __init__(self):
        """
        Initialize an instance of GameController
        """
        self._window = None
        self._image = None
        self._block = None
        self._font = None
        # The maze is a graph of 'Tiles' each tile is 50pixels by 50pixels
        self.TILE_WIDTH = 50
        self.TILE_HEIGHT = 50
      
        self._score = Score()
        
        self.maze = MazeController(self.TILE_WIDTH, self.TILE_HEIGHT)
        
        # Player Conroller controls the actions of the player and has an instance of the player model
        self.player_controller = PlayerController(self.maze, self.TILE_WIDTH, self.TILE_HEIGHT)
        # shortcut to access the player model from the player control. This holds player properties
        self.player = self.player_controller.get_player()
                
        #NOTE: Calculated dimensions of the game (example tile size 50 pixels, and the map is 10 tiles wide then 10*50)
        self.__WIDTH = self.TILE_WIDTH * len(self.maze.cells[0])
        self.__HEIGHT = self.TILE_HEIGHT * len(self.maze.cells)

    def get_game_dimensions(self):
        return (self.__WIDTH, self.__HEIGHT)
    
    def get_tile_dimensions(self):
        return (self.TILE_WIDTH, self.TILE_HEIGHT)
    
    def set_player_name(self, name):
        """Set the players name, if this is never called players will be called "GUEST"

        Args:
            name (string): The name of the player
        """
        self._score.set_name(name)
    
    def keypress(self):
        keypress = pygame.key.get_pressed()
        if keypress[K_UP]:
            self.player_controller.move('UP')
        elif keypress[K_DOWN]:
            self.player_controller.move('DOWN')
        elif keypress[K_LEFT]:
            self.player_controller.move('LEFT')
        elif keypress[K_RIGHT]:
            self.player_controller.move('RIGHT')
    
    def game_over(self):
        """Return True if the player has collected all coins and reached the end

        Returns:
            bool: True if game over, False if game in progress
        """
        return self.player_controller.end
    
    def end_game(self):
        """Ends the game buy starting the End Controller
        """
        self._score.end_timer() # calculate score
        if self.player._backpack != 4:
            self._score.set_score(1000) # overwrite score with default score if backpack isnt full
        end_contoller = EndController(self._score)
        end_contoller.loop()
        exit()
    
    def display_timer(self, window, font):
        text = "Timer: {}ms".format(pygame.time.get_ticks() - self._score.get_start_time())
        colour = (0, 255, 0)
        text_surface = font.render(text, True, colour)
        text_rect = text_surface.get_rect()
        text_rect.center = (75, 25)
        return (text_surface, text_rect)
