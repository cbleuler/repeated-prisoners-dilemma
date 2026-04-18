import pytest

from repeated_prisoners_dilemma.strategy.random import UniformRandomStrategy
from repeated_prisoners_dilemma.player import PlayerNumber
from repeated_prisoners_dilemma.move import Move
from repeated_prisoners_dilemma.errors import DomainError


class TestUniformRandomStrategy:
    def test_calculate_next_move_never_defect(self):
        strategy = UniformRandomStrategy(probability_defection=0)

        for _ in range(100):
            assert strategy.calculate_next_move([], PlayerNumber.PLAYER_1) == Move.COOPERATE

    def test_calculate_next_move_always_defect(self):
        strategy = UniformRandomStrategy(probability_defection=1.0)

        for _ in range(100):
            assert strategy.calculate_next_move([], PlayerNumber.PLAYER_1) == Move.DEFECT

    def test_initialization_domain_error_negative_probability(self):
        with pytest.raises(DomainError):
            UniformRandomStrategy(probability_defection=-0.1)

    def test_initialization_domain_error_probability_larger_1(self):
        with pytest.raises(DomainError):
            UniformRandomStrategy(probability_defection=1.001)

    def test_calculate_next_move_equal_probability(self):
        strategy = UniformRandomStrategy(probability_defection=0.5, random_seed=13)

        assert strategy.calculate_next_move([], PlayerNumber.PLAYER_1) == Move.DEFECT
        assert strategy.calculate_next_move([], PlayerNumber.PLAYER_1) == Move.DEFECT
        assert strategy.calculate_next_move([], PlayerNumber.PLAYER_1) == Move.DEFECT
        assert strategy.calculate_next_move([], PlayerNumber.PLAYER_1) == Move.COOPERATE
        assert strategy.calculate_next_move([], PlayerNumber.PLAYER_1) == Move.COOPERATE
        assert strategy.calculate_next_move([], PlayerNumber.PLAYER_1) == Move.DEFECT

    def test_seed_zero_is_respected(self):
        a = UniformRandomStrategy(probability_defection=0.5, random_seed=0)
        b = UniformRandomStrategy(probability_defection=0.5, random_seed=0)
        moves_a = [a.calculate_next_move([], PlayerNumber.PLAYER_1) for _ in range(10)]
        moves_b = [b.calculate_next_move([], PlayerNumber.PLAYER_1) for _ in range(10)]
        assert moves_a == moves_b

    def test_instances_do_not_share_rng_state(self):
        a = UniformRandomStrategy(probability_defection=0.5, random_seed=42)
        b = UniformRandomStrategy(probability_defection=0.5, random_seed=42)
        _ = [a.calculate_next_move([], PlayerNumber.PLAYER_1) for _ in range(5)]
        assert b.calculate_next_move([], PlayerNumber.PLAYER_1) == a.__class__(
            probability_defection=0.5, random_seed=42
        ).calculate_next_move([], PlayerNumber.PLAYER_1)
