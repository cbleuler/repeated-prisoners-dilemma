from __future__ import annotations
from dataclasses import dataclass

from repeated_prisoners_dilemma.move import Move
from repeated_prisoners_dilemma.player import PlayerNumber


@dataclass
class RoundResult:
    move_player_1: str
    move_player_2: str

    payoff_player_1: float
    payoff_player_2: float


@dataclass
class Round:
    move_player_1: Move
    move_player_2: Move

    def payoff_player(self, player_number: PlayerNumber, payoff: "Payoff") -> float:
        if player_number == PlayerNumber.PLAYER_1:
            return payoff.calculate_payoff(player_move=self.move_player_1, adversary_move=self.move_player_2)
        return payoff.calculate_payoff(player_move=self.move_player_2, adversary_move=self.move_player_1)

    def evaluate_round(self, payoff: "Payoff") -> RoundResult:
        return RoundResult(
            move_player_1=str(self.move_player_1),
            move_player_2=str(self.move_player_2),
            payoff_player_1=self.payoff_player(player_number=PlayerNumber.PLAYER_1, payoff=payoff),
            payoff_player_2=self.payoff_player(player_number=PlayerNumber.PLAYER_2, payoff=payoff),
        )

    def get_player_move(self, player_number: PlayerNumber):
        if player_number == PlayerNumber.PLAYER_1:
            return self.move_player_1
        return self.move_player_2
