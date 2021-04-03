# import game controller here
from controllers.game_controller import GameController 

# -- PRIMARY APP CONTROLLER
class App():
    def __init__(self):
        self._game = GameController()
    
    def run(self):
        self._game.loop()