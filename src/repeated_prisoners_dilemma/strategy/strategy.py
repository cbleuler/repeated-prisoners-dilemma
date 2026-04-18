from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from repeated_prisoners_dilemma.move import Move

if TYPE_CHECKING:
    from repeated_prisoners_dilemma.player import PlayerNumber
    from repeated_prisoners_dilemma.round import Round


class Strategy(ABC):
    @abstractmethod
    def calculate_next_move(self, rounds: list[Round], player_number: PlayerNumber) -> Move:
        pass
