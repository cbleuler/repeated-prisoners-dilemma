import warnings

import numpy as np

from repeated_prisoners_dilemma.move import Move


class PayoffWarning(UserWarning):
    pass


class Payoff:
    def __init__(
        self,
        payoff_cooperate_cooperate: float,
        payoff_cooperate_defect: float,
        payoff_defect_cooperate: float,
        payoff_defect_defect: float,
    ):
        self._validate_prisoners_dilemma(
            reward=payoff_cooperate_cooperate,
            sucker=payoff_cooperate_defect,
            temptation=payoff_defect_cooperate,
            punishment=payoff_defect_defect,
        )

        self.payoffs = np.zeros(shape=(2, 2))
        self.payoffs[Move.COOPERATE.value, Move.COOPERATE.value] = payoff_cooperate_cooperate
        self.payoffs[Move.COOPERATE.value, Move.DEFECT.value] = payoff_cooperate_defect
        self.payoffs[Move.DEFECT.value, Move.COOPERATE.value] = payoff_defect_cooperate
        self.payoffs[Move.DEFECT.value, Move.DEFECT.value] = payoff_defect_defect

    @staticmethod
    def _validate_prisoners_dilemma(reward: float, sucker: float, temptation: float, punishment: float) -> None:
        if not (temptation > reward > punishment > sucker):  # pylint: disable=superfluous-parens
            warnings.warn(
                "Payoff does not follow traditional prisoner's dilemma order T > R > P > S "
                f"(got T={temptation}, R={reward}, P={punishment}, S={sucker}).",
                PayoffWarning,
                stacklevel=3,
            )
        elif not (2 * reward > temptation + sucker):  # pylint: disable=superfluous-parens
            warnings.warn(
                "Payoff does not satisfy 2R > T + S " f"(got 2R={2 * reward}, T+S={temptation + sucker}).",
                PayoffWarning,
                stacklevel=3,
            )

    def calculate_payoff(self, player_move: Move, adversary_move: Move) -> float:
        return float(self.payoffs[player_move.value, adversary_move.value])
