import pygame
from pygame.locals import *
import requests

"""
The EndController controls the end screen which appears 
when the player has beat the game
"""
class EndController:
    
    def __init__(self, score):
        """Initalize an instance of the end controller

        Args:
            time (float): The amount of time it took for the player to complete the game
            name (string): The name of the player
        """
        self._running = True
        self._window = None
        self._image = None
        self._score = score
        # Update server with the score
        self.add_score_to_server()
        
    
    def run(self):
        pygame.init()
        self._window = pygame.display.set_mode((400, 400))
        self._font = pygame.font.SysFont('arial', 18)
    
    def render_screen(self):
        colour = (255, 255, 255)
        text = self._font.render('Press ENTER to exit' , True , colour)
        text_rect = text.get_rect()
        # Hardcoded screen size and hardcoded center of screen
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
                    if event.key in (K_ESCAPE, K_q) or event.key == K_RETURN:
                        self._running = False
                    
            self.render_screen()
        
    def add_score_to_server(self):
        """
        Send the players name and score to the server/api
        """
        try:
            response = requests.put(
                'http://localhost:5000/api/new', 
                json=self._score.__dict__()
            )
            if response.status_code != 204: # if the server did not accept the new score
                print("failed to update scoreboard")
        except:
            print("failed to update scoreboard, is the server running?")
    
    def render_score(self):
        center = (400 // 2, 400 // 2)
        colour = (255, 255, 255)
        
        # Render High score text
        score = self._score.get_score()
        text = self._font.render("Your score: " + str(score) , True , colour)
        text_rect = text.get_rect()
        text_rect.center = (center[0], center[1] + 25)
        self._window.blit(text, text_rect)
        