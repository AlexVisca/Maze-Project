import pygame
from pygame.locals import *
from controllers.game_controller import GameController

class GameView:
    def __init__(self):
        self._running = True
        self._window = None
        self._image = None
        self._block = None
        
        self._game = GameController()
        self.__WIDTH, self.__HEIGHT = self._game.get_game_dimensions()
        self.TILE_WIDTH, self.TILE_HEIGHT = self._game.get_tile_dimensions()

        
        
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
        self._window.blit(self._game.player.image, self._game.player.rect)
        self._game.maze.draw(self._window, self._block)
        timer_text, timer_rect = self._game.display_timer( self._window, self._font)
        self._window.blit(timer_text, timer_rect)
        pygame.display.flip()
        
    def start_game(self):
        if self.run() == False:
            self._running = False
        while self._running:
            self._clock.tick(20)
            self._window.fill((0, 0, 0))
            
            # text = "Timer: {}ms".format(pygame.time.get_ticks())
            # text_surface = self._font.render(text, True, (255, 255, 255))
            # self._window.blit(text_surface, (0, 0))
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    self._running = False
                elif event.type == KEYDOWN:
                    if event.key in (K_ESCAPE, K_q):
                        self._running = False
                        
            
            #NOTE: By ending the game here (in the loop instead of in player controller)
            # There may be a slight lag when you complete the game because it will not end until the next render
            # and will add some time to your total score
            if self._game.game_over():
                self._game.end_game()
                
            self._game.keypress()
            self.render_screen()

    