#  --- Day 5: Hydrothermal Venture ---
#  --- Part Two ---

#  An entry like 1,1 -> 3,3 covers points 1,1, 2,2, and 3,3.
#  An entry like 9,7 -> 7,9 covers points 9,7, 8,8, and 7,9.
#  Considering all lines from the above example would now produce the following diagram:

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


#  1.1....11.
#  .111...2..
#  ..2.1.111.
#  ...1.2.2..
#  .112313211
#  ...1.2....
#  ..1...1...
#  .1.....1..
#  1.......1.
#  222111....
#  You still need to determine the number of points where at least two lines overlap.
# In the above example, this is still anywhere in the diagram with a 2 or larger - now a total of 12 points.

#  Consider all of the lines. At how many points do at least two lines overlap?

import numpy as np
import sys

def my_iter(first_iter, last_iter, cons, stp, array, axis):
	print(f"my_iter: first iter {first_iter}, last_iter {last_iter}, constant axis {cons}, step {stp}\n CURRENT ARRAY\n {array}\n const axis {axis}")
# numpy arrays index [y,x]
	for each_iter in range(first_iter, last_iter+stp,stp):
		if axis=='Y':
			print(f"Current element value {cons}, {each_iter} {array[cons, each_iter]} Iteration {each_iter}")
			array[cons, each_iter]+=1
		elif axis=='X':
			print(f"Current element value {each_iter}, {cons} {array[each_iter, cons]} Iteration {each_iter}")
			array[each_iter, cons]+=1
		elif axis=='UR':
			print(f"Current element value {each_iter}, {cons-(each_iter-first_iter)} {array[each_iter, cons-(each_iter-first_iter)]} Iteration {each_iter}")
			array[cons-(each_iter-first_iter), each_iter]+=1
#			input("Press Enter to continue...")
		elif axis=='DR':
			print(f"Current element value {each_iter}, {cons+(each_iter-first_iter)} {array[each_iter, cons+(each_iter-first_iter)]} Iteration {each_iter}")
			array[cons+(each_iter-first_iter), each_iter]+=1
#			input("Press Enter to continue...")
		elif axis=='DL':
			print(f"Current element value {each_iter}, {cons-(each_iter-first_iter)} {array[each_iter, cons-(each_iter-first_iter)]} Iteration {each_iter}")
			array[cons-(each_iter-first_iter), each_iter]+=1
#			input("Press Enter to continue...")
		elif axis=='UL':
			print(f"Current element value ({each_iter}, {cons+(each_iter-first_iter)}) {array[each_iter, cons+(each_iter-first_iter)]} Iteration {each_iter}")
			array[cons+(each_iter-first_iter), each_iter]+=1
			print(f"New     element value ({each_iter}, {cons+(each_iter-first_iter)}) {array[each_iter, cons+(each_iter-first_iter)]} Iteration {each_iter}")
#			input("Press Enter to continue...")
		else:
			sys.exit("Error in axis for array")
	print(f"my_iter: {first_iter}, last_iter {last_iter}, constant axis {cons}, step {stp}\n NEW ARRAY\n {array}\n const axis {axis}")
	return array


vent_array=np.zeros((1000,1000))
readlines=[]

#file1 = open('d05.inth', 'r')
file1 = open('../day05p2/d05.in', 'r')
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
		if abs(x2-x1)!=abs(y2-y1):
			print(f"x2-x1: {abs(x2-x1)} y2-y1: {abs(y2-y1)}")
			print("NOT HORIZ, VERT OR 45 DEGREES")
			continue                                          # we don't want to process non-vert/non-horiz arrays
	if abs(x2-x1)==abs(y2-y1):                                # we are on a diagonal
		print(f"X2>X1: {x2>x1} Y2>Y1: {y2>y1}")
		print(f"X2<X1: {x2<x1} Y2<Y1: {y2<y1}")
		if x2>x1 and y2>y1:
			axis='DR'
			print(axis)
			stp=1
		elif x2>x1 and y2<y1:
			axis='UR'
			print(axis)
			stp=1
		elif x2<x1 and y2>y1:
			axis='DL'
			print(axis)
			stp=-1
		elif x2<x1 and y2<y1:
			axis='UL'
			print(axis)
			stp=-1
		else:
			sys.exit("Error in diagonal calcs")
		my_iter(x1, x2, y1, stp, vent_array, axis)
		continue
	if x2<x1 or y2<y1:                                        # are we going to iterate +ve or -ve
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
print("*********************************************************************************************")


#  Your puzzle answer was 21038.