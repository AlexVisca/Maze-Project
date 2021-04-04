import pygame
from pygame.locals import *
from controllers.game_controller import GameController
import requests

class StartController:
    
    def __init__(self):
        self._running = True
        self._window = None
        self._image = None
        self._game = GameController()
    
    def run(self):
        pygame.init()
        self.get_highscores()
        self._window = pygame.display.set_mode((400, 400))
        self._font = pygame.font.SysFont('arial', 18)
    
    def render_screen(self):
        colour = (255, 255, 255)
        text = self._font.render('Press SPACE to start' , True , colour)
        text_rect = text.get_rect()
        text_rect.center = (400 // 2, 400 // 2)
        self._window.blit(text, text_rect)
        pygame.display.flip()
    
    def loop(self):
        if self.run() == False:
            self._running = False
        while self._running:
            self._window.fill((0, 0, 0))
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    self._running = False
                elif event.type == KEYDOWN:
                    if event.key in (K_ESCAPE, K_q):
                        self._running = False
                    if event.key == K_SPACE:
                        print("PRESSED")
                        self._game.loop()
                        exit()
         
            self.render_screen()
        
    def get_highscores(self):
        response = requests.get('http://localhost:5000/api/list')
        if response.status_code == '200':
            print(response)