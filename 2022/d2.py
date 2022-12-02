import sys
import numpy as np
from collections import defaultdict, Counter, deque
from pathlib import Path


def get_data(inputdata):
    infile = sys.argv[1] if len(sys.argv) > 1 else inputdata
    theirs = []
    mine = []
    for line in open(infile, 'r'):
        if line.strip():
            stripped = line.strip()
            their_go, my_go = stripped.split()
            theirs.append(their_go)
            mine.append(my_go)
    zipped = list(zip(theirs, mine))
    return zipped

# Rock: 1, Paper 2, Scissors 3
# Rock vs Paper     = 1 - 2 = -1; win for Paper
# Rock vs Scissors  = 1 - 3 = -2; win for Rock
# Paper vs Scissors = 2 - 3 = -1; win for Scissors
# => if result is -1 winner is second variable, if result is -2 winner is first variable
# => if result is 1 winner is first variable, if result is 2 winner is second variable
# => is result is 0 is a draw
# 0 for loss, 3 for draw, 6 for win


def part_one(inputlist):
    # A, B, C = X, Y, Z = Rock, Paper, Scissors
    # Rock: 1, Paper 2, Scissors 3
    # Rock vs Paper     = 1 - 2 = -1; win for Paper
    # Rock vs Scissors  = 1 - 3 = -2; win for Rock
    # Paper vs Scissors = 2 - 3 = -1; win for Scissors
    # => if result is -1 winner is second variable, if result is -2 winner is first variable
    # => if result is 1 winner is first variable, if result is 2 winner is second variable
    # => is result is 0 is a draw
    # 0 for loss, 3 for draw, 6 for win
    total = 0
    shapes = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}
    winscore = [3, 6, 0]
    for each in inputlist:
        comparitor = shapes[each[0]] - shapes[each[1]]
        if comparitor == 0:
            w = winscore[0]
            total += (w + shapes[each[1]])
        elif comparitor == -1 or comparitor == 2:
            w = winscore[1]
            total += (w + shapes[each[1]])
        else:
            w = winscore[2]
            total += (w + shapes[each[1]])
#        print(f"Comparitor: {comparitor}, Elf shape: {each[0]}=>{shape[each[0]]}, My shape: {each[1]}=>{shape[each[1]]}, Shape score: {shapes[each[1]]}, WinScore: {W}, Total: {total}")
    return total


def part_two(inputlist):

    total = 0
    res = {'X': 0, 'Y': 3, 'Z': 6}
    reqd_shape = {'A': {'X': 3, 'Y': 1, 'Z': 2}, 'B': {'X': 1, 'Y': 2, 'Z': 3}, 'C': {'X': 2, 'Y': 3, 'Z': 1}}
    for each in inputlist:
        total += res[each[1]] + reqd_shape[each[0]][each[1]]
    return total


inputData = 'd2.in'
L = get_data(inputData)
print(f"ADVENT OF CODE: {Path(__file__).stem}")
print(f'part one: {part_one(L)}')
print(f'part two: {part_two(L)}')
