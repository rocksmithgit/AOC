#  --- Day 9: Smoke Basin ---

#  Smoke flows to the lowest point of the area it's in. For example, consider the following heightmap:

#  2199943210
#  3987894921
#  9856789892
#  8767896789
#  9899965678
#  Each number corresponds to the height of a particular location, where 9 is the highest and 0 is the lowest a location can be.

#  Your first goal is to find the low points - the locations that are lower than any of its adjacent locations.
#  Most locations have four adjacent locations (up, down, left, and right);
#  locations on the edge or corner of the map have three or two adjacent locations, respectively. (Diagonal locations do not count as adjacent.)

#  In the above example, there are four low points, all highlighted:
#     two are in the first row (a 1 and a 0),
#     one is in the third row (a 5),
#     and one is in the bottom row (also a 5).
#  All other locations on the heightmap have some lower adjacent location, and so are not low points.

#   The risk level of a low point is 1 plus its height.
#   In the above example, the risk levels of the low points are 2, 1, 6, and 6.
#   The sum of the risk levels of all low points in the heightmap is therefore 15.

#  Find all of the low points on your heightmap. What is the sum of the risk levels of all low points on your heightmap?

import numpy as np

#lava = np.zeros(shape=(5, 10))
lava = np.zeros(shape=(100, 100))

def check_x(array, y, x):
#    print(array.shape[1])
    if x > 0 and x < array.shape[1] - 1:
        if array[y, x] < array[y, x - 1] and array[y, x] < array[y, x + 1]:
            return True
        else:
            return False
    else:
        if x == 0:
            if array[y, x] < array[y, x + 1]:
                return True
            else:
                return False
        elif x == array.shape[1] - 1:
            if array[y, x] < array[y, x - 1]:
                return True
            else:
                return False


def check_y(array, y, x):
    if y > 0 and y < array.shape[0] - 1:
        if array[y, x] < array[y - 1, x] and array[y, x] < array[y + 1, x]:
            return True
        else:
            return False
    else:
        if y == 0:
            if array[y, x] < array[y + 1, x]:
                return True
            else:
                return False
        elif y == array.shape[0] - 1:
            if array[y, x] < array[y - 1, x]:
                return True
            else:
                return False


#file1 = open('d09.inth', 'r')
file1 = open('d09.in', 'r')
count = -1
for line in file1:
    count += 1
    diag = line.strip('\n').strip()
    for x in range(len(diag)):
        lava[count, x] = int(diag[x])
#    print(diag)


total = 0
for r in range(100):
    for c in range(100):
        # print(lava)
        # print(check_x(lava, 1, 0))
        # print(check_y(lava, 1, 0))
#        print(f"{c}, {r}, {lava[r, c]}")
        if check_x(lava, r, c) == check_y(lava, r, c) == True:
            print(f"MINIMUM FOUND, x {c} y {r} value {lava[r, c]}")
            total += 1 + lava[r, c]
print(f"TOTAL {total}")

#  Your puzzle answer was 570.