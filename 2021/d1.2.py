#  --- Day 1: Sonar Sweep ---
#  --- Part Two ---
#  Now consider sums of a three-measurement sliding window.

#  199  A      
#  200  A B    
#  208  A B C  
#  210    B C D
#  200  E   C D
#  207  E F   D
#  240  E F G  
#  269    F G H
#  260      G H
#  263        H

#  In the above example, the sum of each three-measurement window is as follows:

#  A: 607 (N/A - no previous sum)
#  B: 618 (increased)
#  C: 618 (no change)
#  D: 617 (decreased)
#  E: 647 (increased)
#  F: 716 (increased)
#  G: 769 (increased)
#  H: 792 (increased)
#  In this example, there are 5 sums that are larger than the previous sum.

#  Consider sums of a three-measurement sliding window.
#  How many sums are larger than the previous sum?

last_but_one_depth=99999
last_depth=99999         # Make this large enough so the first value is lower
current_depth=0
last_window_depth=999999999999999
count=0
rec=0



#read a record

file1 = open('d01.in', 'r')

for line in file1:
	current_depth=float(line.strip())
	current_window_depth=last_but_one_depth+last_depth+current_depth
	rec+=1

	if rec > 3 and current_window_depth > last_window_depth:
		count+=1

	print("Current: ",current_depth, "Last_depth: ", last_depth, "Last but one depth: ", last_but_one_depth, "Window Total: ", current_window_depth, "Last Window Total: ", last_window_depth,"Increase Count: ", count)
#	input("Press Enter to continue...")
	
	last_window_depth=current_window_depth
	last_but_one_depth=last_depth
	last_depth=current_depth
	



print()
print("AdventOfCode 2021: Puzzle 2")
print("The number of times soundings window increases is: ",count)

file1.close()

# Your puzzle answer was 1150.

# Both parts of this puzzle are complete! They provide two gold stars: **