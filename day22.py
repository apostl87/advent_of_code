import re
import numpy as np
import copy

input_file = './day22_input.txt'

with open(input_file, "r") as f:
    puzzle_input = f.read()

### Part 1
snapshot = re.findall(r'([^~]*)~([^~]*)\n', puzzle_input)

bricks = []
for i, (start, end) in enumerate(snapshot):
    x1, y1, z1 = map(int, start.split(","))
    x2, y2, z2 = map(int, end.split(","))
    x1, x2 = sorted((x1, x2))
    y1, y2 = sorted((y1, y2))
    z1, z2 = sorted((z1, z2))
    bricks.append((x1, x2, y1, y2, z1, z2))

xmax = max([b[1] for b in bricks]) + 1
ymax = max([b[3] for b in bricks]) + 1
zmax = max([b[5] for b in bricks]) + 1

bricks.sort(key=lambda x: x[4])

stack = [[[None for _ in range(xmax)] for _ in range(ymax)] for _ in range(zmax)]

supports_of = {}
for i, (x1, x2, y1, y2, z1, z2) in enumerate(bricks):
    support = set()
    for z in range(zmax):
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                if stack[z][y][x] is not None: support.add(stack[z][y][x])
        if support:
            break
    supports_of[i] = support

    height = z2-z1+1
    if i==0: z+=1
    for z_ in range(z-height, z):
        for y in range(y1, y2+1):
            for x in range(x1, x2+1):
                stack[z_][y][x] = i

indispensible = set()
for s in supports_of.values():
    if len(s)==1:
        for s_ in s:
            indispensible.add(s_)

print("Part 1:",len(bricks)-len(indispensible))


### Part 2
total = 0
for i in indispensible:
    removed = set([i])

    for key in supports_of:
        #print(i,key)
        #print(supports_of[key])
        support = supports_of[key]
        fall = len(support)>0 and all([s in removed for s in support])
        if fall:
                removed.add(key)
                #print(removed)         
    total += len(removed)-1
print("Part 2:", total)

