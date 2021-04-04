# import game controller here
from controllers.game_controller import GameController 
from controllers.start_controller import StartController
# -- PRIMARY APP CONTROLLER
class App():
    def __init__(self):
        self._start = StartController()
    
    def run(self):
        self._start.loop()
        