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
    inventory_per_elf = inventory.split("\n\n")

    if (inventory_per_elf):
        for inventory in inventory_per_elf:
            total_calories_per_elf = 0
            items = inventory.split("\n")
            for item in items:
                if (item):
                    total_calories_per_elf = total_calories_per_elf + int(item)
                calories_inventory.append(total_calories_per_elf)

    calories_inventory.sort(reverse=True)
    return calories_inventory


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
                print("Sum of calories of the 3 most loaded elves")
                if (len(ret) >= 3):
                    print(ret[0]+ret[1]+ret[2])
                else:
                    print("There isn't 3 elves in this list")
            else:
                print("Script probably crashed or result was empty (improbable)")
    except Exception as e:
        print(e)
