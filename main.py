from repeated_prisoners_dilemma.strategy import TitForNTatStrategy
from repeated_prisoners_dilemma.strategy import UniformRandomStrategy
from repeated_prisoners_dilemma.player import Player, PlayerNumber
from repeated_prisoners_dilemma.game import Game
from repeated_prisoners_dilemma.payoff import Payoff


def main():
    player_1 = Player(strategy=TitForNTatStrategy(n_tats=1), number=PlayerNumber.PLAYER_1)

    player_2 = Player(strategy=UniformRandomStrategy(0.9), number=PlayerNumber.PLAYER_2)

    payoff = Payoff(
        payoff_cooperate_cooperate=3, payoff_defect_defect=1, payoff_cooperate_defect=0, payoff_defect_cooperate=5
    )

    game = Game(min_number_of_rounds=20, max_number_of_rounds=20, payoff=payoff, players=[player_1, player_2])

    game.run_game()

    summary = game.evaluate_game()
    print(summary)


if __name__ == "__main__":
    main()
