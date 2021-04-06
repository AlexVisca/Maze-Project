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
    
    def end_game(self, seconds_till_fail):
        """Ends the game buy starting the End Controller
        """
        self._score.end_timer() # calculate score
        if self.player._backpack != 4 or self.get_time() > seconds_till_fail: #arbitrary
            self._score.set_score(1000) # overwrite score with default score if backpack isnt full
        end_contoller = EndController(self._score)
        end_contoller.loop()
        exit()
    
    def get_time(self):
        """Return how long the game has been running in milliseconds

        Returns:
            float: time game has been running in milliseconds
        """        
        return (pygame.time.get_ticks()/1000) - self._score.get_start_time()
    
    def display_timer(self, window, font):
        text = "Timer: {}s".format(str(round(self.get_time(),1))) # round to 1 decimal point
        colour = (0, 255, 0)
        text_surface = font.render(text, True, colour)
        text_rect = text_surface.get_rect()
        text_rect.center = (75, 25)
        return (text_surface, text_rect)
    
    def display_backpack(self, window, font):
        # scale the coin image to be smaller
        small_coin_image = pygame.transform.scale(self.maze.coin_image, (20, 20))
        # display the text beside the coin showing the num of items in backpack
        text = "x {}".format(str(self.player._backpack))
        # green
        colour = (0, 255, 0)
        # creating the surface and location to render the text
        text_surface = font.render(text, True, colour)
        text_rect = text_surface.get_rect()
        text_rect.center = (75, 50)
        # pass info so game_view has everything it needs to render
        return (text_surface, text_rect, small_coin_image)