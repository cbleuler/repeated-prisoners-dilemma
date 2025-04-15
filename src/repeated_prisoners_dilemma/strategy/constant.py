from __future__ import annotations

from repeated_prisoners_dilemma.round import Round
from repeated_prisoners_dilemma.move import Move
from repeated_prisoners_dilemma.strategy.strategy import Strategy


class ConstantCooperationStrategy(Strategy):
    def calculate_next_move(self, rounds: list[Round], player_number: "PlayerNumber") -> Move:
        return Move.COOPERATE


class ConstantDefectionStrategy(Strategy):
    def calculate_next_move(self, rounds: list[Round], player_number: "PlayerNumber") -> Move:
        return Move.DEFECT
