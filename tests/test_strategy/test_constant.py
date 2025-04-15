from repeated_prisoners_dilemma.strategy.constant import ConstantCooperationStrategy, ConstantDefectionStrategy
from repeated_prisoners_dilemma.move import Move
from repeated_prisoners_dilemma.player import PlayerNumber


class TestConstantCooperationStrategy:
    def test_calculate_next_move(self):
        assert ConstantCooperationStrategy().calculate_next_move([], PlayerNumber.PLAYER_1) == Move.COOPERATE


class TestConstantDefectionStrategy:
    def test_calculate_next_move(self):
        assert ConstantDefectionStrategy().calculate_next_move([], PlayerNumber.PLAYER_1) == Move.DEFECT
