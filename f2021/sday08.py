import sys, numpy as np, re
from aoclib import *
from collections import defaultdict

if "--test" in sys.argv or "-t" in sys.argv:
    test = True
else:
    test = False

input_file = (sys.argv[0].split(".")[0][1:])
input_file += "test.txt" if test==True else ".txt"
with open(input_file, "r") as f:
    input_ = f.read().strip()

lines = input_.splitlines()
if test:
    lines_new = []
    for i in range(len(lines)//2):
        lines_new.append(lines[i*2] + lines[i*2+1])
    lines = lines_new

# Part 1
result = 0
for line in lines:
    digits = line.split('|')[-1].strip().split()
    result += sum([1 if len(x) in [2, 3, 4, 7] else 0 for x in digits])
print(result)

# Part 2
unique_lengths = {2: 1, 3: 7, 4: 4, 7: 8}
result = 0
for line in lines:
    patterns, digits = [x.split() for x in line.split('|')]

    patterns_ordered = ['']*10

    fives = []
    sixes = []
    for p in patterns:
        if len(p) in unique_lengths:
            patterns_ordered[unique_lengths[len(p)]] = set(p)
        elif len(p) == 5:
            fives.append(set(p))
        elif len(p) == 6:
            sixes.append(set(p))
    for f in fives:
        if patterns_ordered[1] < f:
            patterns_ordered[3] = f
        elif len(patterns_ordered[4].difference(f)) == 1:
            patterns_ordered[5] = f
        else:
            patterns_ordered[2] = f
    for s in sixes:
        if len(s.union(patterns_ordered[3])) == 6:
            patterns_ordered[9] = s
        elif s > patterns_ordered[1]:
            patterns_ordered[0] = s
        else:
            patterns_ordered[6] = s

    print(patterns_ordered)

    digits_decoded = ''
    for digit in digits:
        digits_decoded += str(patterns_ordered.index(set(digit)))
    result += int(digits_decoded)

print(result)