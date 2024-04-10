from __future__ import annotations

from round import Round
from move import Move
from strategy.strategy import Strategy


class ConstantCooperationStrategy(Strategy):
    def calculate_next_move(self, rounds: list[Round], player_number: 'PlayerNumber') -> Move:
        return Move.COOPERATE


class ConstantDefectionStrategy(Strategy):
    def calculate_next_move(self, rounds: list[Round], player_number: 'PlayerNumber') -> Move:
        return Move.DEFECT
