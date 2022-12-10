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


@timer_func
def part_one(inputlist):
    register = 1
    cycles = 1        # we are getting value DURING the cycle....
    special = 0
    repeats = {'noop': 1, 'addx': 2}
    for instruction in inputlist:
        DEBUG1 and print(f"\ninstruction: {instruction.strip()}")
        args = instruction.split()
        for tick in range(repeats[args[0]]):
            DEBUG1 and print(f"during cycle: {cycles:3d}, register: {register:4d}, product: {cycles * register:5d}, special: {special:5d}", end="")
            if args[0] == 'addx' and tick == repeats[args[0]] - 1:
                register += int(args[1])
            cycles += 1
#            DEBUG1 and print(f"cycles: {cycles:3d}, register: {register:4d}, product: {cycles * register:5d}, special: {special:5d}", end="")
            if cycles in (20, 60, 100, 140, 180, 220):
                special += cycles * register
                DEBUG1 and print(f" **")
            else:
                DEBUG1 and print("")
    print("")
    return special


@timer_func
def part_two(inputlist):
    """
    1.  We have the register values DURING a cycle from Part One
    2.  Move sprite and see if it sits within plus/minus 1 of register
    :param inputlist:
    :return:
    """
    register = 1
    cycles = 1  # we are getting value DURING the cycle....
    special = 0
    repeats = {'noop': 1, 'addx': 2}
    crt = ""
    for instruction in inputlist:
        DEBUG2 and print(f"\ninstruction: {instruction.strip()}")
        args = instruction.split()
        for tick in range(repeats[args[0]]):
            drawing = (cycles-1) % 40
            sprite = {register-1, register, register+1}
            DEBUG2 and print(f"During cycles: {cycles}, drawing: {drawing}, sprite range {sprite}, register: {register}")
            if drawing in sprite:
                crt += "#"
            else:
                crt += " "
            DEBUG2 and print(crt)
            if args[0] == 'addx' and tick == repeats[args[0]] - 1:
                register += int(args[1])
            cycles += 1
    print("")
    for x, char in enumerate(crt):
        if x % 40 == 0:
            print("")
        print(char, end="")
    print("")
    return


total_time = []
DEBUG0 = False
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
