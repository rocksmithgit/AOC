#  --- Day 4: Giant Squid ---

#  Bingo is played on a set of boards each consisting of a 5x5 grid of numbers.
#  Numbers are chosen at random, and the chosen number is marked on all boards on which it appears.
#  (Numbers may not appear on all boards.) If all numbers in any row or any column of a board are marked, that board wins. (Diagonals don't count.)


#  a random order in which to draw numbers and a random set of boards (your puzzle input). For example:

#  7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

#  22 13 17 11  0
#  8  2 23  4 24
#  21  9 14 16  7
#   6 10  3 18  5
#   1 12 20 15 19

#   3 15  0  2 22
#   9 18 13 17  5
#  19  8  7 25 23
#  20 11 10 24  4
#  14 21 16 12  6

#  14 21 17 24  4
#  10 16 15  9 19
#  18  8 23 26 20
#  22 11 13  6  5
#   2  0 12  3  7
#  After the first five numbers are drawn (7, 4, 9, 5, and 11), there are no winners, but the boards are marked as follows
#  (shown here adjacent to each other to save space):

#  22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
#   8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
#  21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
#   6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
#   1 12 20 15 19        14 21 16 12  6         2  0 12  3  7
#  After the next six numbers are drawn (17, 23, 2, 0, 14, and 21), there are still no winners:

#  22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
#   8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
#  21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
#   6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
#   1 12 20 15 19        14 21 16 12  6         2  0 12  3  7
#  Finally, 24 is drawn:

#  22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
#   8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
#  21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
#   6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
#   1 12 20 15 19        14 21 16 12  6         2  0 12  3  7
#  At this point, the third board wins because it has at least one complete row or column of marked numbers
#  (in this case, the entire top row is marked: 14 21 17 24 4).

#  The score of the winning board can now be calculated. Start by finding the sum of all unmarked numbers on that board; in this case, the sum is 188.
#  Then, multiply that sum by the number that was just called when the board won, 24, to get the final score, 188 * 24 = 4512.

#  To guarantee victory against the giant squid, figure out which board will win first. What will your final score be if you choose that board?

#  --- Part Two ---
#  Figure out which board will win last. Once it wins, what would its final score (sum of unmarked numbers) be?




#  22, 13, 17, 11,  0
#   8,  2, 23,  4, 24
#  21,  9, 14, 16,  7
#   6, 10,  3, 18,  5
#   1, 12, 20, 15, 19

#   3, 15,  0,  2, 22
#   9, 18, 13, 17,  5
#  19,  8,  7, 25, 23
#  20, 11, 10, 24,  4
#  14, 21, 16, 12,  6

#  14, 21, 17, 24,  4
#  10, 16, 15,  9, 19
#  18,  8, 23, 26, 20
#  22, 11, 13,  6,  5
#   2,  0, 12,  3,  7

#  https://www.geeksforgeeks.org/numpy-sum-in-python/

import numpy as np
import re
import sys

a=[]

#arr0 = [[22, 13, 17, 11,  0],   
#       [8,  2, 23,  4, 24],  
#       [21,  9, 14, 16,  7],
#	   [6, 10,  3, 18,  5],
#	   [1, 12, 20, 15, 19]]  
   
#print("\nSum of arr : ", np.sum(arr0)) 
#print("Sum of arr(axis = 0) : ", np.sum(arr0, axis = 0)) 
#print("Sum of arr(axis = 1) : ", np.sum(arr0, axis = 1))
#a.append(arr0)
#print("\nSum of arr : ", np.sum(a[0])) 
#print("Sum of arr(axis = 0) : ", np.sum(a[0], axis = 0)) 
#print("Sum of arr(axis = 1) : ", np.sum(a[0], axis = 1))
  
#print("\nSum of arr (keepdimension is True): \n",
#      np.sum(arr0, axis = 1, keepdims = True))

#print()
#print()
#arr0 = [[3, 15,  0,  2, 22],   
#       [9, 18, 13, 17,  5],  
#       [19,  8,  7, 25, 23],
#	   [20, 11, 10, 24,  4],
#	   [14, 21, 16, 12,  6]]  
   
#print("\nSum of arr : ", np.sum(arr0)) 
#print("Sum of arr(axis = 0) : ", np.sum(arr0, axis = 0)) 
#print("Sum of arr(axis = 1) : ", np.sum(arr0, axis = 1))
#a.append(arr0)
#print("\nSum of arr : ", np.sum(a[1])) 
#print("Sum of arr(axis = 0) : ", np.sum(a[1], axis = 0)) 
#print("Sum of arr(axis = 1) : ", np.sum(a[1], axis = 1))
#  
#print("\nSum of arr (keepdimension is True): \n",
#      np.sum(arr0, axis = 1, keepdims = True))

