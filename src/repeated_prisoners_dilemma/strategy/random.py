import numpy as np

from repeated_prisoners_dilemma.move import Move
from repeated_prisoners_dilemma.strategy.strategy import Strategy
from repeated_prisoners_dilemma.errors import DomainError


class UniformRandomStrategy(Strategy):
    def __init__(self, probability_defection: float, random_seed: int | None = None):
        if 0.0 > probability_defection or probability_defection > 1.0:
            raise DomainError("Parameter probability_defection must be between 0 and 1.")

        self.probability_defection = probability_defection
        self._rng = np.random.default_rng(random_seed)

    def calculate_next_move(self, rounds: list["Round"], player_number: "PlayerNumber") -> Move:
        return self._rng.choice(
            [Move.COOPERATE, Move.DEFECT],
            p=[1 - self.probability_defection, self.probability_defection],
        )
