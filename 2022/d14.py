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
    parsed_data = []
    with open(infile) as f:
        all_corners = []
        for line in f:
            line = line.replace('->', ' ')
            DEBUG and print(f"line: {line}")
            corners = line.split()
            wall = []
            for corner in corners:
                tpl = tuple(map(int, corner.split(',')))
                wall.append(tpl)
            DEBUG and print(f"wall {wall}")
            for i in range(len(wall)-1):
                DEBUG and print(f"considered pair: {wall[i]}, {wall[i+1]}")
                if wall[i][1] == wall[i+1][1]:
                    DEBUG and print(f"wall2a: {wall}")
#                    print(f"i: {i}, range: {len(wall) - 1}")
                    DEBUG and print(f"{wall[i][0]}, {wall[i+1][0]}")
                    for j in range(min(wall[i][0], wall[i+1][0]), max(wall[i][0], wall[i+1][0])+1):
#                        print(f"j range_a {wall[i][0]}, {wall[i+1][0]+1}")
                        DEBUG and print(f"adding x: {(j, wall[i][1])}")
                        parsed_data.append((j, wall[i][1]))
                        DEBUG and print(f"parsed: {parsed_data}")
                elif wall[i][0] == wall[i+1][0]:
                    DEBUG and print(f"wall2b: {wall}")
#                    print(f"i: {i}, range: {len(wall) - 1}")
                    for j in range(min(wall[i][1], wall[i+1][1]), max(wall[i][1], wall[i+1][1])+1):
#                        print(f"j range_b {wall[i][1]}, {wall[i+1][1]+1}")
                        DEBUG and print(f"adding y: {(wall[i][0], j)}")
                        parsed_data.append((wall[i][0], j))
                        DEBUG and print(f"parsed: {parsed_data}")
                else:
                    pass

    DEBUG and print(f"all_corners: {all_corners}")
    DEBUG and print(f"parsed data: {parsed_data}")

    return parsed_data


def isRock(coords, rock):
    DEBUG and print(f"is_next_rock comparison: {rock}, {coords in rock}")
    return coords in rock


def isSand(coords, sand):
    DEBUG and print(f"is_next_sand comparison: {sand} {coords in sand}")
    return coords in sand

def isOccupied(coords, occupied):
    return coords in occupied


def move(coords, parameters, p2=False):
    """At each step sand moves:
                  - down until hits sand or rock,
                  - then goes down and left until hits sand/rock and if not possible
                  - then goes down/right

       P1 checks to see if sand ends up at the floor level; if so we have reached solution
       P2 check if sand is 1 above floor, locks it in place if is, and continues"""

    x, y = coords
    dn = (x, y + 1)
    dl = (x - 1, y + 1)
    dr = (x + 1, y + 1)
    yfloor, occupied = parameters

    if y == yfloor-1 and p2:
        return coords, parameters
    elif y == yfloor:
        return False, False
    elif dn not in occupied:
        DEBUG and print(f"1 current x,y: {x},{y}, next move is to {x}, {y+1}")
        return move(dn, parameters, p2)
    elif dl not in occupied:
        DEBUG and print(f"2 current x,y: {x},{y}, next move is to {x-1}, {y+1}")
        return move(dl, parameters, p2)
    elif dr not in occupied:
        DEBUG and print(f"3 current x,y: {x},{y}, next move is to {x+1}, {y+1}")
        return move(dr, parameters, p2)
    elif not coords in occupied:
        DEBUG and print(f"Sand settled at x, y {x}, {y}")
        return coords, parameters
    else:
        return False, False


@timer_func
def part_one(inputlist):
    yfloor = max([x[1] for x in inputlist])
    occupied = set(inputlist)
    parameters = [yfloor, occupied]
    count = 0

    while True:
        DEBUG1 and print(f"\nSand # {count + 1}")
        res, parameters = move((500, 0), parameters)
        DEBUG1 and print(f"res: {res}")
        if res:
            occupied.add(res)
            count += 1
        else:
            break
    return count


@timer_func
def part_two(inputlist):
    yfloor = max([x[1] for x in inputlist]) + 2
    occupied = set(inputlist)
    parameters = [yfloor, occupied]
    count = 0
    while True:
        DEBUG2 and print(f"\nSand # {count + 1}")
        res, parameters = move((500, 0), parameters, True)
        DEBUG2 and print(f"res2: {res}")
        if res:
            if res[1] == (500, 0):
                break
            occupied.add(res)
            count += 1
        else:
            break
    return count


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
