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


def part_one_a(inputlist):
    """
    1. Having parsed input, split into two
    2. Compare left to right to see if any member of left appear in right
    3. For item appearing in both look up priority and dd to total
    """
    priority = {key: value+1 for value, key in enumerate('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')}
    DEBUG1a and print(f"priorty: {priority}")
    total = 0
    for element in inputlist:
        halfNumItems = int(len(element)/2)
        set1 = set(element[:halfNumItems])
        set2 = set(element[halfNumItems:])
        DEBUG1a and print(f"Set1: {set1}, Set2: {set2}")
        shared = (set1 & set2).pop()
        DEBUG1a and print(f"shared: {shared}")
        total += priority[shared]
    return total


def part_two_a(inputlist):
    """
    1. Get input into batches of 3 Sacks
    2. For each item in Sack 1, see if appears in Sack 2 AND Sack 3
    3. If it does assign priority and add to total
    """
    priority = {key: value + 1 for value, key in enumerate('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')}
    total = 0
    for x in range(int(len(inputlist) / 3)):
        shortlist = inputlist[0+x*3:3+x*3]
        DEBUG2a and print(f"shortlist: {shortlist}")
        set1 = set(shortlist[0])
        set2 = set(shortlist[1])
        set3 = set(shortlist[2])
        shared = (set1 & set2 & set3).pop()
        DEBUG2a and print(f"Shared: {shared}")
        total += priority[shared]
    return total


DEBUG1 = False
DEBUG2 = False
DEBUG1a = False
DEBUG2a = False
TESTING = False

if TESTING:
    inputData = f'{Path(__file__).stem}_test.in'
else:
    inputData = f'{Path(__file__).stem}.in'

print(f"ADVENT OF CODE: {Path(__file__).stem}")

start_parse = timer()
L = get_data(inputData)
end_parse = timer()

start_part1 = timer()
print(f'\npart one: {part_one(L)}')
end_part1 = timer()
start_part2 = timer()
print(f'part two: {part_two(L)}')
end_part2 = timer()

print(f"Elapsed Parse time: {(end_parse - start_parse)*1000:.3f}ms")
print(f"Elapsed Part1 time: {(end_part1 - start_part1)*1000:.3f}ms")
print(f"Elapsed Part2 time: {(end_part2 - start_part2)*1000:.3f}ms")
print(f"Elapsed computational time: {(end_part2 - start_part1)*1000:.3f}ms")
print(f"Elapsed Total time: {((end_part2 - start_part1)+(end_parse - start_parse))*1000:.3f}ms")

start_part1a = timer()
print(f'\npart one a: {part_one_a(L)}')
end_part1a = timer()
start_part2a = timer()
print(f'part two a: {part_two_a(L)}')
end_part2a = timer()

print(f"Elapsed Parse time: {(end_parse - start_parse)*1000:.3f}ms")
print(f"Elapsed Part1a time: {(end_part1a - start_part1a)*1000:.3f}ms")
print(f"Elapsed Part2a time: {(end_part2a - start_part2a)*1000:.3f}ms")
print(f"Elapsed computational time: {(end_part2a - start_part1a)*1000:.3f}ms")
print(f"Elapsed Total time: {((end_part2a - start_part1a)+(end_parse - start_parse))*1000:.3f}ms")
