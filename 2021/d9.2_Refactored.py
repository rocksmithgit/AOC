#  --- Day 9: Smoke Basin ---
# These caves seem to be lava tubes. Parts are even still volcanically active;
# small hydrothermal vents release smoke into the caves that slowly settles like rain.

#  If you can model how the smoke flows through the caves, you might be able to avoid it and be that much safer.
#  The submarine generates a heightmap of the floor of the nearby caves for you (your puzzle input).

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
#  --- Part Two ---
#  Next, you need to find the largest basins so you know what areas are most important to avoid.

#  A basin is all locations that eventually flow downward to a single low point.
#  Therefore, every low point has a basin, although some basins are very small. Locations of height 9 do not count as being in any basin, and all other locations will always be part of exactly one basin.

#  The size of a basin is the number of locations within the basin, including the low point. The example above has four basins.

#  The top-left basin, size 3:

#  2199943210
#  3987894921
#  9856789892
#  8767896789
#  9899965678
#  The top-right basin, size 9:

#  2199943210
#  3987894921
#  9856789892
#  8767896789
#  9899965678
#  The middle basin, size 14:

#  2199943210
#  3987894921
#  9856789892
#  8767896789
#  9899965678
#  The bottom-right basin, size 9:

#  2199943210
#  3987894921
#  9856789892
#  8767896789
#  9899965678
#  Find the three largest basins and multiply their sizes together. In the above example, this is 9 * 14 * 9 = 1134.

#  What do you get if you multiply together the sizes of the three largest basins?


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

def is_similar(y, x, new):
    if lava[y,x] < 9 and lava[y,x] != new:
        return True
    else:
        return False


def flood_fill(x, y, old, new):
    # we need the x and y of the start position, the old value,
    # and the new value
    # the flood fill has 4 parts
    # firstly, make sure the x and y are inbounds
    if x < 0 or x >= len(lava[0]) or y < 0 or y >= len(lava):
        return
    # secondly, check if the current position equals the old value
    if is_similar(y,x,new) == False:
        return

    # thirdly, set the current position to the new value
    lava[y, x] = new
    count[0] += 1
#    print(count[0])
    # fourthly, attempt to fill the neighboring positions
    flood_fill(x + 1, y, old, new)
    flood_fill(x - 1, y, old, new)
    flood_fill(x, y + 1, old, new)
    flood_fill(x, y - 1, old, new)


#file1 = open('d09.inth', 'r')
file1 = open('d09.in', 'r')
count = -1
for line in file1:
    count += 1
    diag = line.strip('\n').strip()
    for x in range(len(diag)):
        lava[count, x] = int(diag[x])
#    print(diag)

temp_list = []
found_coords = []
total = 0
#for r in range(5):
#    for c in range(10):
for r in range(100):
    for c in range(100):
        temp_list = []
        # print(lava)
        # print(check_x(lava, 1, 0))
        # print(check_y(lava, 1, 0))
#        print(f"{c}, {r}, {lava[r, c]}")
        if check_x(lava, r, c) == check_y(lava, r, c) == True:
            print(f"MINIMUM FOUND, x {c} y {r} value {lava[r, c]}")
            total += 1 + lava[r, c]
            temp_list.append(r)
            temp_list.append(c)
#            print(temp_list)
            found_coords.append(temp_list)
            print(f"found coords {found_coords}")
            print(f"number_found {len(found_coords)} ")
print(f"TOTAL {total}")

#  Your puzzle answer was 570.

# fill the array with '0' unless the value is '9' since that mark the boundary edges
print(f"There are {len(found_coords)} minimums")
#for r in range(5):
#    for c in range(10):
#for r in range(100):
#    for c in range(100):
#        if lava[r, c] != 9:
#            lava[r, c] = 0
#print(f"new array\n {lava}")


# now we are going to fill the array with '1' and count them
big_basin = [0, 0, 0]
for item in found_coords:
    count = [0]
    r = item[0]
    c = item[1]
    flood_fill(c, r, 0, 1)
#    print(count[0])
    if count[0] > min(big_basin):
        big_basin.pop(0)
        big_basin.append(count[0])
        big_basin = sorted(big_basin)

print(sorted(big_basin))
print(f"If you multiply the 3 largest basins you get {big_basin[0]*big_basin[1]*big_basin[2]}")

# Your puzzle answer was 899392.