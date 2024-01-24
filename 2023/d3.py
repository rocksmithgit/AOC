import sys
import re
import numpy as np
from collections import defaultdict, Counter, deque
from pathlib import Path
from timeit import default_timer as timer


def get_data(inputData):
    infile = sys.argv[1] if len(sys.argv) > 1 else inputData
    parsed = []
    for line in open(infile, 'r'):
        if line.strip():
            stripped = line.strip()
            stripped = stripped.replace(".", " ")
            DEBUG1 and print(f"{stripped}")
            parsed.append(stripped)
    return parsed

def checkSquare(inputData, rw, cl):
    DEBUG1 and print(f"r: {rw}, c: {cl}, InputData: {inputData}")
    currentCell = inputData[rw][cl]
    DEBUG1 and print(f"Current: {currentCell}")
    if currentCell.isdigit():
        currentRow = inputData[rw]
        newList = list(currentRow)
        newList[cl] = ' '
        newRow = ''.join(newList)
        inputData[rw] = newRow           # if it is a number, then zero it and then check either side
        if cl > 0:
            checkSquare(inputData, rw, cl-1)
        if cl < len(inputData[rw]) - 1:
            checkSquare(inputData, rw, cl+1)

def checkSquare2(inputData2, rw, cl):
    DEBUG2 and print(f"r: {rw}, c: {cl}, InputData: {inputData2}")
    currentCell = inputData2[rw][cl]
    DEBUG2 and print(f"Current: {currentCell}")
    if currentCell.isdigit():
        currentRow = inputData2[rw]
        newList = list(currentRow)
        newList[cl] = ' '
        newRow = ''.join(newList)
        inputData2[rw] = newRow           # if it is a number, then zero it and then check either side
        if cl > 0:
            checkSquare2(inputData2, rw, cl-1)
        if cl < len(inputData[rw]) - 1:
            checkSquare2(inputData2, rw, cl+1)


def part_one(inputData):
    inputData2 = inputData.copy()
    maxrows = len(inputData)
    for r in range(0, maxrows):
        maxcols = len(inputData[r])
        for c in range(0, maxcols):
            DEBUG1 and print(f"Currently checking cell [{r}][{c}]")
            if not inputData[r][c].isdigit() and inputData[r][c] != ' ':
                DEBUG1 and print(f"Found candidate {inputData[r][c]}")
                if r == 0:
                    if c == 0:                            # current is top left
                        checkSquare(inputData, r, c+1)    # right of current
                        checkSquare(inputData, r+1, c)    # down from current
                        checkSquare(inputData, r+1, c+1)  # down & right of current
                    if c == maxcols:                      # current is top right
                        checkSquare(inputData, r, c-1)    # left of current
                        checkSquare(inputData, r+1, c)    # down from current
                        checkSquare(inputData, r+1, c-1)  # down & left of current

                if r == maxrows:                          # current is bottom left
                    if c == 0:                            # current is top left
                        checkSquare(inputData, r, c+1)    # right of current
                        checkSquare(inputData, r-1, c)    # up from current
                        checkSquare(inputData, r-1, c+1)  # up & right of current
                    if c == maxcols:                      # current is bottom right
                        checkSquare(inputData, r, c-1)    # left of current
                        checkSquare(inputData, r-1, c)    # up from current
                        checkSquare(inputData, r-1, c-1)  # up & left of current

                else:
                    checkSquare(inputData, r-1, c -1)     # up & left of current
                    checkSquare(inputData, r-1, c)        # up from current
                    checkSquare(inputData, r-1, c+1)      # up & right from current
                    checkSquare(inputData, r, c+1)        # right from current
                    checkSquare(inputData, r+1, c+1)      # right & down from current
                    checkSquare(inputData, r+1, c)        # down from current
                    checkSquare(inputData, r+1, c-1)      # down & left from current
                    checkSquare(inputData, r, c-1)        # left from current
                # remove the special symbol
                currentRow = inputData[r]
                newList = list(currentRow)
                newList[c] = ' '
                newRow = ''.join(newList)
                inputData[r] = newRow
    print(inputData)
    nonPartTotal = 0
    for line in inputData:
        tokenised = line.split()
        DEBUG1 and print(f"tokenised: {tokenised}")
        for item in tokenised:
            nonPartTotal += int(item)                    # this gets us to non-part number
            DEBUG1 and print(f"non-part total: {nonPartTotal}")

    allPartTotal = 0
    for line in inputData2:
        line = re.sub(r"[^0-9 ]"," ",line)
        tokenised = line.split()
        for item in tokenised:
            allPartTotal += int(item)
            DEBUG1 and print(f"part total: {allPartTotal}")
    return allPartTotal - nonPartTotal


