import re
import numpy as np
from itertools import combinations

with open("day11_input.txt", "r") as f:
    puzzle_input = f.read()

#def part1(puzzle_input):
lines = puzzle_input.split()

universe = np.array([list(line) for line in lines])
m, n = universe.shape # former shape

# Expanding space
col_ids, row_ids = [], []
for k in range(m):
    if all(universe[k, :]=='.'):
        row_ids.append(k)
for i, row_id in enumerate(row_ids):
    universe = np.insert(universe, i+row_id, np.array(['.']*universe.shape[1]), axis=0)
for k in range(n):
    if all(universe[:, k]=='.'):
        col_ids.append(k)
for i, col_id in enumerate(col_ids):
    universe = np.insert(universe, i+col_id, np.array(['.']*universe.shape[0]), axis=1)
    #ap = np.where(sketch=='S') # animal position

m, n = universe.shape # new shape
galaxy_positions = [(x, y) for x in range(m) for y in range(n) if universe[x, y]=='#']

galaxy_pairs = combinations(galaxy_positions, 2)

total = 0
for pair in galaxy_pairs:
    #print(pair)
    distance = abs(pair[0][0]-pair[1][0]) + abs(pair[0][1]-pair[1][1])
    total += distance

#print(universe)
print("Total distance: ", total)

#print(part1(puzzle_input))

def part2(puzzle_input):
    pass

print(part2(puzzle_input))