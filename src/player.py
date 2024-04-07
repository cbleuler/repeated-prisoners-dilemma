from __future__ import annotations

from enum import Enum
from dataclasses import dataclass

from strategy.strategy import Strategy


class PlayerNumber(Enum):
    PLAYER_1 = 1
    PLAYER_2 = 2


@dataclass
class Player:
    strategy: Strategy
    number: PlayerNumber

    def play_move(self, rounds: list['Round']) -> 'Move':
        next_move = self.strategy.calculate_next_move(rounds=rounds)
        return next_move
