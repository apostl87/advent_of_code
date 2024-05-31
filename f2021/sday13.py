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

dotsinput, foldsinput = input_.split("\n\n")
dots = []

for line in dotsinput.splitlines():
    (x, y) = line.split(',') 
    (x, y) = int(x), int(y)
    dots.append([x, y])

# Part 1
for fold in foldsinput.splitlines():
    axis, pos = fold[fold.find('=')-1], int(fold[fold.find('=')+1:])
    for i, (x, y) in enumerate(dots):
        if axis == 'y':
            if y > pos:
                dots[i][1] = 2*pos - y
        else:
            if x > pos:
                dots[i][0] = 2*pos - x
    break
dots_unique = set()
for dot in dots:
    dots_unique.add(tuple(dot))
print(len(dots_unique))


# Part 2
for fold in foldsinput.splitlines():
    axis, pos = fold[fold.find('=')-1], int(fold[fold.find('=')+1:])
    for i, (x, y) in enumerate(dots):
        if axis == 'y':
            if y > pos:
                dots[i][1] = 2*pos - y
        else:
            if x > pos:
                dots[i][0] = 2*pos - x
    print("Fold complete.")
dots_unique = set()
for dot in dots:
    dots_unique.add(tuple(dot))
print(len(dots_unique))

def print_dots(dots):
    xmax = max([x for x, y in dots])
    ymax = max([y for x, y in dots])
    output = ''
    for i in range(ymax + 1):
        for j in range(xmax + 1):
            output += '.' if not any([x == j and y == i for x, y in dots]) else '#'
        output += '\n'
    print(output)

print_dots(dots_unique)