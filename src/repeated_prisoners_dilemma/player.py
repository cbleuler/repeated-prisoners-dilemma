from __future__ import annotations

from enum import Enum
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from repeated_prisoners_dilemma.strategy.strategy import Strategy
    from repeated_prisoners_dilemma.round import Round
    from repeated_prisoners_dilemma.move import Move


class PlayerNumber(Enum):
    PLAYER_1 = 1
    PLAYER_2 = 2

    @property
    def opponent(self):
        if self == PlayerNumber.PLAYER_1:
            return PlayerNumber.PLAYER_2
        return PlayerNumber.PLAYER_1


@dataclass
class Player:
    strategy: Strategy
    number: PlayerNumber

    def play_move(self, rounds: list["Round"]) -> "Move":
        next_move = self.strategy.calculate_next_move(rounds=rounds, player_number=self.number)
        return next_move
