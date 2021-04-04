import pygame
from pygame.locals import *
# from controllers.game_controller import GameController
import requests
# from controllers.start_controller import StartController

class EndController:
    
    def __init__(self):
        self._running = True
        self._window = None
        self._image = None
        # self._start = StartController()
        
    
    def run(self):
        pygame.init()
        self._window = pygame.display.set_mode((400, 400))
        self._font = pygame.font.SysFont('arial', 18)
    
    def render_screen(self):
        colour = (255, 255, 255)
        text = self._font.render('Press SPACE to exit' , True , colour)
        text_rect = text.get_rect()
        text_rect.center = (400 // 2, 400 // 2)
        self._window.blit(text, text_rect)
        self.render_score()
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
                        # self._start.loop() # possibly .run()
                        exit()
         
            self.render_screen()
        
    def put_highscore(self):
        response = requests.put(
            'http://localhost:5000/api/new', 
            data={
                'name':'Always Daniel',
                'score': 75
            }
        )
        if response.status_code == 204:
            return True
        else:
            print("failed to get high scores")
            return False
    
    def render_score(self):
        
        
        center = (400 // 2, 400 // 2)
        colour = (255, 255, 255)
        
        # Render High score text
        score = 75
        text = self._font.render("Your score: " + str(score) , True , colour)
        text_rect = text.get_rect()
        text_rect.center = (center[0], center[1] + 25)
        self._window.blit(text, text_rect)
        