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
def part_one_abandonded(inputlist):
    """
    1. use tuples to store position of head and tail
    2. If delta of x or y pos > 1 then move 1 step closer in that axis
    3. Update new position
    """
    head_v_tail = [0, 0]
    tail_visits = [(0, 0)]
    direction = {'U': 1, 'D': -1, 'L': -1, 'R': 1}
    for instruction in inputlist:
        new_tail_x = tail_visits[-1][0]
        new_tail_y = tail_visits[-1][1]
        DEBUG1 and print(f"\nDirection: {instruction[0]}, Size: {instruction[1]}")
        if instruction[0] == 'L' or instruction[0] == 'R':
            for move in range(instruction[1]):
                head_v_tail[0] = head_v_tail[0] + direction[instruction[0]]          # move head
                DEBUG1 and print(f"Starting Head-Tail Delta: ({head_v_tail[0]-direction[instruction[0]]}, {head_v_tail[1]}), Intermediate Head Delta: {head_v_tail}")
                if abs(head_v_tail[0]) > 1:  # check if > 1 in that axis
                    new_tail_x = new_tail_x + direction[instruction[0]]  # if so move 1 unit closer in BOTH axis
                    head_v_tail[0] = head_v_tail[0] - direction[instruction[0]]
                    if head_v_tail[1] > 0:
                        new_tail_y = new_tail_y + 1
                        head_v_tail[1] = head_v_tail[1] - 1
                    if head_v_tail[1] < 0:
                        new_tail_y = new_tail_y - 1
                        head_v_tail[1] = head_v_tail[1] + 1
                else:
                    DEBUG1 and print("NO MOVE!!")
                DEBUG1 and print(f"New Tail pos: ({new_tail_x}, {new_tail_y}), Final Head Delta {head_v_tail})")
                tail_visits.append((new_tail_x, new_tail_y))
        else:
            for move in range(instruction[1]):
                head_v_tail[1] = head_v_tail[1] + direction[instruction[0]]          # move head
                DEBUG1 and print(f"Starting Head-Tail Delta: ({head_v_tail[0]}, {head_v_tail[1]-direction[instruction[0]]}), Intermediate Head Delta: {head_v_tail}")
                if abs(head_v_tail[1]) > 1:  # check if > 1 in that axis
                    new_tail_y = new_tail_y + direction[instruction[0]]  # if so move 1 unit closer in BOTH axis
                    head_v_tail[1] = head_v_tail[1] - direction[instruction[0]]
                    if head_v_tail[0] > 0:
                        new_tail_x = new_tail_x + 1
                        head_v_tail[0] = head_v_tail[0] - 1
                    if head_v_tail[0] < 0:
                        new_tail_x = new_tail_x - 1
                        head_v_tail[0] = head_v_tail[1] + 1
                else:
                    DEBUG1 and print("NO MOVE!!")
                DEBUG1 and print(f"New Tail pos: ({new_tail_x}, {new_tail_y}), Final Head Delta {head_v_tail})")
                tail_visits.append((new_tail_x, new_tail_y))
    DEBUG1 and print(f"Total Tail visits: {len(tail_visits)}, Unique visits: {len(set(tail_visits))}")
    return len(set(tail_visits))


@timer_func
def part_one(inputlist):
    positions = [[0, 0], [0, 0]]   # hold the head [0] and tail [1] positions
    tail_pos = set()
    leftright = {"R": 1, "L": -1}                 # hold the direction/size of L/R moves
    updown = {"U": 1, "D": -1}                    # hold the direction/size of L/R moves
    for instruction in inputlist:
        direction, steps = instruction.split()
        for step in range(int(steps)):
            positions[0][0] += leftright.get(direction, 0)  # update L/R position of head; no move if not in Dict
            positions[0][1] += updown.get(direction, 0)     # update U/D position of head; no move if not in Dict
            xdist = positions[0][0]-positions[1][0]  # how far are we apart in the x direction
            ydist = positions[0][1]-positions[1][1]  # how far are we apart in the y direction
            if xdist**2 + ydist**2 > 2:        # we will move if more than 1 step away ie further than 1^2 + 1^2 =2
                positions[1][0] += np.sign(xdist)  # sign returns -1, 0, +1 based on sign of argument
                positions[1][1] += np.sign(ydist)
            tail_pos.add(tuple(positions[-1]))
    return len(tail_pos)


@timer_func
def part_two(inputlist, knots):
    positions = [[0, 0] for _ in range(knots)]   # hold the head [0] AND knot [...] and tail [-1] positions
    tail_pos = set()
    leftright = {"R": 1, "L": -1}                 # hold the direction/size of L/R moves
    updown = {"U": 1, "D": -1}                    # hold the direction/size of L/R moves
    for instruction in inputlist:
        direction, steps = instruction.split()
        for step in range(int(steps)):
            positions[0][0] += leftright.get(direction, 0)  # update L/R position of head; no move if not in Dict
            positions[0][1] += updown.get(direction, 0)     # update U/D position of head; no move if not in Dict
            for segment in range(1, len(positions)):  # we now treat each segment as the entire rope before!!
                xdist = positions[segment-1][0]-positions[segment][0]  # how far are we apart in the x direction
                ydist = positions[segment-1][1]-positions[segment][1]  # how far are we apart in the y direction
                if xdist**2 + ydist**2 > 2:        # we will move if more than 1 step away ie further than 1^2 + 1^2 =2
                    positions[segment][0] += np.sign(xdist)  # sign returns -1, 0, +1 based on sign of argument
                    positions[segment][1] += np.sign(ydist)
            tail_pos.add(tuple(positions[-1]))
    return len(tail_pos)


total_time = []
DEBUG0 = False
DEBUG1 = True
DEBUG2 = False
TESTING = False

if TESTING:
    inputData = f'{Path(__file__).stem}_test.in'
else:
    inputData = f'{Path(__file__).stem}.in'

print(f"ADVENT OF CODE: {Path(__file__).stem}")
L = get_data(inputData)
print(f"Part one: {part_one(L)}")
print(f"Part two: {part_two(L, 10)}")
print(f"Elapsed Total time: {sum(total_time):.4f}s")
