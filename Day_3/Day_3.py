# Authored by RAKOTOMALALA Hassim Mazahere, 04/12/2022 23h11

priorities_index = {}


def SetPriorities() -> None:
    for key in range(1, 27):
        priorities_index[chr(96+key)] = key

    for key in range(27, 53):
        priorities_index[chr(64 + (key - 26))] = key
    return


def main(ruck_sack_list: str) -> int:
    priority_sum = 0
    SetPriorities()

    duplicates = []
    for items in ruck_sack_list.splitlines():
        len_items = len(items)
        first_pocket = items[0:(len_items//2)]
        second_pocket = items[(len_items//2):len_items]

        check_pocket2 = set(first_pocket)

        for char in second_pocket:
            if char in check_pocket2:
                duplicates.append(char)
                break
            else:
                pass

    for letters in duplicates:
        priority_sum += priorities_index[letters]

    return priority_sum


if (__name__ == "__main__"):
    ret = None
    input = ""
    with open('Day_3/input.txt') as f:
        input = f.read()
        assert input
    ret = main(input)
    assert ret
    print(ret)
