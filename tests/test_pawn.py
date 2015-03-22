import pytest

from pawn.game import Game
from pawn.game import Player


@pytest.mark.parametrize('number_of_players',
                         [2, pytest.mark.xfail(3), 4])
def test_number_of_players(number_of_players):
    assert len(Game(number_of_players=number_of_players).players) == number_of_players

@pytest.mark.parametrize('name', ['Fox', 'Falco', 'Peppy', 'Slippy'])
def test_player_name(name):
    assert Player(name).name == name

def test_main():
    from pawn.__main__ import main
    assert main([]) == 0
