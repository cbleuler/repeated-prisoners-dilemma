from repeated_prisoners_dilemma.player import PlayerNumber


def test_opponent():
    assert PlayerNumber.PLAYER_1.opponent == PlayerNumber.PLAYER_2
    assert PlayerNumber.PLAYER_2.opponent == PlayerNumber.PLAYER_1
