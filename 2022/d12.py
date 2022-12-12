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
            list = [letter for letter in line.strip()]
            parsed.append(list)
    return parsed


def shortest_path(graph, node1, node2):
    path_list = [[node1]]
    path_index = 0
    # To keep track of previously visited nodes
    previous_nodes = {node1}
    if node1 == node2:
        return path_list[0]

    while path_index < len(path_list):
        current_path = path_list[path_index]
        last_node = current_path[-1]
        next_nodes = graph[last_node]
        # Search goal node
        if node2 in next_nodes:
            current_path.append(node2)
            return current_path
        # Add new paths
        for next_node in next_nodes:
#            if not next_node in previous_nodes:
            if next_node not in previous_nodes:
                new_path = current_path[:]
                new_path.append(next_node)
                path_list.append(new_path)
                # To avoid backtracking
                previous_nodes.add(next_node)
        # Continue to next path in list
        path_index += 1
    # No path is found
    return []

total_time = []
matrix = get_data('d12.in')

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == 'S':
            src = (i, j)
        if matrix[i][j] == 'E':
            dest = (i, j)

multi_src = []
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == 'a':
            multi_src.append((i, j))

ords = {key: ord(key) for key in 'abcdefghijklmnopqrstuvwxyz'}
ords['S'] = ord('a')
ords['E'] = ord('z')
graph = {}
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        XY = (i, j)
        graph[XY] = set()
        if i+1 < len(matrix) and (ords[matrix[i+1][j]] - ords[matrix[i][j]]) <= 1:
            tup = (i+1,j)
            graph[XY].add(tup)
        if i-1 >= 0 and (ords[matrix[i-1][j]] - ords[matrix[i][j]]) <= 1:
            tup = (i-1,j)
            graph[XY].add(tup)
        if j+1 < len(matrix[0]) and (ords[matrix[i][j+1]] - ords[matrix[i][j]]) <= 1:
            tup = (i, j+1)
            graph[XY].add(tup)
        if j-1 >= 0 and (ords[matrix[i][j-1]] - ords[matrix[i][j]]) <= 1:
            tup = (i, j-1)
            graph[XY].add(tup)

@timer_func
def part_one(graph, src, dest):
    print(f"Part 1: Shortest path: {len(shortest_path(graph, src, dest))-1}")
    return len(shortest_path(graph, src, dest))-1


@timer_func
def part_two(graph, src, dest):
    multi_result = [len(shortest_path(graph, src, dest))-1 for src in multi_src if len(shortest_path(graph, src, dest)) > 0]
    print(f"Part 2: Shortest path from an 'a': {min(multi_result)}")
    return min(multi_result)


DEBUG0 = False
DEBUG1 = False
DEBUG2 = False
TESTING = False

if TESTING:
    inputData = f'{Path(__file__).stem}_test.in'
else:
    inputData = f'{Path(__file__).stem}.in'

print(f"ADVENT OF CODE: {Path(__file__).stem}")
print(f"Part one: {part_one(graph, src, dest)}")
print(f"Part two: {part_two(graph, src, dest)}")
print(f"Elapsed Total time: {sum(total_time):.4f}s")