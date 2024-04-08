import pytest

from round import Round, RoundResult


def test_payoff_player(prisoners_dilemma_payoff, cooperating_player_1, defecting_player_2):
    game_round = Round(cooperating_player_1.play_move([]), defecting_player_2.play_move([]))

    assert game_round.payoff_player(player_number=cooperating_player_1.number, payoff=prisoners_dilemma_payoff) == 0
    assert game_round.payoff_player(player_number=defecting_player_2.number, payoff=prisoners_dilemma_payoff) == 5


def test_evaluate_round(prisoners_dilemma_payoff, cooperating_player_1, defecting_player_2):
    game_round = Round(cooperating_player_1.play_move([]), defecting_player_2.play_move([]))

    expected_round_result = RoundResult(move_player_1="Cooperate",
                                        move_player_2="Defect",
                                        payoff_player_1=0,
                                        payoff_player_2=5)

    assert game_round.evaluate_round(payoff=prisoners_dilemma_payoff) == expected_round_result
