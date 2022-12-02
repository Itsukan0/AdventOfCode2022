# Authored by RAKOTOMALALA Hassim Mazahere, 01/12/2022 19h12

def main(inventory: str) -> list:
    """ Main method solving the puzzle.
    This first iteration just gets the inventory string, single out per elf inventory,
    and count the amount of calories of every elf's item in a linear fashion

    args:
     - inventory : string input of the inventory

     returns the list in descending order to the calories carried by each elf
     (eg: the most loaded elf carries the calories amount in index 0 of the list)
    """
    calories_inventory = []

    for inv in inventory.split("\n\n"):
        total_calories_per_elf = 0

        for item in inv.splitlines():
            total_calories_per_elf += int(item)

        calories_inventory.append(total_calories_per_elf)

    calories_inventory.sort(reverse=True)
    return calories_inventory


if (__name__ == "__main__"):
    ret = None
    input = ""

    with open('input.txt') as f:
        input = f.read()
        assert input

    ret = main(input)
    assert (len(ret) >= 3)
    print((ret[0]))  # Part 1
    print(sum(ret[0:3]))  # Part 2
