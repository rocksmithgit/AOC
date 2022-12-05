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
    print(f"infile: {infile}")
    parsed = []
    with open(infile, 'r') as f:
        holding = []
        for line in f:
            stripped = line.strip('\n')
            if stripped:
                holding.append(stripped)
            else:
                parsed.append(holding)
                holding = []
        parsed.append(holding)
    return parsed


def part_one(inputlist):
    """
    1. Reverse the input so you can see how many piles there are
    2. For each row in the crates input, create a new list that takes every 4th char from first ie crate positions
    3. Look at each new crate list and if it is not a ' ' assign the crate
    4. Move the crates remembering that a slice is reversed
    :param inputlist:
    :return:
    """
    stacks = inputlist[0][::-1]
    DEBUG1 and print(f"original stack: {stacks}")
    crates = []
    max = int(stacks[0][-1])
    for row in stacks:
        crates.append(row[1::4])
        DEBUG1 and print(f"crates: {crates}")
    new_stack = [str(x) for x in range(1, max+1)]
    for row in crates:
        DEBUG1 and print(f"row: {row}")
        for i, pile in enumerate(row):
            if pile != ' ':
                new_stack[i] = new_stack[i]+pile
    DEBUG1 and print(f"new_stack: {new_stack}")
    instructions = inputlist[1][::]
    DEBUG1 and print(f"stacks: {stacks}, instructions: {instructions}")
    DEBUG1 and print(f"new_stack: {new_stack}")
    for instruction in instructions:
        thing = re.findall(r'\d+', instruction)
        DEBUG1 and print(f"digit: {thing}")
        number_to_move, from_stack, to_stack = map(int, re.findall(r'\d+', instruction))
        DEBUG1 and print(f"\n#: {number_to_move}, from: {from_stack}, to: {to_stack}, stacks: {new_stack}")
        to_move = new_stack[from_stack-1][-number_to_move:][::-1]
        new_stack[to_stack-1] = new_stack[to_stack-1] + to_move
        new_stack[from_stack-1] = new_stack[from_stack-1][:-number_to_move]
        DEBUG1 and print(f"BECOMES => stacks: {new_stack}, moving: {to_move}, to stack: {new_stack[to_stack-1]}")
    DEBUG1 and print(f"final_stack: {new_stack}")
    final = ''.join([x[-1] for x in new_stack])
    return final


@timer_func
def part_two(inputlist):
    """
    1. Reverse the input so you can see how many piles there are
    2. For each row in the crates input, create a new list that takes every 4th char from first ie crate positions
    3. Look at each new crate list and if it is not a ' ' assign the crate
    4. Move the crates remembering that a slice is NOT reversed
    :param inputlist:
    :return:
    """
    stacks = inputlist[0][::-1]
    DEBUG2 and print(f"original stack: {stacks}")
    crates = []
    max = int(stacks[0][-1])
    for row in stacks:
        crates.append(row[1::4])
        DEBUG2 and print(f"crates: {crates}")
    new_stack = [str(x) for x in range(1, max + 1)]
    for row in crates:
        DEBUG2 and print(f"row: {row}")
        for i, pile in enumerate(row):
            if pile != ' ':
                new_stack[i] = new_stack[i] + pile
    DEBUG2 and print(f"new_stack: {new_stack}")
    instructions = inputlist[1][::]
    DEBUG2 and print(f"stacks: {stacks}, instructions: {instructions}")
    DEBUG2 and print(f"new_stack: {new_stack}")
    for instruction in instructions:
        thing = re.findall(r'\d+', instruction)
        DEBUG2 and print(f"digit: {thing}")
        number_to_move, from_stack, to_stack = map(int, re.findall(r'\d+', instruction))
        DEBUG2 and print(f"\n#: {number_to_move}, from: {from_stack}, to: {to_stack}, stacks: {new_stack}")
        to_move = new_stack[from_stack - 1][-number_to_move:]
        new_stack[to_stack - 1] = new_stack[to_stack - 1] + to_move
        new_stack[from_stack - 1] = new_stack[from_stack - 1][:-number_to_move]
        DEBUG2 and print(f"BECOMES => stacks: {new_stack}, moving: {to_move}, to stack: {new_stack[to_stack - 1]}")
    DEBUG2 and print(f"final_stack: {new_stack}")
    final = ''.join([x[-1] for x in new_stack])
    return final


total_time = []
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
