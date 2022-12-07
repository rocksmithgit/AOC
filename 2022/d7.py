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
            parsed.append(line.strip())
    return parsed


def part_one_abandonded(inputlist):
    """
    1. Traverse instructions to build tree
    2. Traverse instructions to build files and totals
    :param inputlist:
    :return:
    """
    # 1.
    below = defaultdict(list)
    above = defaultdict(list)
    current_dir = None
    for line in inputlist:
        DEBUG1 and print(f"current line: {line}")
        if line.startswith('$ cd '):
            current_dir = line[5:]
            DEBUG1 and print(f"Current dir: {current_dir}")
            continue
        elif line.startswith('dir '):
            found_dir = line[4:]
            DEBUG1 and print(f"Dir Found: {found_dir}")
            below[current_dir].append(found_dir)
            above[found_dir].append(current_dir)
            DEBUG1 and print(f"Directory tree, Current dir: {current_dir}, dir to add: {found_dir}, above: {above}, below: {below} ")

    sizes = defaultdict(list)
    names = defaultdict(list)
    current_dir = None
    DEBUG1 and print("FILESIZES")
    for line in inputlist:
        if line.startswith('$ cd '):
            current_dir = line[5:]
            continue
        elif not line.startswith('$ ls') and not line.startswith('dir '):
            DEBUG1 and print(f"line {line}")
            sz, name = line.split()
            sz = int(sz)
            sizes[current_dir].append(sz)
            names[current_dir].append(name)
            DEBUG1 and print(f"Directory tree, Current dir: {current_dir}, name to add: {name}, sizes: {sizes}, names: {names}")

    totals = defaultdict(list)
    for elem in sizes:
        print(f"Elem: {elem}, Size_list {sizes[elem]}, Total size: {sum(sizes[elem])}")
        totals[elem] = sum(sizes[elem])
    return

@timer_func
def part_one(inputlist):
    """
    1.  Every time we see 'cd' not followed by '..' make the argument (the current dir) the value of dir_list
    1a. Every time you see 'cd' followed by '..' then remove last part of path from dir_list
    2.  Ignore 'ls' commands as they don;t do anything :)
    3.  Ignore 'dir' statements as we will pick up their size via a 'cd'
    4.  For file size data (ie not 'cd', 'dir' or 'ls' it will be size / name, add to a dictionary that has keys equal
        to a tuple made from the directory path)
    4a. Add the current file_size to every path key above and including the current directory
    5.  Sum the size of directories if they are less than stated size
    :param inputlist:
    :return:
    """
    path = []
    dirs = defaultdict(int)

    for instruction in inputlist:
        args = instruction.split()
        if args[0] == "$":
            if args[1] == "cd":
                if args[2] == "..":
                    path.pop()
                else:
                    path.append(args[2])
        elif args[0] != "dir":
            for i in range(len(path)):
                DEBUG1 and print(f"Path: {path}")
                dirs[tuple(path[: i + 1])] += int(args[0])
                DEBUG1 and print(f"TUPLE: {dirs[tuple(path[: i + 1])]}")
    total = (sum(size for size in dirs.values() if size <= 100000))

    return total

@timer_func
def part_two(inputlist):
    """
    1.  Every time we see 'cd' not followed by '..' make the argument (the current dir) the value of dir_list
    1a. Every time you see 'cd' followed by '..' then remove last part of path from dir_list
    2.  Ignore 'ls' commands as they don;t do anything :)
    3.  Ignore 'dir' statements as we will pick up their size via a 'cd'
    4.  For file size data (ie not 'cd', 'dir' or 'ls' it will be size / name, add to a dictionary that has keys equal
        to a tuple made from the directory path)
    4a. Add the current file_size to every path key above and including the current directory
    5.  Calculate the reqd directory size to free space ie update_size - (capacity - total_used) when total_used is
        just the size of '/'
    :param inputlist:
    :return:
    """
    path = []
    dirs = defaultdict(int)
    for instruction in inputlist:
        args = instruction.split()
        if args[0] == "$":
            if args[1] == "cd":
                if args[2] == "..":
                    path.pop()
                else:
                    path.append(args[2])
        elif args[0] != "dir":
            for i in range(len(path)):
                dirs[tuple(path[: i + 1])] += int(args[0])
    required = 30000000 - (70000000 - dirs[("/",)])
    total = min(size for size in dirs.values() if size >= required)
    return total


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
