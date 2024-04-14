import numpy as np

from move import Move
from strategy.strategy import Strategy
from errors import DomainError


class UniformRandomStrategy(Strategy):
    def __init__(self, probablity_defetion: float, random_seed: int = None):
        if 0.0 > probablity_defetion or probablity_defetion > 1.0:
            raise DomainError("Parameter probability_defection must be between 0 and 1.")

        self.probability_defection = probablity_defetion
        if random_seed:
            np.random.seed(random_seed)

    def calculate_next_move(self, rounds: list['Round'], player_number: 'PlayerNumber'):
        strategy_array = np.random.choice([Move.COOPERATE, Move.DEFECT], size=1, replace=False,
                                          p=[1 - self.probability_defection, self.probability_defection])
        return strategy_array[0]
