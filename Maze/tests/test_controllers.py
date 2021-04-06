from controllers.start_controller import StartController
from controllers.maze_controller import MazeController
from controllers.player_controller import PlayerController
from controllers.game_controller import GameController
from controllers.end_controller import EndController
import pytest


class Fixture:
    """ Controller fixture

    Returns:
        obj: controller object
    """
    @staticmethod
    def player():
        player_controller = PlayerController(list(), 50, 50)
        
        return player_controller
    
    @staticmethod
    def score():
        end_controller = EndController(12.5)

        return end_controller

def test_start_controller():
    """ Test `StartController()`

    Test ID#03
    """
    start_controller = StartController()
    assert start_controller._running

def test_maze_controller():
    """ Test `MazeController()`

    Test ID#05 
    """
    maze_controller = MazeController()
    assert maze_controller

def test_player_controller():
    """ Test `PlayerController()`

    Test ID#06
    """
    player_controller = Fixture.player()
    assert hasattr(player_controller, 'move')

def test_game_controller():
    """ Test `GameController()`

    Test ID#04
    """
    game_controller = GameController()
    assert game_controller

def test_end_controller():
    """ Test `EndController()`
    
    Test ID#07
    """
    end_controller = Fixture.score()
    assert end_controller._running
