from enum import Enum


class Move(Enum):
    COOPERATE = 0
    DEFECT = 1

    def __str__(self):
        if self == Move.COOPERATE:
            return "Cooperate"
        return "Defect"
