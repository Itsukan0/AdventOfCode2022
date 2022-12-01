# Authored by RAKOTOMALALA Hassim Mazahere, 01/12/2022 19h12

def main(inventory: str):
    """ Main method solving the puzzle.
    This first iteration just gets the inventory string, single out per elf inventory,
    and count the amount of calories of every elf's item in a linear fashion

    args:
     - inventory : string input of the inventory

     returns the maximum amount of calories carried by a single elf
    """
    max_calories = 0
    inventory_per_elf = inventory.split("\n\n")

    if (inventory_per_elf):
        for inventory in inventory_per_elf:
            total_calories_per_elf = 0
            items = inventory.split("\n")
            for item in items:
                if (item):
                    total_calories_per_elf = total_calories_per_elf + int(item)

            if (total_calories_per_elf > max_calories):
                max_calories = total_calories_per_elf

    return max_calories


if (__name__ == "__main__"):
    ret = None
    input = ""
    try:
        with open('input.txt') as f:
            input = f.read()
        if (not input):
            print("Coudn't read input file")
        else:
            ret = main(input)
            if (ret):
                print(ret)
            else:
                print("Script probably crashed or result was empty (improbable)")
    except Exception as e:
        print(e)
