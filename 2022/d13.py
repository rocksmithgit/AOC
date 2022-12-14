import sys
import numpy as np
from collections import defaultdict, Counter, deque
from pathlib import Path
from timeit import default_timer as timer
import re
import json
import itertools
from functools import cmp_to_key as cmp_to_key


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
    with open(infile) as f:
        lines = f.read().replace('\n\n', '\n').splitlines()
        packets = list(map(json.loads, lines))
        pairs = []
        for i in range(0, len(packets), 2):
            pairs.append(packets[i:i + 2])
    return pairs


def compare_func(left, right):
    # Check the types of the input
    l_is_int = type(left) is int
    r_is_int = type(right) is int
#    print(f"Comparing {l} to {r}")
    DEBUG and print(f"l is int: {l_is_int}, r is int:{r_is_int}")

    # If BOTH are integers.
    if l_is_int and r_is_int:
        return left - right

    # If one is an integer, make it a list and check again.
    if l_is_int != r_is_int:
        if l_is_int:
            return compare_func([left], right)
        else:
            return compare_func(left, [right])

    # Both are lists, check their items pairwise, stop at the first conclusive result.
    for x, y in zip(left, right):
        result = compare_func(x, y)
        if result != 0:
            return result

    # If we get here we ran out of items before coming to a conclusion. Now what matters is
    # which list was longer
    return len(left) - len(right)


@timer_func
def part_one(inputlist):

    count = 0
    for i, (left, right) in enumerate(inputlist, 1):
        if compare_func(left, right) < 0:
            count += i
    return count


@timer_func
def part_two(inputlist):
    # add the divider packets - brace the multiple elements!
    newlist = []
    for i, (left, right) in enumerate(inputlist, 1):
        newlist.append(left)
        newlist.append(right)
    print("************ PART 2*******************")
    newlist.extend(([[2]], [[6]]))
    # now need to generate a sort order key
#    print(inputlist)
    newlist.sort(key=cmp_to_key(compare_func))
    result = newlist.index([[2]]) + 1
    result *= newlist.index([[6]]) + 1
    return result


total_time = []
DEBUG = False
DEBUG1 = False
DEBUG2 = False
TESTING = False

if TESTING:
    inputData = f'{Path(__file__).stem}_test.in'
else:
    inputData = f'{Path(__file__).stem}.in'

print(f"ADVENT OF CODE: {Path(__file__).stem}")
L = get_data(inputData)
print(f"Part one: {part_one(L)}")
print(f"Part two: {part_two(L)}")
print(f"Elapsed Total time: {sum(total_time):.4f}s")
