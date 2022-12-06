# Authored by RAKOTOMALALA Hassim Mazahere, 05/12/2022 22h33
# TODO : Rework this, functionnal but ugly

import string
import re

alphabet = set(string.ascii_uppercase)


def getStackCrates(drawing: str, numberofstacks: int) -> list:
    Queues = []

    for stack in range(numberofstacks):
        Queues.append([])

    for line in drawing.splitlines():
        for index in range(len(line)):
            if line[index] in alphabet:
                Queues[(index-1)//4].append(line[index])
    return Queues


def processInstruction(instruction: str) -> tuple:
    list_numbers = re.findall(r'\d+', instruction)
    amount = int(list_numbers[0])
    source = int(list_numbers[1])
    destination = int(list_numbers[2])
    return (source-1, destination-1, amount)


def moveCrate(source: list, destination: list, Crate_amount: int) -> None:
    for x in range(Crate_amount):
        destination.insert(0, source.pop(0))
    return


def sectionDrawing(drawing: str) -> tuple:
    Crates = drawing.split("\n 1")[0]
    Instructions = drawing.split("\n\n")[1]
    NumberOfStacks = int(drawing.split(" \n\n")[0][-1])
    return (Crates, Instructions, NumberOfStacks)


def main(drawing: str) -> str:
    returnstring = ""
    Crates, Instructions, NoS = sectionDrawing(drawing)
    Queues_List = getStackCrates(Crates, NoS)
    for instruction in Instructions.split("\n"):
        source, destination, amount = processInstruction(instruction)
        moveCrate(Queues_List[source], Queues_List[destination], amount)

    for q in Queues_List:
        returnstring += q[0]
    return returnstring


if (__name__ == "__main__"):
    ret = None
    input = ""
    with open('input.txt') as f:
        input = f.read()
        assert input

    # Part 1
    print(main(input))
