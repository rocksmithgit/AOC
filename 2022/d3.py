import sys
import numpy as np
from collections import defaultdict, Counter, deque
from pathlib import Path


def get_data(inputdata):
    infile = sys.argv[1] if len(sys.argv) > 1 else inputdata
    parsed = []
    for line in open(infile, 'r'):
        if line.strip():
            stripped = line.strip()
            parsed.append(stripped)
    return parsed


def part_one(inputlist):
    """
    1. Having parsed input, split into two
    2. Compare left to right to see if any member of left appear in right
    3. For item appearing in both look up priority and dd to total
    """
    priority = {key: value+1 for value, key in enumerate('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')}
    DEBUG1 and print(f"priorty: {priority}")
    total = 0
    for element in inputlist:
        halfNumItems = int(len(element)/2)
        compartment1 = element[:halfNumItems]
        compartment2 = element[halfNumItems:]
        if len(compartment1) != len(compartment2):
            sys.exit("Lengths wrong")
        for item in compartment1:
            if item in compartment2:
                DEBUG1 and print(f"Shared item: {item}, priority: {priority[item]}")
                total += priority[item]
                break
    return total


def part_two(inputlist):
    """
    1. Get input into batches of 3 Sacks
    2. For each item in Sack 1, see if appears in Sack 2 AND Sack 3
    3. If it does assign priority and add to total
    """
    priority = {key: value + 1 for value, key in enumerate('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')}
    total = 0
    for x in range(int(len(inputlist) / 3)):
        shortlist = inputlist[0+x*3:3+x*3]
        DEBUG2 and print(f"shortlist: {shortlist}")
        for item in shortlist[0]:
            DEBUG2 and print(f"item: {item}")
            if item in shortlist[1] and item in shortlist[2]:
                DEBUG2 and print(f"shared item: {item}, priority: {priority[item]}")
                total += priority[item]
                break
    return total


DEBUG1 = False
DEBUG2 = False
inputData = 'd3.in'
L = get_data(inputData)
print(f"ADVENT OF CODE: {Path(__file__).stem}")
print(f'part one: {part_one(L)}')
print(f'part two: {part_two(L)}')
