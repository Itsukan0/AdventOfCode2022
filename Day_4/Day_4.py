# Authored by RAKOTOMALALA Hassim Mazahere, 05/12/2022 01h18

def check_overlap(assignement: str) -> int:
    pairs_overlap = 0

    for pairs in assignement.splitlines():
        p1, p2 = pairs.split(",")
        p1_b, p1_e = p1.split("-")
        p2_b, p2_e = p2.split("-")

        p1_b, p2_b = int(p1_b), int(p2_b)
        p1_e, p2_e = int(p1_e), int(p2_e)

        if p1_b <= p2_b <= p1_e:
            pairs_overlap += 1
        elif p1_b <= p2_e <= p1_e:
            pairs_overlap += 1
        elif p2_b <= p1_b <= p2_e:
            pairs_overlap += 1
        elif p2_b <= p1_e <= p2_e:
            pairs_overlap += 1
        else:
            pass

    return pairs_overlap


def check_contained(assignement: str) -> int:
    pairs_contained = 0

    for pairs in assignement.splitlines():
        p1, p2 = pairs.split(",")
        p1_b, p1_e = p1.split("-")
        p2_b, p2_e = p2.split("-")

        p1_b, p2_b = int(p1_b), int(p2_b)
        p1_e, p2_e = int(p1_e), int(p2_e)

        if p1_b >= p2_b and p1_e <= p2_e:
            pairs_contained += 1
        elif p2_b >= p1_b and p2_e <= p1_e:
            pairs_contained += 1

    return pairs_contained


if (__name__ == "__main__"):
    ret = None
    input = ""
    with open('input.txt') as f:
        input = f.read()
        assert input
    # Part 1
    ret = check_contained(input)
    assert ret
    print(ret)

    # Part 2
    ret = check_overlap(input)
    assert ret
    print(ret)
