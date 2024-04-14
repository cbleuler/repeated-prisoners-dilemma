from player import PlayerNumber
from strategy.constant import ConstantCooperationStrategy


def test_play_move(cooperating_player_1):
    assert cooperating_player_1.play_move([]) \
           == ConstantCooperationStrategy().calculate_next_move([], cooperating_player_1.number)
