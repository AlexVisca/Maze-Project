from models.maze import Maze
from models.player import Player
import pytest


class Fixture:
    """ Maze fixture

    Returns:
        obj: maze object
    """
    @staticmethod
    def test_map():
        maze = Maze()
        
        return maze
    
    @staticmethod
    def test_player():
        player = Player(list(), 50, 50)

        return player

def test_maze():
    """ Test Maze model
    Test ID#01
    """
    test_maze = Fixture.test_map()
    assert hasattr(test_maze, 'cells')

def test_player():
    """ Test Player model 
    Test ID#02
    """
    test_player = Fixture.test_player()
    assert test_player._backpack == 0
