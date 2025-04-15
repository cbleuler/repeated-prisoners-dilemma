import pytest

from repeated_prisoners_dilemma.strategy.random import UniformRandomStrategy
from repeated_prisoners_dilemma.player import PlayerNumber
from repeated_prisoners_dilemma.move import Move
from repeated_prisoners_dilemma.errors import DomainError


class TestUniformRandomStrategy:
    def test_calculate_next_move_never_defect(self):
        strategy = UniformRandomStrategy(probablity_defetion=0)

        for _ in range(100):
            assert strategy.calculate_next_move([], PlayerNumber.PLAYER_1) == Move.COOPERATE

    def test_calculate_next_move_always_defect(self):
        strategy = UniformRandomStrategy(probablity_defetion=1.0)

        for _ in range(100):
            assert strategy.calculate_next_move([], PlayerNumber.PLAYER_1) == Move.DEFECT

    def test_initialization_domain_error_negative_probability(self):
        with pytest.raises(DomainError):
            UniformRandomStrategy(probablity_defetion=-0.1)

    def test_initialization_domain_error_probability_larger_1(self):
        with pytest.raises(DomainError):
            UniformRandomStrategy(probablity_defetion=1.001)

    def test_calculate_next_move_equal_probability(self):
        strategy = UniformRandomStrategy(probablity_defetion=0.5, random_seed=13)

        assert strategy.calculate_next_move([], PlayerNumber.PLAYER_1) == Move.DEFECT
        assert strategy.calculate_next_move([], PlayerNumber.PLAYER_1) == Move.COOPERATE
        assert strategy.calculate_next_move([], PlayerNumber.PLAYER_1) == Move.DEFECT
        assert strategy.calculate_next_move([], PlayerNumber.PLAYER_1) == Move.DEFECT
        assert strategy.calculate_next_move([], PlayerNumber.PLAYER_1) == Move.DEFECT
        assert strategy.calculate_next_move([], PlayerNumber.PLAYER_1) == Move.COOPERATE
