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

grid = [list(line) for line in input_.splitlines()]
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

lowpoints, risk_level = [], 0
for y in range(len(grid)):
    for x in range(len(grid[0])):
        neighbors = [(y + d[0], x + d[1]) for d in directions if 0 <= y + d[0] <= len(grid)-1 and 0 <= x + d[1] <= len(grid[0])-1]
        if all([grid[ny][nx] > grid[y][x] for ny, nx in neighbors]):
            lowpoints.append((y, x))
            risk_level += 1 + int(grid[y][x])
print(risk_level)

def compute_basin(points, basin):
    new_points = set()
    for y, x in points:
        neighbors = [(y + d[0], x + d[1]) for d in directions if 0 <= y + d[0] <= len(grid)-1 and 0 <= x + d[1] <= len(grid[0])-1]
        for yn, xn in neighbors:
            if (yn, xn) not in new_points and (yn, xn) not in basin:
                if grid[yn][xn] < '9':
                    new_points.add((yn, xn))
    recursion = False
    for y, x in new_points:
        basin.add((y, x))
        recursion = True
    if recursion:
        return compute_basin(new_points, basin)
    else:
        return basin

result = np.prod(sorted([len(compute_basin({(y, x)}, set())) for y, x in lowpoints])[-3:])
print(result)
