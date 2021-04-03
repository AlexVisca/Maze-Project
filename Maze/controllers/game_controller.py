import pygame
from pygame.locals import *

from controllers.player_controller import PlayerController
# import maze
from controllers.maze_controller import MazeController 

# -- CONTROLLERS --
class GameController:
    
    def __init__(self):
        self._running = True
        self._window = None
        self._image = None
        self._block = None

        self.maze = MazeController()

        self.TILE_WIDTH = 50
        self.TILE_HEIGHT = 50
        
        self.player_controller = PlayerController(self.maze, self.TILE_WIDTH, self.TILE_HEIGHT)
        self.player = self.player_controller.get_player()
        
        # self.player = Player(self.maze, self.TILE_WIDTH, self.TILE_HEIGHT) #NOTE: pass in maze so player has access to it
        
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
        self.maze.draw(self._window, self._block, self.TILE_WIDTH, self.TILE_HEIGHT)
        pygame.display.flip()
        
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
            
            # -- KEYBOARD CONTROLLER -- 
            #NOTE: changed to use move method
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
