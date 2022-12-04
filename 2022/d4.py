import sys
import numpy as np
from collections import defaultdict, Counter, deque
from pathlib import Path
from timeit import default_timer as timer


def timer_func(func):
    # This function shows the execution time of
    # the function object passed
    def wrap_func(*args, **kwargs):
        t1 = timer()
        result = func(*args, **kwargs)
        t2 = timer()
        print(f'Function {func.__name__!r} executed in {(t2 - t1):.4f}s')
        return result

    return wrap_func


@timer_func
def get_data(inputdata):
    infile = sys.argv[1] if len(sys.argv) > 1 else inputdata
    parsed = []
    for line in open(infile, 'r'):
        if line.strip():
            stripped = line.strip()
            parsed.append(stripped)
    return parsed


@timer_func
def part_one(inputlist):
    """
    1. Having parsed input, split into two
    2. Split left/right side to get IDs of range
    3. Compare left sode to right to see if one is a full subset of the other
    """
    total = 0
    for line in inputlist:
        left, right = line.split(',')
        DEBUG1 and print(f"left: {left}, right: {right}")
        elf1 = left.split('-')
        elf2 = right.split('-')
        DEBUG1 and print(f"elf1: {elf1}, elf2: {elf2}")
        range1 = [x for x in range(int(elf1[0]), int(elf1[1])+1)]
        range2 = [x for x in range(int(elf2[0]), int(elf2[1])+1)]
        common = (set(range1) & set(range2))
        DEBUG1 and print(f"common: {common}, range1: {set(range1)}, range2: {set(range2)}")
        DEBUG1 and print(f"check1: {common == set(range1)}, check2: {common == set(range2)}")
        if common == set(range1) or common == set(range2):
            DEBUG1 and print("ENTERD")
            total += 1
    return total


@timer_func
def part_two(inputlist):
    """
    1. Having parsed input, split into two
    2. Split left/right side to get IDs of range
    3. Compare left side to right to see if any overlap - even simpler!
    """
    total = 0
    for line in inputlist:
        left, right = line.split(',')
        DEBUG2 and print(f"left: {left}, right: {right}")
        elf1 = left.split('-')
        elf2 = right.split('-')
        DEBUG2 and print(f"elf1: {elf1}, elf2: {elf2}")
        range1 = [x for x in range(int(elf1[0]), int(elf1[1])+1)]
        range2 = [x for x in range(int(elf2[0]), int(elf2[1])+1)]
        common = (set(range1) & set(range2))
        DEBUG2 and print(f"common: {common}, range1: {set(range1)}, range2: {set(range2)}")
        if common:
            DEBUG2 and print("ENTERD")
            total += 1
    return total


DEBUG1 = False
DEBUG2 = False
TESTING = False

if TESTING:
    inputData = f'{Path(__file__).stem}_test.in'
else:
    inputData = f'{Path(__file__).stem}.in'

print(f"ADVENT OF CODE: {Path(__file__).stem}")

#start_parse = timer()
L = get_data(inputData)
#end_parse = timer()

#start_part1 = timer()
print(f"Part one: {part_one(L)}")
#end_part1 = timer()
#start_part2 = timer()
print(f"Part two: {part_two(L)}")
#end_part2 = timer()

#print(f"Elapsed Parse time: {(end_parse - start_parse)*1000:.3f}ms")
#print(f"Elapsed Part1 time: {(end_part1 - start_part1)*1000:.3f}ms")
#print(f"Elapsed Part2 time: {(end_part2 - start_part2)*1000:.3f}ms")
#print(f"Elapsed computational time: {(end_part2 - start_part1)*1000:.3f}ms")
#print(f"Elapsed Total time: {((end_part2 - start_part1)+(end_parse - start_parse))*1000:.3f}ms")
