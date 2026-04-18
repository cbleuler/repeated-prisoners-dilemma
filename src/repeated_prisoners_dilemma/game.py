from dataclasses import dataclass, field

import numpy as np

from repeated_prisoners_dilemma.errors import DomainError
from repeated_prisoners_dilemma.move import Move
from repeated_prisoners_dilemma.payoff import Payoff
from repeated_prisoners_dilemma.player import Player
from repeated_prisoners_dilemma.round import Round


@dataclass
class GameSummary:
    moves_player_1: list[Move]
    moves_player_2: list[Move]
    total_score_player_1: float
    total_score_player_2: float
    score_relative_to_mutual_cooperation_player_1: float
    score_relative_to_mutual_cooperation_player_2: float


@dataclass
class Game:
    min_number_of_rounds: int
    max_number_of_rounds: int
    payoff: Payoff
    players: tuple[Player, Player]
    rounds: list[Round] = field(default_factory=list)

    def __post_init__(self):
        if len(self.players) != 2:
            raise DomainError(f"Game requires exactly 2 players (got {len(self.players)}).")
        self.players = tuple(self.players)

        if self.min_number_of_rounds > self.max_number_of_rounds:
            raise DomainError(
                "min_number_of_rounds must be <= max_number_of_rounds "
                f"(got {self.min_number_of_rounds} > {self.max_number_of_rounds})."
            )
        if self.min_number_of_rounds < 1:
            raise DomainError(
                f"min_number_of_rounds must be >= 1 (got {self.min_number_of_rounds})."
            )

        self.number_of_rounds = int(
            np.random.randint(self.min_number_of_rounds, self.max_number_of_rounds + 1)
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

    def evaluate_game(self) -> GameSummary:
        results = [game_round.evaluate_round(payoff=self.payoff) for game_round in self.rounds]

        moves_player_1 = [result.move_player_1 for result in results]
        moves_player_2 = [result.move_player_2 for result in results]
        total_score_player_1 = sum(result.payoff_player_1 for result in results)
        total_score_player_2 = sum(result.payoff_player_2 for result in results)

        mutual_cooperation_total = (
            self.payoff.calculate_payoff(Move.COOPERATE, Move.COOPERATE) * self.number_of_rounds
        )

        return GameSummary(
            moves_player_1=moves_player_1,
            moves_player_2=moves_player_2,
            total_score_player_1=total_score_player_1,
            total_score_player_2=total_score_player_2,
            score_relative_to_mutual_cooperation_player_1=total_score_player_1 / mutual_cooperation_total,
            score_relative_to_mutual_cooperation_player_2=total_score_player_2 / mutual_cooperation_total,
        )
