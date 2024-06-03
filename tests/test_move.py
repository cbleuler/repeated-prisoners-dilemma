from move import Move


def test_string_conversion():
    assert str(Move.COOPERATE) == "Cooperate"
    assert str(Move.DEFECT) == "Defect"
