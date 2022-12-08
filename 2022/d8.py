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
            li = [int(x) for x in line.strip()]
            parsed.append(li)
        parsed = np.array(parsed)
    return parsed


@timer_func
def part_one(inputlist):
    """
    1.  For a cell, look at horiz (left/right), vert slice (up/down) and see if height is bigger than the max in slice:
    1a. If visible in EITHER direction the mark as visible
    :param inputlist:
    :return:
    """
    DEBUG1 and print(inputlist)
    total = 0
    num_rows, num_cols = inputlist.shape
    perimeter = num_cols*2 + (num_cols-2)*2
    DEBUG1 and print(f"rows: {num_rows}, cols: {num_cols}, perimeter: {perimeter}")
    for x in range(1, num_cols-1):
        for y in range(1, num_rows-1):
            tree = inputlist[y, x]
            DEBUG1 and print(f"x: {x}, y: {y}, test: {inputlist[0:, 0]}")  # [row1:row2, col1:cols]
            left = np.max(inputlist[y, 0:x])   # np.[(row, col)]
            right = np.max(inputlist[y, x+1:])   # np.[(row, col)]
            up = np.max(inputlist[0:y, x])  # np.[(row, col)]
            down = np.max(inputlist[y+1:, x])  # np.[(row, col)]
            if tree > left or tree > right or tree >  up or tree > down:
                DEBUG1 and print(f"VISIBLE!")
                total += 1
    return total + perimeter

@timer_func
def part_two(inputlist):
    """
    1.  For a cell, look at horiz (left/right), vert slice (up/down) and compare size of each tree to current:
    1a. Add 1 to # of trees seen (starts at 0)
    1b. If tree in list is same size or bigger than current tree break out of list
    2.  Multiply all directions
    :param inputlist:
    :return:
    """
    DEBUG2 and print(inputlist)
    total = 0
    num_rows, num_cols = inputlist.shape
    perimeter = (num_cols) * 2 + (num_cols - 2) * 2
    DEBUG2 and print(f"rows: {num_rows}, cols: {num_cols}, perimeter: {perimeter}")
    best = 0
    for x in range(1, num_cols-1):
        for y in range(1, num_rows-1):
            tree = inputlist[y, x]
            DEBUG2 and print(f"x: {x}, y: {y}, tree: {inputlist[y, x]}")  # [row1:row2, col1:cols]
            lscore, rscore, uscore, dscore = 0, 0, 0, 0
            llst = reversed(inputlist[y, 0:x].tolist())
            rlst = (inputlist[y, x + 1:].tolist())
            ulst = reversed(inputlist[0:y, x].tolist())
            dlst = (inputlist[y + 1:, x].tolist())
            for height in llst:
                lscore += 1
                DEBUG2 and print(f"Tree: {tree}, lscore num: {height}")
                if height >= tree:
                    DEBUG2 and print(f"lscore: {lscore}")
                    break
                else:
                    DEBUG2 and print(f"lscore: {lscore}")
            for height in rlst:
                rscore += 1
                DEBUG2 and print(f"Tree: {tree}, rscore num: {height}")
                if height >= tree:
                    DEBUG2 and print(f"rscore: {rscore}")
                    break
                else:
                    DEBUG2 and print(f"rscore: {rscore}")
            for height in ulst:
                uscore += 1
                DEBUG2 and print(f"Tree: {tree}, uscore num: {height}")
                if height >= tree:
                    DEBUG2 and print(f"uscore: {uscore}")
                    break
                else:
                    DEBUG2 and print(f"uscore: {uscore}")
            for height in dlst:
                dscore += 1
                DEBUG2 and print(f"Tree: {tree}, dscore num: {height}")
                if height >= tree:
                    DEBUG2 and print(f"dscore: {dscore}")
                    break
                else:
                    DEBUG2 and print(f"dscore: {dscore}")
            if lscore * rscore * uscore * dscore > best:
                DEBUG2 and print(f"BEST FOUND!! = lscore: {lscore}, rscore: {rscore}, dscore: {dscore}, uscore: {uscore}")
                best = lscore * rscore * uscore * dscore
    return best


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
