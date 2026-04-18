# Repeated Prisoner's Dilemma

[![Python](https://img.shields.io/badge/python-%3E%3D3.11-blue)](https://www.python.org/)
[![Tests](https://github.com/cbleuler/repeated-prisoners-dilemma/actions/workflows/test.yml/badge.svg)](https://github.com/cbleuler/repeated-prisoners-dilemma/actions/workflows/test.yml)

A Python library for simulating the [Repeated Prisoner's Dilemma](https://www.youtube.com/watch?v=mScpHTIi-kM) game with configurable strategies and payoff matrices.

## Installation

Requires Python ≥ 3.11.

```bash
pip install repeated-prisoners-dilemma
```

Or install from source using [uv](https://docs.astral.sh/uv/):

```bash
uv sync
```

## Quick Start

```python
from repeated_prisoners_dilemma.game import Game
from repeated_prisoners_dilemma.payoff import Payoff
from repeated_prisoners_dilemma.player import Player, PlayerNumber
from repeated_prisoners_dilemma.strategy.tit_for_tat import TitForNTatStrategy
from repeated_prisoners_dilemma.strategy.constant import ConstantDefectionStrategy

payoff = Payoff(
    payoff_cooperate_cooperate=3.0,
    payoff_cooperate_defect=0.0,
    payoff_defect_cooperate=5.0,
    payoff_defect_defect=1.0,
)

player_1 = Player(strategy=TitForNTatStrategy(n_tats=1), number=PlayerNumber.PLAYER_1)
player_2 = Player(strategy=ConstantDefectionStrategy(), number=PlayerNumber.PLAYER_2)

game = Game(
    min_number_of_rounds=10,
    max_number_of_rounds=20,
    payoff=payoff,
    players=(player_1, player_2),
)

game.run_game()
summary = game.evaluate_game()

print(f"Player 1 score: {summary.total_score_player_1}")
print(f"Player 2 score: {summary.total_score_player_2}")
```

## Core Concepts

### Payoff Matrix

The `Payoff` class defines the four outcomes of each round using standard Prisoner's Dilemma notation:

| | Opponent Cooperates | Opponent Defects |
|---|---|---|
| **You Cooperate** | R (Reward) | S (Sucker) |
| **You Defect** | T (Temptation) | P (Punishment) |

A valid Prisoner's Dilemma requires **T > R > P > S** and **2R > T + S**. A `PayoffWarning` is issued if these conditions are not met.

### Strategies

| Class | Description |
|---|---|
| `ConstantCooperationStrategy` | Always cooperates |
| `ConstantDefectionStrategy` | Always defects |
| `TitForNTatStrategy(n_tats)` | Cooperates unless the opponent defected in each of the last `n_tats` rounds |
| `UniformRandomStrategy(probability_defection)` | Defects with a given probability each round |

#### Custom Strategy

Implement the `Strategy` abstract base class:

```python
from repeated_prisoners_dilemma.strategy.strategy import Strategy
from repeated_prisoners_dilemma.move import Move
from repeated_prisoners_dilemma.player import PlayerNumber
from repeated_prisoners_dilemma.round import Round

class MyStrategy(Strategy):
    def calculate_next_move(self, rounds: list[Round], player_number: PlayerNumber) -> Move:
        # rounds contains the full history of played rounds
        return Move.COOPERATE
```

### Game

`Game` runs a match between two players for a random number of rounds in `[min_number_of_rounds, max_number_of_rounds]`.

```python
game = Game(
    min_number_of_rounds=10,
    max_number_of_rounds=20,
    payoff=payoff,
    players=(player_1, player_2),
)
game.run_game()
summary = game.evaluate_game()
```

`evaluate_game()` returns a `GameSummary` with:

- `moves_player_1` / `moves_player_2` — list of `Move` values played each round
- `total_score_player_1` / `total_score_player_2` — cumulative payoffs
- `score_relative_to_mutual_cooperation_player_1` / `_player_2` — score as a fraction of what both players would have earned under mutual cooperation

## Development

```bash
# Install dev dependencies
uv sync --group dev

# Run tests
uv run pytest

# Run tests with coverage
uv run pytest --cov

# Lint
uv run pylint src/

# Type check
uv run mypy src/

# Format
uv run black src/ tests/
```

## License

LGPL-2.1 — see [LICENSE](LICENSE).