from abc import ABC, abstractmethod


class Strategy(ABC):
    @abstractmethod
    def calculate_next_move(self, rounds):
        pass
