import pygame
from pygame.locals import *
# Contoller imports
from controllers.player_controller import PlayerController
from controllers.maze_controller import MazeController 
from controllers.end_controller import EndController

# -- CONTROLLERS --
"""
Game Controller is the master Controller of the game. It creates an instance of the MazeController
and the PlayerController and controls how the Maze and Player interact
"""
class GameController:
    
    def __init__(self):
        """
        Initialize an instance of GameController
        """
        self._running = True
        self._window = None
        self._image = None
        self._block = None

        # The maze is a graph of 'Tiles' each tile is 50pixels by 50pixels
        self.TILE_WIDTH = 50
        self.TILE_HEIGHT = 50
        
        # Default name if the name is never set from the start screen
        self._name = 'GUEST'
        # When GameController is initialized the game has begun so we start the timer
        self.start_time = pygame.time.get_ticks()/1000 # in seconds
        self.end_time = None
        
        self.maze = MazeController(self.TILE_WIDTH, self.TILE_HEIGHT)
        
        # Player Conroller controls the actions of the player and has an instance of the player model
        self.player_controller = PlayerController(self.maze, self.TILE_WIDTH, self.TILE_HEIGHT)
        # shortcut to access the player model from the player control. This holds player properties
        self.player = self.player_controller.get_player()
                
        #NOTE: Calculated dimensions of the game (example tile size 50 pixels, and the map is 10 tiles wide then 10*50)
        self.__WIDTH = self.TILE_WIDTH * len(self.maze.cells[0])
        self.__HEIGHT = self.TILE_HEIGHT * len(self.maze.cells)

    def run(self):
        pygame.init()
        self._window = pygame.display.set_mode((self.__WIDTH, self.__HEIGHT)) #NOTE: changed to variables
        self._font = pygame.font.SysFont('arial', 18)
        self._clock = pygame.time.Clock()

        # -- Block Image --
        self._block = pygame.Surface((self.TILE_WIDTH, self.TILE_HEIGHT)) #NOTE: changed to variables
        self._block.fill((255, 0, 0))
        self._block.convert()
        
    def render_screen(self):
        self._window.fill((0, 0, 0))
        self._window.blit(self.player.image, self.player.rect)
        self.maze.draw(self._window, self._block)
        pygame.display.flip()
        
    def set_player_name(self, name):
        """Set the players name, if this is never called players will be called "GUEST"

        Args:
            name (string): The name of the player
        """
        self._name = name
        
    def loop(self):
        if self.run() == False:
            self._running = False
        while self._running:
            self._clock.tick(20)
            self._window.fill((0, 0, 0))
            
            text = "Timer: {}ms".format(pygame.time.get_ticks())
            text_surface = self._font.render(text, True, (255, 255, 255))
            self._window.blit(text_surface, (0, 0))
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    self._running = False
                elif event.type == KEYDOWN:
                    if event.key in (K_ESCAPE, K_q):
                        self._running = False
                        
            
            #NOTE: By ending the game here (in game controller's loop instead of in player controller)
            # There may be a slight lag when you complete the game because it will not end until the next render
            # and will add some time to your total score
            if self.player_controller.end:
                # the game has been completed
                self.end_time = pygame.time.get_ticks()/1000
                time = self.end_time - self.start_time
                end_contoller = EndController(time, self._name)
                end_contoller.loop()
                exit()
            
            # -- KEYBOARD CONTROLLER -- 
            keypress = pygame.key.get_pressed()
            if keypress[K_UP]:
                self.player_controller.move('UP')
            elif keypress[K_DOWN]:
                self.player_controller.move('DOWN')
            elif keypress[K_LEFT]:
                self.player_controller.move('LEFT')
            elif keypress[K_RIGHT]:
                self.player_controller.move('RIGHT')
            self.render_screen()