#print()
#print()
#arr0 = [[14, 21, 17, 24,  4],   
#       [10, 16, 15,  9, 19],  
#       [18,  8, 23, 26, 20],
#	   [22, 11, 13,  6,  5],
#	   [2,  0, 12,  3,  7]]  
#   
#print("\nSum of arr : ", np.sum(arr0)) 
#print("Sum of arr(axis = 0) : ", np.sum(arr0, axis = 0)) 
#print("Sum of arr(axis = 1) : ", np.sum(arr0, axis = 1))
#a.append(arr0)
#print("\nSum of arr : ", np.sum(a[2])) 
#print("Sum of arr(axis = 0) : ", np.sum(a[2], axis = 0)) 
#print("Sum of arr(axis = 1) : ", np.sum(a[2], axis = 1))
  
#print("\nSum of arr (keepdimension is True): \n",
#      np.sum(arr0, axis = 1, keepdims = True))

#print()
#print()
#print(a[0])
#print(a[1])
#print(a[2])


#let's read the test harness
#read a record

file1 = open('d04.in', 'r')
# From Puzzle5 the mcb are 001100100101, lcb are 110011011010. We must get rid of the first bit in each list

bingo=[]
#map_object=[]
diag=[]
#random=[]
count=0
arrayno=-1
rw=-1
arr0=np.zeros(shape=(5,5))
arr0.astype("float")                                       #  https://www.kite.com/python/answers/how-to-replace-a-number-in-a-numpy-array-with-nan-in-python
for line in file1:
	count+=1
	rw+=1
	diag=line.strip('\n')
	diag=diag.strip()
	diag=re.sub("\s+", ",", diag)
	a_list=diag.split(',')                                    #  https://www.kite.com/python/answers/how-to-split-a-string-into-a-list-of-integers-in-python
	map_object=map(int, a_list)
#	print("DIAG: ", diag)
	if count==1:
		random=list(map_object)
		rw=-1
		continue
	elif diag=="" and count>2:
		bingo.append(arr0)
#		print("END of ARRAY:", arr0)
		arr0=np.zeros(shape=(5,5))
		rw=-1
		arrayno+=1
		continue
	elif diag=="":
#		print("END of array", arr0)
		arr0=np.zeros(shape=(5,5))
		rw=-1
		continue
	insert_row=list(map_object)
#	print("COUNT:", count, "RW: ", rw)
#	print(insert_row)
	arr0[rw]=insert_row                                       #  https://stackoverflow.com/questions/568962/how-do-i-create-an-empty-array-matrix-in-numpy
#	print("Attempted LIST object:", insert_row)
#	print("ARR0", arr0)
#	print("BINGO ARR':", arrayno)

# A gash job as the file has no blank newline at end
bingo.append(arr0)
#print("END of ARRAY:", arr0)
	
#  Now lets iterate each bingo card and find some values
numcard=len(bingo)
filled_card=np.zeros(numcard)
print("\nNumber of cards", numcard)
#sys.exit()
for call in random:
	for card,bing in enumerate(bingo):
		print("\nCARD PRINT\n",bingo[card])                                     #  https://thispointer.com/find-the-index-of-a-value-in-numpy-array/
		result = np.where(bingo[card] == call)
#		print("\nSum of arr : ", np.sum(bingo[card])) 
#		print("Sum of arr(axis = 0) : ", np.sum(bingo[card], axis = 0)) 
#		print("Sum of arr(axis = 1) : ", np.sum(bingo[card], axis = 1))
		print("Call", call, 'Tuple of arrays returned : ', result)
		listOfCoordinates= list(zip(result[0], result[1]))            ## zip the 2 arrays to get the exact coordinates
		for cord in listOfCoordinates:                              # iterate over the list of coordinates
			print(cord)
#			if cord!="":
			bg=bingo[card]
			print("\n","TEST PRINT\n", bg)
			print(bg[cord])
			if cord!="":
				bg[cord]=np.nan
				print("\nALTERED MATRIX\n",bg)
#				print("Sum of arr(axis = 0) : ", np.nanmean(bg, axis = 0)) 
#				print("Sum of arr(axis = 1) : ", np.nanmean(bg, axis = 1))
				print("Count of arr(axis = 0) : ", np.count_nonzero(bg>=0, axis = 0)) 
				print("Count of arr(axis = 1) : ", np.count_nonzero(bg>=0, axis = 1))				
#			if np.all(np.isnan(np.sum(bingo[card], axis = 0))) or np.all(np.isnan(np.sum(bingo[card], axis = 1))):           #  https://numpy.org/doc/stable/reference/generated/numpy.isnan.html
			if np.any(np.count_nonzero(bg>=0, axis = 0)==0) or np.any(np.count_nonzero(bg>=0, axis = 1)==0):           #  https://numpy.org/doc/stable/reference/generated/numpy.isnan.html
#				sys.exit()
				filled_card[card]=1
				print(filled_card)
				print("\nFilled cards",np.count_nonzero(filled_card==1))
				print("\nFilled cards2",np.all(filled_card>=0, axis = 0))
#				if (np.count_nonzero(filled_card))==numcard:
				if np.all(filled_card>0, axis = 0):
					print("AdventOfCode 2021: Puzzle 8")
					print("\nSum of arr : ", int(np.nansum(bg)))
					print("\nCall was", call)
					print("\nMultiple is",int(np.nansum(bg)*call))
					print("\nBINGO!!!!\n")
					sys.exit()

#  Your puzzle answer was 16836.