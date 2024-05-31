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
#print(grid)
grid = np.array(grid).astype(int)
directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

def time_evolve(grid, steps):
    counter = 0
    synchronized_at = None
    for i in range(steps):
        stepcounter = counter
        grid += 1
        while np.any(grid > 9):
            flashingyy, flashingxx = np.nonzero(grid > 9)
            for y, x in zip(flashingyy, flashingxx):
                neighbors = np.array([(y + d[0], x + d[1]) for d in directions if 0 <= y + d[0] <= len(grid)-1 and 0 <= x + d[1] <= len(grid[0])-1])
                grid[neighbors[:, 0], neighbors[:, 1]] += 1
                grid[y, x] = -1e9
                counter += 1
        grid[grid < 0] = 0
        if counter == stepcounter + 100:
            synchronized_at = i + 1
            break
    return grid, counter, synchronized_at

print(time_evolve(grid, 100))

grid = [list(line) for line in input_.splitlines()]
grid = np.array(grid).astype(int)

print(time_evolve(grid, 1000))
