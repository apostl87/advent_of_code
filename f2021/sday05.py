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
# Part 1
points = defaultdict(int)
for line in lines:
    x1, y1, x2, y2 = re.findall(r'(\d+)', line)
    if x1 == x2:
        for y in range(min(int(y1), int(y2)), max(int(y1), int(y2)) + 1):
            points[str(x1)+', '+str(y)] += 1
    if y1 == y2:
        for x in range(min(int(x1), int(x2)), max(int(x1), int(x2)) + 1):
            points[str(x)+', '+str(y1)] += 1
print(len(points)-list(points.values()).count(1))

# Part 2
points = defaultdict(int)
for line in lines:
    x1, y1, x2, y2 = [int(x) for x in re.findall(r'(\d+)', line)]
    if x1 == x2:
        for y in range(min(int(y1), int(y2)), max(int(y1), int(y2)) + 1):
            points[(x1, y)] += 1
    if y1 == y2:
        for x in range(min(int(x1), int(x2)), max(int(x1), int(x2)) + 1):
            points[(x, y1)] += 1
    if abs(x1-x2) == abs(y1-y2):
        for i in range(abs(x1-x2)+1):
            x = x1 + i*np.sign(x2-x1)
            y = y1 + i*np.sign(y2-y1)
            #print(x, y)
            points[(x, y)] += 1
print(len(points)-list(points.values()).count(1))