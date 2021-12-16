import sys

infile = open('d13.in', 'r')


dots = {}
did_p1 = False
count = 0
for line in infile:
	line = line.strip()
	if line and line.startswith('fold'):
		count += 1
		dots2 = {}
#		instruct = line.split()[-1]              # split at last ' '
		dir, axis = line.split()[-1].split('=')
		axis = int(axis)
		if dir == 'x':
			for (x,y) in dots:
				if x < axis:
					dots2[(x,y)] = True
				else:
					dots2[(axis-(x-axis),y)] = True
		elif dir == 'y':
			for (x,y) in dots:
				if y < axis:
					dots2[(x,y)] = True
				else:
					dots2[(x, axis-(y-axis))] = True
		else:
			sys.exit("Error in input")
		dots = dots2
		if count == 1:
			print(f"Number of dots after fold {count}: {len(dots2)}")
	elif line:
		x,y = [int(v) for v in line.strip().split(',')]
		dots[(x,y)] = True
#print(dots)

X = max([x for x,y in dots.keys()])
Y = max([y for x,y in dots.keys()])

#print(dots)
wrd =''
for y in range(Y+1):
	for x in range(X+1):
			wrd += ('#' if (x,y) in dots else ' ')
	print(wrd)
	wrd = ''


wrd =''
for y in range(Y+1):
	for x in range(X+1):
		if (x,y) in dots:
			wrd += '*'
		else:
			wrd += ' '
	print(wrd)
	wrd = ''
