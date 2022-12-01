import sys
import numpy as np
from collections import defaultdict, Counter, deque
from pathlib import Path


def get_data(inputdata):
    infile = sys.argv[1] if len(sys.argv) > 1 else inputdata
    sanitised_list = []
    for line in open(infile, 'r'):
        stripped = line.strip()
        sanitised_list.append(stripped)
    return sanitised_list


def part_one(inputlist):
    elves = {}
    elf_calories = []
    elf = 1
    for element in inputlist:
        if element != '':
            elf_calories.append(int(element))
        else:
            elves[elf] = elf_calories
            elf += 1
            elf_calories = []
    highest = 0
    fattest = 0
    for elf in elves:
        if sum(elves[elf]) > highest:
            highest = sum(elves[elf])
            fattest = elf
    return sum(elves[fattest])


def part_two(inputlist):
    elves = [0]
    for element in inputlist:
        if element != '':
            if elves[-1] == 'NEXT':
                elves[-1] = 0
            elves[-1] = elves[-1] + int(element)
        else:
            elves.append('NEXT')
    if elves[-1] == 'NEXT':
        pop.elves(-1)
    sorted_elves = sorted(elves, reverse=True)
    return sorted_elves[0] + sorted_elves[1] + sorted_elves[2]


inputData = 'd1.in'
L = get_data(inputData)
print(f"ADVENT OF CODE: {Path(__file__).stem}")
print(f'part one: {part_one(L)}')
print(f'part two: {part_two(L)}')
