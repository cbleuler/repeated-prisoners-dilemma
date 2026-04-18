import pytest
from repeated_prisoners_dilemma.errors import DomainError
from repeated_prisoners_dilemma.game import Game, GameSummary
from repeated_prisoners_dilemma.round import Round
from repeated_prisoners_dilemma.move import Move


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

    summary = game.evaluate_game()

    assert summary.moves_player_1 == [Move.COOPERATE, Move.COOPERATE]
    assert summary.moves_player_2 == [Move.DEFECT, Move.DEFECT]
    assert summary.total_score_player_1 == 0
    assert summary.total_score_player_2 == 10
    assert summary.score_relative_to_mutual_cooperation_player_1 == pytest.approx(0.0)
    assert summary.score_relative_to_mutual_cooperation_player_2 == pytest.approx(10 / 6)
    assert isinstance(summary, GameSummary)


def test_rejects_wrong_number_of_players(prisoners_dilemma_payoff, cooperating_player_1):
    with pytest.raises(DomainError):
        Game(
            min_number_of_rounds=1,
            max_number_of_rounds=1,
            payoff=prisoners_dilemma_payoff,
            players=(cooperating_player_1,),
        )


def test_rejects_inverted_round_bounds(
    prisoners_dilemma_payoff, cooperating_player_1, defecting_player_2
):
    with pytest.raises(DomainError):
        Game(
            min_number_of_rounds=5,
            max_number_of_rounds=2,
            payoff=prisoners_dilemma_payoff,
            players=(cooperating_player_1, defecting_player_2),
        )


def test_accepts_list_for_players(
    prisoners_dilemma_payoff, cooperating_player_1, defecting_player_2
):
    game = Game(
        min_number_of_rounds=1,
        max_number_of_rounds=1,
        payoff=prisoners_dilemma_payoff,
        players=[cooperating_player_1, defecting_player_2],
    )
    assert isinstance(game.players, tuple)
