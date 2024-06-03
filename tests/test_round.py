import pytest

from player import PlayerNumber
from round import Round, RoundResult
from move import Move


def test_payoff_player(prisoners_dilemma_payoff, cooperating_player_1, defecting_player_2):
    game_round = Round(cooperating_player_1.play_move([]), defecting_player_2.play_move([]))

    assert game_round.payoff_player(player_number=cooperating_player_1.number, payoff=prisoners_dilemma_payoff) == 0
    assert game_round.payoff_player(player_number=defecting_player_2.number, payoff=prisoners_dilemma_payoff) == 5


def test_evaluate_round(prisoners_dilemma_payoff, cooperating_player_1, defecting_player_2):
    game_round = Round(cooperating_player_1.play_move([]), defecting_player_2.play_move([]))

    expected_round_result = RoundResult(
        move_player_1="Cooperate", move_player_2="Defect", payoff_player_1=0, payoff_player_2=5
    )

    assert game_round.evaluate_round(payoff=prisoners_dilemma_payoff) == expected_round_result


def test_get_player_move():
    game_round = Round(move_player_1=Move.COOPERATE, move_player_2=Move.DEFECT)

    assert game_round.get_player_move(player_number=PlayerNumber.PLAYER_1) == Move.COOPERATE
    assert game_round.get_player_move(player_number=PlayerNumber.PLAYER_2) == Move.DEFECT
