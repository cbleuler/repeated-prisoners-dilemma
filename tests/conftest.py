import pytest
from payoff import Payoff
from player import Player, PlayerNumber
from strategy.constant import ConstantCooperationStrategy, ConstantDefectionStrategy


@pytest.fixture
def prisoners_dilemma_payoff():
    payoff = Payoff(payoff_cooperate_cooperate=3,
                    payoff_defect_defect=1,
                    payoff_cooperate_defect=0,
                    payoff_defect_cooperate=5)
    return payoff


@pytest.fixture
def cooperating_player_1():
    player = Player(
        strategy=ConstantCooperationStrategy(),
        number=PlayerNumber.PLAYER_1
    )
    return player


@pytest.fixture
def defecting_player_2():
    player = Player(
        strategy=ConstantDefectionStrategy(),
        number=PlayerNumber.PLAYER_2
    )
    return player
