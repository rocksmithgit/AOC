import sys
import numpy as np
from collections import defaultdict, Counter, deque


def get_data():
    infile = sys.argv[1] if len(sys.argv) > 1 else 'xx.in'
    for line in open(infile, 'r'):
        # L = [int(l.strip(line))]
        L = [l.strip(line)]
    return L


L = get_data()
#  print(L)
print(f'part one: {part_one(L)}')
print(f'part two: {part_two(L)}')