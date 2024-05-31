import re
from collections import deque
from itertools import count
import math

input_file = 'day21_input.txt'

with open(input_file, "r") as f:
    puzzle_input = f.read().strip()

directions = ((1, 0), (-1, 0), (0, 1), (0, -1))


### Part 1
grid = puzzle_input.split("\n")
m, n = len(grid), len(grid[0])

# Init
possibles = set()
for i, line in enumerate(grid):
    j = line.find('S')
    if j > -1:
        grid[i] = grid[i].replace('S', '.')
        possibles.add((i, j))
        break

# display_grid = ""
# for x in grid:
#     display_grid += x + "\n"
# print(display_grid)

# Simulation
for step in range(64):
    possibles_new = set()
    for x, y in possibles:
        for dx, dy in directions:
            new_x, new_y = x+dx, y+dy
            if new_x >= 0 and new_y >= 0 and \
            new_x < len(grid) and new_y < len(grid[0]) and \
            grid[new_x][new_y] == '.':
                possibles_new.add((new_x, new_y))
    possibles = possibles_new

# Output
print("Part 1:",len(possibles))