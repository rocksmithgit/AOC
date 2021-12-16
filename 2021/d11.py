def flood_fill(x ,y):
    # we need the x and y of the start position
    # the flood fill has 4 parts
    # firstly, make sure the x and y are inbounds
	if x < 0 or x >= len(field[0]) or y < 0 or y >= len(field):
		return
	# secondly make sure we want to fill
	if flash[y,x] == 1:
		return
    
    # thirdly, set the current position to the new value
	field[y,x] += 1
	if field[y, x] == 10:
		field[y, x] = 0
		flash[y, x] = 1
		total[0] += 1
    # fourthly, attempt to fill the neighboring positions
		flood_fill(x+1, y)
		flood_fill(x-1, y)
		flood_fill(x, y+1)
		flood_fill(x, y-1)
		flood_fill(x+1, y+1)
		flood_fill(x-1, y+1)
		flood_fill(x-1, y-1)
		flood_fill(x+1, y-1)
	
	
def file_input(file):
	r = 0
	for line in file1:
		for c, digit in enumerate(line.strip().strip('\n')):
			field[r,c] = int(digit)
		r += 1

	
import numpy as np
import sys

field = np.zeros(shape=(10,10))
flash = np.zeros(shape=(10,10))
total =[0]
file1 = open('d11.in', 'r')
file_input(file1)
abort = 0
for step in range(1,2000):
	flash = np.zeros(shape=(10,10))
	for r in range(10):
		for c in range(10):
			flood_fill(c, r)
			if np.sum(flash) == 100:
				abort = 1
				print(f"SYNCHRO FLASH after step: {step}")
#				sys.exit()
			if abort == 1:
				break
		if abort == 1:
			break
	if abort == 1:
		break
	if step == 100:
		print(f"After step {step} FLASHES are {total[0]}")


#  Your puzzle answer was 1793.
#  Your puzzle answer was 247.