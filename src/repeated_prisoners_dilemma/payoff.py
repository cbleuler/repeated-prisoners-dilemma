import numpy as np

from repeated_prisoners_dilemma.move import Move


class Payoff:
    def __init__(
        self,
        payoff_cooperate_cooperate: float,
        payoff_cooperate_defect: float,
        payoff_defect_cooperate: float,
        payoff_defect_defect: float,
    ):
        self.payoffs = np.zeros(shape=(2, 2))
        self.payoffs[Move.COOPERATE.value, Move.COOPERATE.value] = payoff_cooperate_cooperate
        self.payoffs[Move.COOPERATE.value, Move.DEFECT.value] = payoff_cooperate_defect
        self.payoffs[Move.DEFECT.value, Move.COOPERATE.value] = payoff_defect_cooperate
        self.payoffs[Move.DEFECT.value, Move.DEFECT.value] = payoff_defect_defect

    def calculate_payoff(self, player_move: Move, adversary_move: Move) -> float:
        if player_move == adversary_move:
            if player_move == Move.COOPERATE:
                return float(self.payoffs[Move.COOPERATE.value, Move.COOPERATE.value])
            return float(self.payoffs[Move.DEFECT.value, Move.DEFECT.value])
        if player_move == Move.COOPERATE:
            return float(self.payoffs[Move.COOPERATE.value, Move.DEFECT.value])
        return float(self.payoffs[Move.DEFECT.value, Move.COOPERATE.value])
