import pytest
from game import Game
from round import Round
from move import Move


@pytest.fixture(scope="function")
def game(prisoners_dilemma_payoff, cooperating_player_1, defecting_player_2):
    game = Game(
        min_number_of_rounds=2,
        max_number_of_rounds=2,
        payoff=prisoners_dilemma_payoff,
        players=(cooperating_player_1, defecting_player_2),
    )
    return game


def test_play_round(game):
    expected_round = Round(move_player_1=Move.COOPERATE, move_player_2=Move.DEFECT)

    assert game.play_round() == expected_round
    assert game.play_round() == expected_round
    assert game.rounds == [expected_round, expected_round]


def test_run_game(game):
    expected_round = Round(move_player_1=Move.COOPERATE, move_player_2=Move.DEFECT)
    expected_rounds = [expected_round, expected_round]

    game.run_game()

    assert game.rounds == expected_rounds


def test_evaluate_game(game):
    game.run_game()
    expected_evaluation = {
        "moves_player_1": ["Cooperate", "Cooperate"],
        "moves_player_2": ["Defect", "Defect"],
        "total_score_player_1": 0,
        "total_score_player_2": 10,
        "relative_achieved_points_player_1": 0.0,
        "relative_achieved_points_player_2": 1.6666666666666667,
    }

    assert game.evaluate_game() == expected_evaluation
