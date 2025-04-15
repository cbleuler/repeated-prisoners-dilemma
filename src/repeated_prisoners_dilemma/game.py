from dataclasses import dataclass, field

import numpy as np

from repeated_prisoners_dilemma.payoff import Payoff
from repeated_prisoners_dilemma.player import Player
from repeated_prisoners_dilemma.round import Round
from repeated_prisoners_dilemma.move import Move


@dataclass
class Game:
    min_number_of_rounds: int
    max_number_of_rounds: int
    payoff: Payoff
    players: tuple[Player, Player]
    rounds: list[Round] = field(default_factory=list)

    def __post_init__(self):
        self.number_of_rounds = int(
            np.round(np.random.uniform(low=self.min_number_of_rounds, high=self.max_number_of_rounds))
        )

    def play_round(self) -> Round:
        move_player_1 = self.players[0].play_move(self.rounds)
        move_player_2 = self.players[1].play_move(self.rounds)
        game_round = Round(move_player_1=move_player_1, move_player_2=move_player_2)
        self.rounds.append(game_round)
        return game_round

    def run_game(self):
        for _ in range(self.number_of_rounds):
            self.play_round()

    def evaluate_game(self) -> dict:
        results = []
        for game_round in self.rounds:
            results.append(game_round.evaluate_round(payoff=self.payoff))
        summary = {"moves_player_1": [], "moves_player_2": [], "total_score_player_1": 0, "total_score_player_2": 0}

        for result in results:
            summary["moves_player_1"].append(result.move_player_1)
            summary["moves_player_2"].append(result.move_player_2)
            summary["total_score_player_1"] += result.payoff_player_1
            summary["total_score_player_2"] += result.payoff_player_2

        max_payoff = self.payoff.calculate_payoff(Move.COOPERATE, Move.COOPERATE) * self.number_of_rounds

        summary["relative_achieved_points_player_1"] = summary["total_score_player_1"] / max_payoff
        summary["relative_achieved_points_player_2"] = summary["total_score_player_2"] / max_payoff

        return summary
