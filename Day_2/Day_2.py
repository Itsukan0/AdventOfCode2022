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

# my Rock beats his Scissors : -2
# my Paper beats his Rock : 1
# my Scissors  his beats Paper : 1
# his Rock beats my Scissors : 2
# his Paper beats my Rock : -1
# his Scissors beats my Paper : -1
win = {1, -2}
loss = {-1, 2}


def RoundScore_Moves(mymove: str, opponentmove: str) -> int:
    """ Returns the score of the round given the plays of the player and the opponent.
    args :
        - mymove : str arg representing the player move
        - opponentmove : str arg reprensenting the opponent move

    Returns move_score + 6 on win, 3 on draw, 0 on loss.
    """
    score = my_moves_decrypt[mymove]

    if my_moves_decrypt[mymove] == opponent_moves_decrypt[opponentmove]:
        score += 3
    elif (my_moves_decrypt[mymove] - opponent_moves_decrypt[opponentmove]) in win:
        score += 6
    else:
        score += 0

    return score


def RoundScore_Outcome(round_outcome: str, opponentmove: str) -> int:
    """ Returns the score of the round given the opponent moves and the round outcome
        args :
         - round_outcome : str arg indicating if the player should win
         - opponentmove : str arg reprensenting the opponent move

         Returns move_score + 6 on win, 3 on draw, 0 on loss.
    """
    Round_score = 0

    if round_outcome == "Y":
        Round_score += 3
        Round_score += opponent_moves_decrypt[opponentmove]

    elif round_outcome == "Z":
        Round_score += 6
        if opponentmove == "C":
            Round_score += 1
        else:
            Round_score += opponent_moves_decrypt[opponentmove]+1

    else:
        if opponentmove == "A":
            Round_score += 3
        else:
            Round_score += opponent_moves_decrypt[opponentmove]-1
    return Round_score


def main(strategy_guide: str) -> int:
    """ Main method solving the puzzle.

    args:
     - stratagy_guide : string guide of victory

    Returns the total score if the strategy guide is completly correct
    """
    total_score_moves = 0
    total_score_outcome = 0
    for round in strategy_guide.splitlines():
        opponentmove, playerdata = round.split(" ")
        total_score_moves += RoundScore_Moves(playerdata, opponentmove)
        total_score_outcome += RoundScore_Outcome(playerdata, opponentmove)

    return [total_score_moves, total_score_outcome]


if (__name__ == "__main__"):
    ret = None
    input = ""
    with open('Day_2/input.txt') as f:
        input = f.read()
        assert input
    ret = main(input)
    assert (len(ret) == 2)
    print(ret[0]) # Part 1
    print(ret[1]) # Part 2
