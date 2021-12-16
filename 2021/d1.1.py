#  Find # times the depth sounding increases relative to the last one
#  The first increase does not count as there is no previous sounding
# --- Day 1: Sonar Sweep ---
# --- Part One ---

#  For example, suppose you had the following report:

#  199
#  200
#  208
#  210
#  200
#  207
#  240
#  269
#  260
#  263

#  C00ount the number of times a depth measurement increases from the previous measurement. (There is no measurement before the first measurement.) In the example above, the changes are as follows:

#  199 (N/A - no previous measurement)
#  200 (increased)
#  208 (increased)
#  210 (increased)
#  200 (decreased)
#  207 (increased)
#  240 (increased)
#  269 (increased)
#  260 (decreased)
#  263 (increased)
#  In this example, there are 7 measurements that are larger than the previous measurement.

#  How many measurements are larger than the previous measurement?

#  Your puzzle answer was 1215.

last_depth=999999999999999         # Make this large enough so the first value is lower
current_depth=0
count=0

#read a record

file1 = open('d01.in', 'r')

for line in file1:
	current_depth=float(line.strip())

	if current_depth > last_depth:
		count+=1

	last_depth=current_depth


print()
print("AdventOfCode 2021: Puzzle 1")
print("The number of times soundings increase is: ",count)

file1.close()

#  Your puzzle answer was 1215.