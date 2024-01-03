import sys
import numpy as np
from collections import defaultdict, Counter, deque
from pathlib import Path
from timeit import default_timer as timer


def get_data(inputdata):
    infile = sys.argv[1] if len(sys.argv) > 1 else inputdata
    parsed = []
    for line in open(infile, 'r'):
        if line.strip():
            stripped = line.strip()
            parsed.append(stripped)
    return parsed


def part_one(inputData):
    total = 0
    for line in inputData:
        digits = []
        for char in line:
            if char.isdigit():
                digits.append(char)
        tens = int(digits[0])
        units = int(digits[-1])
        total += tens*10 + units
    return total


def part_two(inputData):
    total = 0
    numberList = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
                  '1', '2', '3', '4', '5', '6', '7', '8', '9']
    numberDict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9,
                  '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    ln = 0
    for line in inputData:
        highestIndex = 0
        lowestIndex = 999999
        lowest = ''
        highest = ''
        ln += 1
        for number in numberList:
            findResultL = line.find(number)
            findResultR = line.rfind(number)
            if findResultL < lowestIndex and findResultL != -1:
                lowest = number
                lowestIndex = findResultL
            if findResultR > highestIndex and findResultR != -1:
                highest = number
                highestIndex = findResultR
        if highest == '':
            highest = lowest
        DEBUG2 and print(f"{line.ljust(50)} {ln} tot: {total} lo: {lowest} => {numberDict[lowest]}; hi: {highest} => {numberDict[highest]} add: {numberDict[lowest]*10 + numberDict[highest]}")
        total += (numberDict[lowest]*10) + numberDict[highest]
    return total


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
