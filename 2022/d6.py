import sys
import numpy as np
from collections import defaultdict, Counter, deque
from pathlib import Path
from timeit import default_timer as timer
import re


def timer_func(func):
    # This function shows the execution time of the function object passed
    def wrap_func(*args, **kwargs):
        t1 = timer()
        result = func(*args, **kwargs)
        t2 = timer()
        print(f'Function {func.__name__!r} executed in {(t2 - t1):.4f}s')
        total_time.append((t2 - t1))
        return result
    return wrap_func


@timer_func
def get_data(inputdata):
    infile = sys.argv[1] if len(sys.argv) > 1 else inputdata
    parsed = []
    with open(infile, 'r') as f:
        for line in f:
            parsed.append(line)
    return parsed


def part_one(inputlist):
    """
    1. Traverse line with a 4char moving window
    2. See if all four char are different
    :param inputlist:
    :return:
    """
    DEBUG1 and print(f"inputlist: {inputlist}")
    for line in inputlist:
        for x in range(0, len(line) - 4):
            DEBUG1 and print(f"window: {line[x:x+4]}")
            if len(set(line[x:x+4])) == 4:
                return x + 4
    return print("No solution")


@timer_func
def part_two(inputlist):
    """
    1. Traverse line with a 14char moving window
    2. See if all fourteen char are different
    :param inputlist:
    :return:
    """
    DEBUG2 and print(f"inputlist: {inputlist}")
    for line in inputlist:
        for x in range(0, len(line) - 14):
            DEBUG2 and print(f"window: {line[x:x+14]}")
            if len(set(line[x:x+14])) == 14:
                return x + 14
    return print("No solution")


total_time = []
DEBUG1 = False
DEBUG2 = False
TESTING = True

if TESTING:
    inputData = f'{Path(__file__).stem}_test.in'
else:
    inputData = f'{Path(__file__).stem}.in'

print(f"ADVENT OF CODE: {Path(__file__).stem}")
L = get_data(inputData)
print(f"Part one: {part_one(L)}")
print(f"Part two: {part_two(L)}")
print(f"Elapsed Total time: {sum(total_time):.4f}s")
