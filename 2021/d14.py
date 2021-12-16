from collections import defaultdict

state = 'TEST'
if state == 'TEST':
	poly_len = 4
	infile = open('d14.in_test', 'r')
else:
	infile = open('d14.in', 'r')
	poly_len = 21

polymer = ''
replaceable_chunks = defaultdict(list)
for line in infile:
	line = line.strip()
#	print(len(line))
	if len(line) == poly_len:
		polymer = line
	elif line:
		line = line.split(' ')
#		print(line)
#		print((line[0][0] + line[2]))
#		print((line[0][1] + line[2]))
		replaceable_chunks[line[0]].append(line[0][0] + line[2])
		
		replaceable_chunks[line[0]].append(line[2] + line[0][1])
print("POLYMER",polymer)
print(f"REPLACEABLE CHUNKS {replaceable_chunks}")
#  count the chunks before transformation
total_chunks = defaultdict(int)
working_chunks = defaultdict(int)
#                  for key in replaceable_chunks.keys():
#                   	print("KEY", key)
#                	total_chunks[key] = polymer.count(key)
#print(total_chunks)

# count the two element chinks in polymer
i = 0
while i < len(polymer) - 1:
	print("I:", i)
	this_chunk = polymer[0+i:i+2]
	print(this_chunk)
	total_chunks[this_chunk] = polymer.count(this_chunk)
	i += 1
print("INITIAL POLYMER COUNT: ", total_chunks)
#  transform
for step in range(1,10+1):
	working_chunks = total_chunks.copy()
	print(f"\nSTEP {step} ENTERING CHUNKS {total_chunks}")
	for key in replaceable_chunks.keys():
		if total_chunks[key] > 0:
			print(f"\tKEY {key} TOTAL CHUNKS {total_chunks} TOTAL OF KEY {total_chunks[key]}")
			working_chunks[key] = 0 
			print(f"\tREPLACING {key} WITH {replaceable_chunks[key][0]} {replaceable_chunks[key][1]}")
			working_chunks[replaceable_chunks[key][0]] = total_chunks[key]
			working_chunks[replaceable_chunks[key][1]] = total_chunks[key]
			print(f"\tWORKING CHUNKS {working_chunks}")
	print(f"STEP {step} EXITING CHUNKS {working_chunks}")
#	print(working_chunks)
	total_chunks = working_chunks.copy()
