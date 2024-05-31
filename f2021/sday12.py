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

connections = [line.split("-") for line in input_.splitlines()]

caves, smalls = set(), set()
neighbors = defaultdict(set)

for c1, c2 in connections:
    neighbors[c1].add(c2)
    neighbors[c2].add(c1)
    caves.add(c1)
    caves.add(c2)

for c in caves:
    if c == str.lower(c):
        smalls.add(c)

counter = 0
queue = [('start', set(), False)]
while queue:
    cave, excluded_ = queue.pop(0)
    if cave == 'end':
        counter += 1
        continue
    if cave in smalls:
        excluded_.add(cave)
    for n in neighbors[cave]:
        if n not in excluded_:
            queue.append((n, excluded_.copy()))
print(counter, "paths")

counter = 0
queue = [('start', set(), False)]
while queue:
    cave, excluded_, doublevisit = queue.pop(0)
    if cave == 'end':
        counter += 1
        continue
    if cave in smalls:
        excluded_.add(cave)
    for n in neighbors[cave]:
        if n not in excluded_:
            queue.append((n, excluded_.copy(), doublevisit))
        elif n != 'start' and not doublevisit:
            queue.append((n, excluded_.copy(), True))
print(counter, "paths")