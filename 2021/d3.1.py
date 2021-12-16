#  --- Day 3: Binary Diagnostic ---
#  You need to use the binary numbers in the diagnostic report to generate two new binary numbers (called the gamma rate and the epsilon rate).
#  The power consumption can then be found by multiplying the gamma rate by the epsilon rate.

#  Each bit in the gamma rate can be determined by finding the most common bit in the corresponding position of all numbers in the diagnostic report.
#  For example, given the following diagnostic report:

#  00100
#  11110
#  10110
#  10111
#  10101
#  01111
#  00111
#  11100
#  10000
#  11001
#  00010
#  01010
#  Considering only the first bit of each number, there are five 0 bits and seven 1 bits. Since the most common bit is 1, the first bit of the gamma rate is 1.

#  The most common second bit of the numbers in the diagnostic report is 0, so the second bit of the gamma rate is 0.

# #The most common value of the third, fourth, and fifth bits are 1, 1, and 0, respectively, and so the final three bits of the gamma rate are 110.

#  So, the gamma rate is the binary number 10110, or 22 in decimal.

#  The epsilon rate is calculated in a similar way; rather than use the most common bit, the least common bit from each position is used.
#  So, the epsilon rate is 01001, or 9 in decimal. Multiplying the gamma rate (22) by the epsilon rate (9) produces the power consumption, 198.

#  Use the binary numbers in your diagnostic report to calculate the gamma rate and epsilon rate, then multiply them together.
#  What is the power consumption of the submarine? (Be sure to represent your answer in decimal, not binary.)

#init vars
mcb=[]
lcb=[]
count=0
bit=[]
gamma=0
epsilon=0
list1=[]
list2=[]

for i in range(1, 14):
	bit.append(0)
	mcb.append(0)
	lcb.append(0)
#read a record
file1 = open('d03.in', 'r')
# From Puzzle5 the mcb are 001100100101, lcb are 110011011010. We must get rid of the first bit in each list

for line in file1:
	diag=line.split()
	count+=1
	for i,c in enumerate(diag[0]):
		bit[i+1]=bit[i+1]+int(c)
count=count/2


for i,c in enumerate(mcb, start=0):
	if (bit[i]) > count:
		mcb[i]=1
		lcb[i]=0
	else:
		mcb[i]=0
		lcb[i]=1
mcb[0]=0
lcb[0]=0

print("MCB: ",''.join(str(mcb)))
print("LCB: ",''.join(str(lcb)))


for i,n in enumerate(mcb):
	maxexp=(len(mcb)-1)
	gamma=gamma+mcb[i]*(2**(maxexp-i))
	epsilon=epsilon+lcb[i]*(2**(maxexp-i))
	multiply=gamma*epsilon
print("AdventOfCode 2021: Puzzle 5")
print("GAMMA: ", gamma, "EPSILON: ", epsilon, "POWER CONSUMPTION: ", multiply)

# Your puzzle answer was 2648450.