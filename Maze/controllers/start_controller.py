import pygame
from pygame.locals import *
from controllers.game_controller import GameController
from views.game_view import GameView
import requests


"""
Start Controller to generate the start screen
"""
class StartController:
    
    def __init__(self):
        self._running = True
        self._window = None
        self._image = None
        self._game_view = None
        self._name = ''
        self.high_scores = self.get_highscores()
        
    
    def run(self):
        pygame.init()
        self._window = pygame.display.set_mode((400, 400))
        self._font = pygame.font.SysFont('arial', 18)
    
    def render_screen(self):
        colour = (255, 255, 255)
        text = self._font.render('Press ENTER to start' , True , colour)
        text_rect = text.get_rect()
        text_rect.center = (400 // 2, 400 // 2)
        self._window.blit(text, text_rect)
        self.render_highscores()
        self.render_input()
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
                    elif event.key == K_RETURN:
                        #NOTE: we wait to initalize GameView until enter 
                        # is pressed because it starts the game timer
                        self._game_view = GameView() 
                        if self._name != '': #Otherwise "GUEST" is set as default name
                            self._game_view._game.set_player_name(self._name)
                        
                        # start game!
                        self._game_view.start_game()
                        exit()
                    # when backspace is pressed, remove character from name
                    elif event.key == K_BACKSPACE:
                        self._name = self._name[:-1]
                    # update name string with character
                    else:
                        self._name += event.unicode
         
            self.render_screen()
        
    def get_highscores(self):
        """Get highscores from server

        Returns:
            list of dicts: response from server a list of dictionaires that have name and scores
        """
        try:
            response = requests.get('http://localhost:5000/api/list')
            if response.status_code == 200:
                response_dict = response.json()
                return response_dict.get("scores")
            else:
                print("failed to get high scores") # instead of raising error, just dont show highscores
                return []
        except:
            print("failed to get high scores, is the server running?") # instead of raising error, just dont show highscores
            return []
        
    def render_input(self):
        """
        Collect user name in an input box
        """
        input_box = pygame.Rect(100, 100, 140, 32)
        colour = (255, 255, 255)
        center = (400 // 2, 400 // 2)
        text = "enter name: " + self._name
        txt_surface = self._font.render( text, self._name, True, colour)
        text_rect = txt_surface.get_rect()
        text_rect.center = (center[0], center[1] -25)
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        self._window.blit(txt_surface, text_rect)
        
    def render_highscores(self):
                
        center = (400 // 2, 400 // 2)
        colour = (255, 255, 255)
        
        # Render High score text
        text = self._font.render("High Scores" , True , colour)
        text_rect = text.get_rect()
        text_rect.center = (center[0], center[1] + 25)
        self._window.blit(text, text_rect)
        
        # trim highscore list to be max len 3
        if len(self.high_scores) > 3:
            self.high_scores = self.high_scores[:3]
        
        # render each highscore 
        for i in range(len(self.high_scores)):
            score = self.high_scores[i]
            score_text = score["name"] + ": " + str(score["score"])
            text = self._font.render(score_text , True , colour)
            text_rect = text.get_rect()
            text_rect.center = (center[0], center[1] + ((i+2)*25))
            # text_rect.center = (400 // 2, 300)
            self._window.blit(text, text_rect)