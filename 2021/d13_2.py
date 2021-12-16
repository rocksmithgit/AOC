import sys
import numpy as np
from collections import defaultdict, Counter, deque


def get_data(infile):
    trans = []
#    infile = sys.argv[1] if len(sys.argv) > 1 else 'd13.in'
    c_max = 0
    r_max = 0
    state = 0
    for line in open(infile, 'r'):
        tmp = []
        I = []
#        print(line)
        if line == '\n':
            state = 1
            continue
        match state:
            case 0:
#            if '=' not in line:
                c, r = line.split(',')
                c = int(c)
                r = int(r)
                if c > c_max:
                    c_max = c
                if r > r_max:
                    r_max = r
                tmp.append(int(c))
                tmp.append(int(r))
                L.append(tmp)
            case _:
                ins = line.split('=')
                instr = str(ins[0])
                instr = instr[-1]
                val = int(ins[1])
                I.append(instr)
                I.append(val)
                folds.append(I)
#    print(folds)


    trans = np.zeros(shape=(r_max+1, c_max+1))
    return trans, r_max, c_max, folds


def fill_tranparency(trans, L):
    for cell in L:
#        print(L)
#        print(cell)
        r = cell[0]
        c = cell[1]
        trans[c,r] = 1
 #       print(f"c {c} r {r} {trans[c,r]}")


def horiz_fold(trans, axis):
    c_max = len(trans[0])
    r_max = len(trans)
    for row in range(0, r_max-axis):
        for col in range(0, c_max):
            trans[axis-row, col] += trans[axis+row, col]
            if trans[axis-row, col] > 1:
                trans[axis - row, col] = 1
    trans = np.delete(trans, slice(axis+1, r_max), 0)
    return trans

def vert_fold(trans, axis):
    c_max = len(trans[0])
    r_max = len(trans)
#    print(f"c_max {c_max}, r_max {r_max}")
    for col in range(0, c_max-axis):
        for row in range(0, r_max):
            trans[row, axis-col] += trans[row, axis+col]
            if trans[row, axis-col] > 1:
                trans[row, axis - col] = 1
    trans = np.delete(trans, slice(axis+1, c_max), 1)
    return trans


f = 'TESTING'
f = 'PROD'
if f != 'TESTING':
    infile = sys.argv[1] if len(sys.argv) > 1 else 'd13.in'
else:
    infile = 'tmpo'

trans = []
L =[]
folds = []
trans, r_max, c_max, folds = get_data(infile)
fill_tranparency(trans, L)
#print(trans)
#print(folds)

# now to start folding....
count = 0
for f in folds:
    count += 1
    if f[0] == 'x':
        trans = vert_fold(trans, f[1])
#        print(trans)
    else:
        trans = horiz_fold(trans, f[1])
#        print(trans)
    if count ==1:
        a = np.sum(trans)
        print(f"\nTotal dots: {a}")
#trans = horiz_fold(trans, 7)
#print("\n",trans)
#trans = vert_fold(trans, 5)
#print("\n",trans)


