#  --- Day 2: Dive! ---

#  forward X increases the horizontal position by X units.
#  down X increases the depth by X units.
#  up X decreases the depth by X units.

#  forward 5 adds 5 to your horizontal position, a total of 5.
#  down 5 adds 5 to your depth, resulting in a value of 5.
#  forward 8 adds 8 to your horizontal position, a total of 13.
#  up 3 decreases your depth by 3, resulting in a value of 2.
#  down 8 adds 8 to your depth, resulting in a value of 10.
#  forward 2 adds 2 to your horizontal position, a total of 15.
#  After following these instructions, you would have a horizontal position of 15 and a depth of 10. (Multiplying these together produces 150.)

#  Calculate the horizontal position and depth you would have after following the planned course. What do you get if you multiply your final horizontal position by your final depth?

#init vars
depth=0
forwards=0
multiple=0
#read a record
file1 = open('d02.in', 'r')

for line in file1:
	direction=line.split()
#	print(direction[0], direction[1])
	
	match direction[0]:
		case "forward":
			forwards=forwards+float(direction[1].strip())
#			print("FORWARD", direction[0],": ", direction[1])
		case "up":
			depth=depth-float(direction[1].strip())
#			print("UP", direction[0],": ", direction[1])
		case "down":
			depth=depth+float(direction[1].strip())
#			print("DOWN", direction[0],": ", direction[1])

multiple=forwards*depth

print()
print("AdventOfCode 2021: Puzzle 3")
print("HORIZONTAL: ", forwards, "DEPTH: ", depth, "MULIPLE: ", multiple)

file1.close()

# Your puzzle answer was 2117664.
