from strategy.constant import ConstantCooperationStrategy, ConstantDefectionStrategy
from move import Move


class TestConstantCooperationStrategy:
    def test_calculate_next_move(self):
        assert ConstantCooperationStrategy().calculate_next_move([]) == Move.COOPERATE


class TestConstantDefectionStrategy:
    def test_calculate_next_move(self):
        assert ConstantDefectionStrategy().calculate_next_move([]) == Move.DEFECT

        