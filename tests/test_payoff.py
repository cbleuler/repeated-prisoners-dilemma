import pytest

from payoff import Payoff
from move import Move
from tests.fixtures import *


def test_calculate_payoff_cooperate_cooperate(prisoners_dilemma_payoff):
    assert prisoners_dilemma_payoff.calculate_payoff(player_move=Move.COOPERATE, adversary_move=Move.COOPERATE) == 3


def test_calculate_payoff_cooperate_defect(prisoners_dilemma_payoff):
    assert prisoners_dilemma_payoff.calculate_payoff(player_move=Move.COOPERATE, adversary_move=Move.DEFECT) == 0


def test_calculate_payoff_defect_cooperate(prisoners_dilemma_payoff):
    assert prisoners_dilemma_payoff.calculate_payoff(player_move=Move.DEFECT, adversary_move=Move.COOPERATE) == 5


def test_calculate_payoff_defect_defect(prisoners_dilemma_payoff):
    assert prisoners_dilemma_payoff.calculate_payoff(player_move=Move.DEFECT, adversary_move=Move.DEFECT) == 1
