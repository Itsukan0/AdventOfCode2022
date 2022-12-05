# Authored by RAKOTOMALALA Hassim Mazahere, 05/12/2022 01h18

def main(assignement: str) -> int:
    pairs_contained = 0

    for pairs in assignement.splitlines():
        only_once = True
        p1, p2 = pairs.split(",")
        p1_b, p1_e = p1.split("-")
        p2_b, p2_e = p2.split("-")

        if int(p1_b) >= int(p2_b) and int(p1_e) <= int(p2_e):
            pairs_contained += 1
            only_once = False
        if int(p2_b) >= int(p1_b) and int(p2_e) <= int(p1_e) and only_once:
            pairs_contained += 1

    return pairs_contained


if (__name__ == "__main__"):
    ret = None
    input = ""
    with open('input.txt') as f:
        input = f.read()
        assert input
    ret = main(input)
    assert ret
    print(ret)
