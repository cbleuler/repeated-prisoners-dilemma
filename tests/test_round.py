import pytest

from payoff import Payoff
from player import Player, PlayerNumber
from round import Round, RoundResult
from strategy.constant import ConstantCooperationStrategy, ConstantDefectionStrategy


@pytest.fixture
def constant_cooperation_strategy():
    return ConstantCooperationStrategy()


@pytest.fixture
def constant_defection_strategy():
    return ConstantDefectionStrategy()


@pytest.fixture
def player_1(constant_cooperation_strategy):
    return Player(strategy=constant_cooperation_strategy, number=PlayerNumber.PLAYER_1)


@pytest.fixture
def player_2(constant_defection_strategy):
    return Player(strategy=constant_defection_strategy, number=PlayerNumber.PLAYER_2)


@pytest.fixture
def prisoners_dilemma_payoff():
    payoff = Payoff(payoff_cooperate_cooperate=3,
                    payoff_defect_defect=1,
                    payoff_cooperate_defect=0,
                    payoff_defect_cooperate=5)
    return payoff


def test_payoff_player(prisoners_dilemma_payoff, player_1, player_2):
    game_round = Round(player_1.play_move([]), player_2.play_move([]))

    assert game_round.payoff_player(player_number=player_1.number, payoff=prisoners_dilemma_payoff) == 0
    assert game_round.payoff_player(player_number=player_2.number, payoff=prisoners_dilemma_payoff) == 5


def test_evaluate_round(prisoners_dilemma_payoff, player_1, player_2):
    game_round = Round(player_1.play_move([]), player_2.play_move([]))

    expected_round_result = RoundResult(move_player_1="Cooperate",
                                        move_player_2="Defect",
                                        payoff_player_1=0,
                                        payoff_player_2=5)

    assert game_round.evaluate_round(payoff=prisoners_dilemma_payoff) == expected_round_result
