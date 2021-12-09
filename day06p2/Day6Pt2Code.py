#  --- Day 6: Lanternfish ---
#  --- Part Two ---
#  Suppose the lanternfish live forever and have unlimited food and space. Would they take over the entire ocean?

#  After 256 days in the example above, there would be a total of 26984457539 lanternfish!

#  
#  How many lanternfish would there be after 256 days?

#  The trick here is to recognise (unlike in the earlier Part 1) that all you need know is how many fisgh are of each age
# Each time some get to zero, the disappear and the same number of 8 day fish appear, the 'births'.
# At the same time, the number of 6 day fish increase by the number of births
# So in an array we might have as the number of fish of age distribution
# [5, 6, 3, 3, 1, 2, 0, 0, 0, 0]   => 0 day fish to 8 day fish ie 9 values

# These will become
# [6, 3, 3, 1, 2, 0, 5, 0, 0, 5]   => ie +5 on 6 day fish and 5 8 day fish

# Iterate this for 256 days, bingo!!
# Much simpler than the previous tree method (which might have been handy if we needed to know the age af any given fish......)


import sys



ages = [0,0,0,0,0,0,0,0,0]

file1 = open('Day6Input.txt', 'r')
for line in file1:
	diag=line.strip('\n')
	diag=diag.strip()
	a_list=diag.split(',')                                    #  https://www.kite.com/python/answers/how-to-split-a-string-into-a-list-of-integers-in-python
	map_object=map(int, a_list)
	school=list(map_object)
print("Original fish", len(school))
file1.close()

for age in range(0,8):                                       #  count number in each age bin
	ages[age]=school.count(age)
print(ages)

for day in range(256):
	births=ages.pop(0)
	ages.append(births)
	ages[6] += births
print(f"Total lanternfish {sum(ages)}")


#  Your puzzle answer was 1629570219571.