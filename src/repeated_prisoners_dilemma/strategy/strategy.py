from __future__ import annotations
from abc import ABC, abstractmethod


class Strategy(ABC):
    @abstractmethod
    def calculate_next_move(self, rounds: list["Round"], player_number: "PlayerNumber"):
        pass
