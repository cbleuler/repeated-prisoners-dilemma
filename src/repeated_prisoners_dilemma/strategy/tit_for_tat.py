from repeated_prisoners_dilemma.strategy.strategy import Strategy
from repeated_prisoners_dilemma.round import Round
from repeated_prisoners_dilemma.player import PlayerNumber
from repeated_prisoners_dilemma.move import Move


class TitForNTatStrategy(Strategy):
    def __init__(self, n_tats: int):
        self.n_tats = n_tats

    def calculate_next_move(self, rounds: list[Round], player_number: PlayerNumber):
        if len(rounds) < self.n_tats:
            return Move.COOPERATE

        for i in range(1, self.n_tats + 1):
            if rounds[-i].get_player_move(player_number.opponent) == Move.COOPERATE:
                return Move.COOPERATE
        return Move.DEFECT
