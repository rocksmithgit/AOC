#  --- Day 7: The Treachery of Whales ---

#  --- Part Two ---

#  Instead, each change of 1 step in horizontal position costs 1 more unit than the last:
#  the first step costs 1, the second step costs 2, the third step costs 3, and so on.

#  As each crab moves, moving further becomes more expensive.
#  This changes the best horizontal position to align them all on; in the example above, this becomes 5:

#  Move from 16 to 5: 66
#  Move from 1 to 5: 10
#  Move from 2 to 5: 6
#  Move from 0 to 5: 15
#  Move from 4 to 5: 1
#  Move from 2 to 5: 6
#  Move from 7 to 5: 3
#  Move from 1 to 5: 10
#  Move from 2 to 5: 6
#  Move from 14 to 5: 45
#  This costs a total of 168 fuel.
#  This is the new cheapest possible outcome; the old alignment position (2) now costs 206 instead.

#  Determine the horizontal position that the crabs can align at least cost


import sys

def fuel_needed(crabs, aligned_pos, type):
	fuel = 0
	for crab in crabs:
		if type == "constant":
			fuel += abs(aligned_pos - crab)
		else:
			fuel += abs(aligned_pos - crab) * (abs(aligned_pos - crab)+1)/2
	return fuel

def iterate_crabs(crabs, type):
	max_pos = max(crabs)
	min_fuel = 9E20
	for aligned_pos in range(max_pos):
		fuel_demand = fuel_needed(crabs, aligned_pos, type)
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

print("Min fuel requirement, constant", iterate_crabs(crabs,"constant"))
print("Min fuel requirement, ramped", iterate_crabs(crabs,"ramped"))


#  Part 2 Your puzzle answer was 336131.
