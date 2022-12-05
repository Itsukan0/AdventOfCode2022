# Authored by RAKOTOMALALA Hassim Mazahere, 04/12/2022 23h11

priorities_index = {}


def SetPriorities() -> None:
    for key in range(1, 27):
        priorities_index[chr(96+key)] = key

    for key in range(27, 53):
        priorities_index[chr(64 + (key - 26))] = key
    return


def FindDuplicateItems(ruck_sack_list: str) -> int:
    priority_sum = 0
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


def FindBadges(ruck_sack_list: str) -> int:
    priority_sum = 0
    line_counter = 0
    lines_per_group = 3

    badges = []
    first_elf_items = set()
    second_elf_items = set()
    group_sets = [first_elf_items, second_elf_items]

    for items in ruck_sack_list.splitlines():
        if (line_counter % lines_per_group) == 0:
            line_counter = 0
            for sets in group_sets:
                sets.clear()

            group_sets[0] = set(items)

        elif (line_counter % lines_per_group) == 1:
            group_sets[1] = set(items)

        elif (line_counter % lines_per_group) == 2:
            for char in items:
                if char in group_sets[0] and char in group_sets[1]:
                    badges.append(char)
                    break
                else:
                    pass
        line_counter += 1

    for letters in badges:
        priority_sum += priorities_index[letters]

    return priority_sum


if (__name__ == "__main__"):
    ret = None
    input = ""
    with open('input.txt') as f:
        input = f.read()
        assert input

    SetPriorities()

    # Part 1
    ret = FindDuplicateItems(input)
    assert ret
    print(ret)

    # Part 2
    ret = FindBadges(input)
    assert ret
    print(ret)
