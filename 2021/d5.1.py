#  --- Day 5: Hydrothermal Venture ---

# a list of nearby lines of vents (your puzzle input) for you to review. For example:

#  0,9 -> 5,9
#  8,0 -> 0,8
#  9,4 -> 3,4
#  2,2 -> 2,1
#  7,0 -> 7,4
#  6,4 -> 2,0
#  0,9 -> 2,9
#  3,4 -> 1,4
#  0,0 -> 8,8
#  5,5 -> 8,2

#  An entry like 1,1 -> 1,3 covers points 1,1, 1,2, and 1,3.
#  An entry like 9,7 -> 7,7 covers points 9,7, 8,7, and 7,7.
#  For now, only consider horizontal and vertical lines: lines where either x1 = x2 or y1 = y2.

#  So, the horizontal and vertical lines from the above list would produce the following diagram:

#  .......1..
#  ..1....1..
#  ..1....1..
#  .......1..
#  .112111211
#  ..........
#  ..........
#  ..........
#  ..........
#  222111....
#  In this diagram, the top left corner is 0,0 and the bottom right corner is 9,9. Each position is shown as the number of lines which cover that point or '.' if no line covers that point.
#  The top-left pair of 1s, for example, comes from 2,2 -> 2,1; the very bottom row is formed by the overlapping lines 0,9 -> 5,9 and 0,9 -> 2,9.

#  Consider only horizontal and vertical lines. At how many points do at least two lines overlap?

import numpy as np

def my_iter(first_iter, last_iter, cons, stp, array, axis):
	print(f"my_iter: {first_iter}, last_iter {last_iter}, constant axis {cons}, step {stp}\n CURRENT ARRAY\n {array}\n const axis {axis}")
	for each_iter in range(first_iter, last_iter+stp,stp):
		if axis=='Y':
			print(f"Currect element value {array[cons, each_iter]} Iteration {each_iter}")
			array[cons, each_iter]=array[cons, each_iter]+1
		elif axis=='X':
			print(f"Currect element value {array[each_iter, cons]} Iteration {each_iter}")
			array[each_iter ,cons ]=array[each_iter ,cons ]+1
		else:
			sys.exit("Error in axis for array")
	print(f"my_iter: {first_iter}, last_iter {last_iter}, constant axis {cons}, step {stp}\n NEW ARRAY\n {array}\n const axis {axis}")
	return array

#readlines =[[1 ,2 ,1 ,4] ,[3 ,2 ,1 ,4] ,[5 ,7 ,8 ,9]]
#vent_array=np.array[[0 ,0 ,0 ,0, 0, 0, 0, 0, 0],
#					[0 ,0 ,0 ,0, 0, 0, 0, 0, 0],
#					[0 ,0 ,0 ,0, 0, 0, 0, 0, 0],
#					[0 ,0 ,0 ,0, 0, 0, 0, 0, 0],
#					[0 ,0 ,0 ,0, 0, 0, 0, 0, 0],
#					[0 ,0 ,0 ,0, 0, 0, 0, 0, 0],
##					[0 ,0 ,0 ,0, 0, 0, 0, 0, 0],
#	#				[0 ,0 ,0 ,0, 0, 0, 0, 0, 0],
#					[0 ,0 ,0 ,0, 0, 0, 0, 0, 0],
#					[0 ,0 ,0 ,0, 0, 0, 0, 0, 0]]
vent_array=np.zeros((1000,1000))
readlines=[]

file1 = open('d05.in', 'r')
for line in file1:
	diag=line.strip('\n')
	diag=diag.strip()
	diag=diag.replace(' -> ',',')
	diag=diag.split(',')
#	print(diag)
	readlines.append(diag)
file1.close()
#print(vent_array)

for coords in readlines:
	stp=1
	x1=int(coords[0])
	y1=int(coords[1])
	x2=int(coords[2])
	y2=int(coords[3])
#	print(coords)
	print(f"\nX1: {x1}, Y1: {y1}, X2: {x2}, Y2: {y2}")
	if x1!=x2 and y1!=y2:
		print("NOT HORIZ OR VERT")
		continue                                          # we don't want to process non-vert/non-horiz arrays
	if x2<x1 or y2<y1:                                    # are we going to iterate +ve or -ve
		stp = -1
	if x1!=x2: 
		axis = 'Y'
		my_iter(x1, x2, y1, stp, vent_array, axis)
	elif y1!=y2:
		axis = 'X'
		my_iter(y1, y2, x1, stp, vent_array, axis)
	else:
		sys.exit("Error in axis for array")

print("\nFinal MATRIX\n", vent_array)
print(f"\nTotal with more than 2 crossings {np.count_nonzero(vent_array>=2)}")
print("**************************************************************************")

## Your puzzle answer was 7297.