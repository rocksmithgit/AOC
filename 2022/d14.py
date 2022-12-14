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


def move(coords, parameters):
    """At each step sand moves:
                  - down until hits sand or rock, and if not possible
                  - then goes down and left until hits sand/rock and if not possible
                  - then goes down/right"""
    x, y = coords[0], coords[1]
#    xrange = parameters[0]
    yfloor = parameters[0]
#    print(f"yflloe: {yfloor}")
    rock = parameters[1]
    sand = parameters[2]
    if not isRock((x, y+1), rock) and not isSand((x, y+1), sand) and not y+1 > yfloor:
        DEBUG and print(f"current x,y: {x},{y}, next move is to {x}, {y+1}")
        return move((x, y+1), parameters)
    elif not isRock((x-1, y+1), rock) and not isSand((x-1, y+1), sand):
#        if not x-1 < min(xrange):
        if not y+1 > yfloor:
            DEBUG and print(f"current x,y: {x},{y}, next move is to {x-1}, {y+1}")
            return move((x-1, y+1), parameters)
        else:
            DEBUG and print(f"Sand will move to infinity")
            return False, False
    elif not isRock((x+1, y+1), rock) and not isSand((x+1, y+1), sand):
#        if not x+1 > max(xrange):
        if not y+1 > yfloor:
            DEBUG and print(f"current x,y: {x},{y}, next move is to {x+1}, {y+1}")
            return move((x+1, y+1), parameters)
        else:
            DEBUG and print(f"Sand will move to infinity")
            return False, False
    else:
        DEBUG and print(f"Sand settled at x, y {x}, {y}")
        if not (x, y) in set(sand):
            return coords, parameters
        else:
            return False, False


@timer_func
def part_one(inputlist):

    xrange = [min(inputlist)[0], max(inputlist)[0]]
    yfloor = max([x[1] for x in inputlist])
    DEBUG1 and print(f"XRANGE: {xrange}, YFLOOR: {yfloor} {max(inputlist)[1]}")
    rock = [(498, 2), (500, 2), (499, 2), (501, 2), (502, 2)]
    rock = inputlist
    sand = []
    parameters = [yfloor, rock, sand]

    count = 0
    while True:
        count % 100 == 0 and print(f"Sand: {count}")
        DEBUG1 and print(f"\nSand # {count + 1}")
        res, parameters = move((500, 0), parameters)
        DEBUG1 and print(f"res: {res}")
        if res:
            sand.append(res)
            count += 1
            DEBUG1 and print(f"new sand {sand}")
        else:
            DEBUG1 and print(f"rock: {rock}, sand: {sand}")
            break
            #sys.exit("no more moves possible")
    print(f"Total sand dropped: {count}")
    return count


@timer_func
def part_two(inputlist):
    return


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
