# Authored by RAKOTOMALALA Hassim Mazahere, 02/12/2022 13h03

opponent_moves_decrypt = {
    "A": 1,
    "B": 2,
    "C": 3
}

my_moves_decrypt = {
    "X": 1,
    "Y": 2,
    "Z": 3
}


def RoundScore(mymove: str, opponentmove: str) -> int:
    """ Returns the score of the round given the plays of the player and the opponent.
    args :
        - mymove : str arg representing the player move
        - opponentmove : str arg reprensenting the opponent move

    Returns 6 on win, 3 on draw, 0 on loss.
    """
    score = 0

    win = {1, -2}

    if my_moves_decrypt[mymove] == opponent_moves_decrypt[opponentmove]:
        score = 3
    elif (my_moves_decrypt[mymove] - opponent_moves_decrypt[opponentmove]) in win:
        score = 6
    else:
        score = 0

    return score


def main(strategy_guide: str) -> int:
    """ Main method solving the puzzle.

    args:
     - stratagy_guide : string guide of victory

    Returns the total score if the strategy guide is completly correct
    """
    total_score = 0
    for round in strategy_guide.splitlines():
        opponentmove, my_move = round.split(" ")
        total_score += my_moves_decrypt[my_move]
        total_score += RoundScore(my_move, opponentmove)

    return total_score


if (__name__ == "__main__"):
    ret = None
    input = ""

    with open('input.txt') as f:
        input = f.read()
        assert input

    ret = main(input)
    print(ret)
