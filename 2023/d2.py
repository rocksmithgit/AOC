import sys
import numpy as np
from collections import defaultdict, Counter, deque
from pathlib import Path
from timeit import default_timer as timer


def get_data(inputData):
    infile = sys.argv[1] if len(sys.argv) > 1 else inputData
    parsed = []
    for line in open(infile, 'r'):
        if line.strip():
            stripped = line.strip()
            replaced = stripped.replace(":", "")
            replaced = replaced.replace(";", "")
            replaced = replaced.replace(",", "")
            DEBUG1 and print(f"{replaced}")
            splt = replaced.split()
            splt[0], splt[1] = splt[1], splt[0]
            cubeDict = {'red': 0, 'green': 0, 'blue': 0, 'Game': 0}
            for indx in range(len(splt)-1, 0, -2):
                cubeDict[splt[indx]] = max(int(splt[indx-1]),cubeDict[splt[indx]])
            parsed.append(cubeDict)
    return parsed


def part_one(inputData):
    if TESTING:
        maxCubes = {'red': 12, 'green': 13, 'blue': 14}
    if PART1:
        maxCubes = {'red': 12, 'green': 13, 'blue': 14}
    total = 0
    for line in inputData:
        DEBUG1 and print(f"LINE: {line}")
        DEBUG1 and print(f"RED: {line['red']}")
        DEBUG1 and print(f"BLUE: {line['blue']}")
        DEBUG1 and print(f"GREEN: {line['green']}")
        if int(line['red']) <= maxCubes['red'] and int(line['green']) <= maxCubes['green'] and int(line['blue']) <= maxCubes['blue']:
            total += int(line['Game'])
            DEBUG1 and print({total})
    return total


def part_two(inputData):
    power = 0
    for line in inputData:
        DEBUG2 and print(f"LINE: {line}")
        DEBUG2 and print(f"RED: {line['red']}")
        DEBUG2 and print(f"BLUE: {line['blue']}")
        DEBUG2 and print(f"GREEN: {line['green']}")
        power += int(line['red']) * int(line['green']) * int(line['blue'])
        DEBUG2 and print({power})
    return power


PART1 = True
DEBUG1 = False
PART2 = True
DEBUG2 = False
TESTING = False

if TESTING:
    inputData = f'{Path(__file__).stem}_test.in'
else:
    inputData = f'{Path(__file__).stem}.in'

print(f"ADVENT OF CODE: {Path(__file__).stem}")

start_parse = timer()
inputList = get_data(inputData)
end_parse = timer()

start_part1 = timer()
PART1 and print(f'\npart one: {part_one(inputList)}')
end_part1 = timer()
start_part2 = timer()
PART2 and print(f'part two: {part_two(inputList)}')
end_part2 = timer()

print(f"Elapsed Parse time: {(end_parse - start_parse)*1000:.3f}ms")
print(f"Elapsed Part1 time: {(end_part1 - start_part1)*1000:.3f}ms")
print(f"Elapsed Part2 time: {(end_part2 - start_part2)*1000:.3f}ms")
print(f"Elapsed computational time: {(end_part2 - start_part1)*1000:.3f}ms")
print(f"Elapsed Total time: {((end_part2 - start_part1)+(end_parse - start_parse))*1000:.3f}ms")
