import pytest
from strategy.constant import ConstantCooperationStrategy
from player import Player, PlayerNumber


@pytest.fixture
def constant_cooperation_strategy():
    return ConstantCooperationStrategy()


@pytest.fixture
def player_1(constant_cooperation_strategy):
    return Player(strategy=constant_cooperation_strategy, number=PlayerNumber.PLAYER_1)


def test_play_move(player_1, constant_cooperation_strategy):
    assert player_1.play_move([]) == constant_cooperation_strategy.calculate_next_move([])
