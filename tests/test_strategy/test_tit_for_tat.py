import pytest
from repeated_prisoners_dilemma.strategy.tit_for_tat import TitForNTatStrategy
from repeated_prisoners_dilemma.round import Round
from repeated_prisoners_dilemma.move import Move
from repeated_prisoners_dilemma.player import PlayerNumber


@pytest.mark.parametrize(
    "opponent_moves,resulting_move,n_tats",
    [
        ([Move.COOPERATE, Move.DEFECT, Move.DEFECT], Move.DEFECT, 2),
        ([Move.COOPERATE, Move.DEFECT, Move.DEFECT], Move.COOPERATE, 3),
        ([Move.DEFECT, Move.DEFECT, Move.DEFECT], Move.DEFECT, 3),
        ([Move.DEFECT], Move.COOPERATE, 2),
        ([Move.DEFECT], Move.DEFECT, 1),
        ([Move.DEFECT, Move.COOPERATE], Move.COOPERATE, 1),
    ],
)
def test_player_rounds(opponent_moves, resulting_move, n_tats):
    strategy = TitForNTatStrategy(n_tats=n_tats)
    game_rounds = []

    for opponent_move in opponent_moves:
        game_rounds.append(Round(move_player_1=Move.COOPERATE, move_player_2=opponent_move))

    assert strategy.calculate_next_move(rounds=game_rounds, player_number=PlayerNumber.PLAYER_1) == resulting_move
