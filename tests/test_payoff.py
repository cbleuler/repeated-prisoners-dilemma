import pytest

from repeated_prisoners_dilemma.move import Move
from repeated_prisoners_dilemma.payoff import Payoff, PayoffWarning


def test_calculate_payoff_cooperate_cooperate(prisoners_dilemma_payoff):
    assert prisoners_dilemma_payoff.calculate_payoff(player_move=Move.COOPERATE, adversary_move=Move.COOPERATE) == 3


def test_calculate_payoff_cooperate_defect(prisoners_dilemma_payoff):
    assert prisoners_dilemma_payoff.calculate_payoff(player_move=Move.COOPERATE, adversary_move=Move.DEFECT) == 0


def test_calculate_payoff_defect_cooperate(prisoners_dilemma_payoff):
    assert prisoners_dilemma_payoff.calculate_payoff(player_move=Move.DEFECT, adversary_move=Move.COOPERATE) == 5


def test_calculate_payoff_defect_defect(prisoners_dilemma_payoff):
    assert prisoners_dilemma_payoff.calculate_payoff(player_move=Move.DEFECT, adversary_move=Move.DEFECT) == 1


def test_warns_non_prisoners_dilemma_ordering():
    with pytest.warns(PayoffWarning, match="T > R > P > S"):
        Payoff(
            payoff_cooperate_cooperate=5,
            payoff_cooperate_defect=0,
            payoff_defect_cooperate=3,
            payoff_defect_defect=1,
        )


def test_warns_exploitable_alternation():
    with pytest.warns(PayoffWarning, match="2R > T \\+ S"):
        Payoff(
            payoff_cooperate_cooperate=3,
            payoff_cooperate_defect=0,
            payoff_defect_cooperate=10,
            payoff_defect_defect=1,
        )
