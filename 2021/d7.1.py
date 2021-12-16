#  --- Day 7: The Treachery of Whales ---
#  You quickly make a list of the horizontal position of each crab (your puzzle input).

#  For example, consider the following horizontal positions:

#  16,1,2,0,4,2,7,1,2,14
#  This means there's a crab with horizontal position 16, a crab with horizontal position 1, and so on.

#  Each change of 1 step in horizontal position of a single crab costs 1 fuel.
#  You could choose any horizontal position to align them all on, but the one that 'costs' the least is horizontal position 2:

#  Move from 16 to 2: 14
#  Move from 1 to 2: 1
#  Move from 2 to 2: 0
#  Move from 0 to 2: 2
#  Move from 4 to 2: 2
#  Move from 2 to 2: 0
#  Move from 7 to 2: 5
#  Move from 1 to 2: 1
#  Move from 2 to 2: 0
#  Move from 14 to 2: 12
#  This costs a total of 37
#  This is the cheapest possible outcome; more expensive outcomes include aligning at position 1 (41 fuel), position 3 (39 fuel), or position 10 (71 fuel).

#  Determine the horizontal position that the crabs can align to using the least fuel possible. How much fuel must they spend to align to that position?

import sys

def fuel_needed(crabs, aligned_pos):
	fuel = 0
	for crab in crabs:
		fuel += abs(aligned_pos - crab)
	return fuel

def iterate_crabs(crabs):
	max_pos = max(crabs)
	min_fuel = 9E20
	for aligned_pos in range(max_pos):
		fuel_demand = fuel_needed(crabs, aligned_pos)
		if fuel_demand < min_fuel:
			min_fuel = fuel_demand
	return min_fuel
	
#file1 = open('d07.inth', 'r')
file1 = open('d07.in', 'r')
for line in file1:
	diag=line.strip('\n').strip().split(',')
#	diag=diag.strip()
#	a_list=diag.split(',')                                    #  https://www.kite.com/python/answers/how-to-split-a-string-into-a-list-of-integers-in-python
#	map_object=map(int, a_list)
	map_object=map(int, diag)
	crabs=list(map_object)
file1.close()

print("Min fuel requirement", iterate_crabs(crabs))




min_fuel = 0





