from views.game_view import GameView
import pytest

class Fixture:
    """ GameView fixture

    Returns:
        obj: GameView obj
    """
    @staticmethod
    def test_view(_ttl):
        game_view = GameView(seconds_till_fail=_ttl)

        return game_view

def test_game_view():
    """ Test `GameView()`

    Test ID#08
    """
    default_ttl = Fixture.test_view(15)
    test_ttl = default_ttl._seconds_till_fail
    assert default_ttl == test_ttl

    custom_ttl = Fixture.test_view(10)
    test_ttl = custom_ttl._seconds_till_fail
    assert custom_ttl == test_ttl