def part_two(inputData2):
    DEBUG2 and print(f"Part 2: {inputData2}")
    inputData2a = inputData2.copy()
    maxrows = len(inputData2)
    for r in range(0, maxrows):
        maxcols = len(inputData2[r])
        for c in range(0, maxcols):
            DEBUG2 and print(f"Currently checking cell [{r}][{c}]")
            if not inputData2[r][c].isdigit() and inputData2[r][c] == '*':
                DEBUG2 and print(f"Found candidate row{r} col {c} {inputData2[r][c]}")
                if r == 0:
                    if c == 0:                            # current is top left
                        checkSquare2(inputData2, r, c+1)    # right of current
                        checkSquare2(inputData2, r+1, c)    # down from current
                        checkSquare2(inputData2, r+1, c+1)  # down & right of current
                    if c == maxcols:                      # current is top right
                        checkSquare2(inputData2, r, c-1)    # left of current
                        checkSquare2(inputData2, r+1, c)    # down from current
                        checkSquare2(inputData2, r+1, c-1)  # down & left of current

                if r == maxrows:                          # current is bottom left
                    if c == 0:                            # current is top left
                        checkSquare2(inputData2, r, c+1)    # right of current
                        checkSquare2(inputData2, r-1, c)    # up from current
                        checkSquare2(inputData2, r-1, c+1)  # up & right of current
                    if c == maxcols:                      # current is bottom right
                        checkSquare2(inputData2, r, c-1)    # left of current
                        checkSquare2(inputData2, r-1, c)    # up from current
                        checkSquare2(inputData2, r-1, c-1)  # up & left of current

                else:
                    checkSquare2(inputData2, r-1, c -1)     # up & left of current
                    checkSquare2(inputData2, r-1, c)        # up from current
                    checkSquare2(inputData2, r-1, c+1)      # up & right from current
                    checkSquare2(inputData2, r, c+1)        # right from current
                    checkSquare2(inputData2, r+1, c+1)      # right & down from current
                    checkSquare2(inputData2, r+1, c)        # down from current
                    checkSquare2(inputData2, r+1, c-1)      # down & left from current
                    checkSquare2(inputData2, r, c-1)        # left from current
                # remove the special symbol
                currentRow = inputData2[r]
                newList = list(currentRow)
                newList[c] = ' '
                newRow = ''.join(newList)
                inputData2[r] = newRow
    print(inputData2)
    nonPartTotal = 0
    for line in inputData2:
        tokenised = line.split()
        DEBUG2 and print(f"tokenised: {tokenised}")
        for item in tokenised:
            nonPartTotal += int(item)                    # this gets us to non-part number
            DEBUG2 and print(f"non-part total: {nonPartTotal}")

    allPartTotal = 0
    for line in inputData2a:
        line = re.sub(r"[^0-9 ]"," ",line)
        tokenised = line.split()
        for item in tokenised:
            allPartTotal += int(item)
            DEBUG2 and print(f"part total: {allPartTotal}")
    return allPartTotal - nonPartTotal


PART1 = True
DEBUG1 = False
PART2 = True
DEBUG2 = True
TESTING = True

if TESTING:
    inputData = f'{Path(__file__).stem}_test.in'
else:
    inputData = f'{Path(__file__).stem}.in'

print(f"ADVENT OF CODE: {Path(__file__).stem}")

start_parse = timer()
inputList = get_data(inputData)
inputList2 = get_data(inputData)
end_parse = timer()

start_part1 = timer()
PART1 and print(f'\npart one: {part_one(inputList)}')
end_part1 = timer()
start_part2 = timer()
PART2 and print(f'part two: {part_two(inputList2)}')
end_part2 = timer()

print(f"Elapsed Parse time: {(end_parse - start_parse)*1000:.3f}ms")
print(f"Elapsed Part1 time: {(end_part1 - start_part1)*1000:.3f}ms")
print(f"Elapsed Part2 time: {(end_part2 - start_part2)*1000:.3f}ms")
print(f"Elapsed computational time: {(end_part2 - start_part1)*1000:.3f}ms")
print(f"Elapsed Total time: {((end_part2 - start_part1)+(end_parse - start_parse))*1000:.3f}ms")
