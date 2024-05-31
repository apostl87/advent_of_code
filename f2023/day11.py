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

## Part 2
with open("day11_input.txt", "r") as f:
    puzzle_input = f.read()

lines = puzzle_input.split()

universe = np.array([list(line) for line in lines])
m, n = universe.shape # former shape

# Expanding space
col_ids, row_ids = [], []
for k in range(m):
    if all(universe[k, :]=='.'):
        row_ids.append(k)
for k in range(n):
    if all(universe[:, k]=='.'):
        col_ids.append(k)

galaxy_positions_original = [(x, y) for x in range(m) for y in range(n) if universe[x, y]=='#']

galaxy_positions_expanded = []
for xy_original in galaxy_positions_original:
    x_new = xy_original[0] + len([True for x in row_ids if x < xy_original[0]])*999999
    y_new = xy_original[1] + len([True for y in col_ids if y < xy_original[1]])*999999
    galaxy_positions_expanded.append((x_new, y_new))

#print(universe)
#print(galaxy_positions_expanded)
galaxy_pairs = combinations(galaxy_positions_expanded, 2)

total = 0
for pair in galaxy_pairs:
    #print(pair)
    distance = abs(pair[0][0]-pair[1][0]) + abs(pair[0][1]-pair[1][1])
    total += int(distance)

#print(universe)
print("Total distance: ", total)




input_file = 'day11_input.txt'

# To match the format of input files for the Basilisk.
q = { 11: open(input_file).read() }


galaxies = [(x, y) for y, row in enumerate(q[11].strip().split()) for x, col in enumerate(row) if col == '#']

max_x = max(galaxies, key=lambda x: x[0])[0]
max_y = max(galaxies, key=lambda x: x[1])[1]

empty_rows = [y for y in range(max_y+1) if not any([y == g[1] for g in galaxies])]
empty_cols = [x for x in range(max_x+1) if not any([x == g[0] for g in galaxies])]

galaxies = [(g[0] + (len([x for x in empty_cols if x < g[0]]) * 999999), g[1] + (len([y for y in empty_rows if y < g[1]]) * 999999)) for g in galaxies]

shortest_paths = {}
for g1 in galaxies:
    for g2 in galaxies:
        if g1 != g2 and (g2, g1) not in shortest_paths:
            shortest_paths[(g1, g2)] = abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])
print('Day 11 Part 2:',sum(shortest_paths.values()))