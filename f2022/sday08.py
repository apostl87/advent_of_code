import re
from collections import defaultdict

test_input = False
if test_input:
   input_file = "day08test.txt"
else:
    input_file = "day08.txt"

with open(input_file, "r") as f:
    puzzle_input = f.read().strip()

def part1(puzzle_input):
    grid = [[int(x) for x in line] for line in puzzle_input.split("\n")]

    visible = set()
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            height = grid[x][y]
            if all([grid[t][y] < height for t in range(x)]) or \
                all([grid[x][t] < height for t in range(y)]):
                visible.add((x, y))
                continue
            if all([grid[t][y] < height for t in range(x+1, len(grid))]):
                visible.add((x, y))
                continue
            if all([grid[x][t] < height for t in range(y+1, len(grid[0]))]):
                visible.add((x, y))
                continue

    return(len(visible))


def part2(puzzle_input):
    grid = [[int(x) for x in line] for line in puzzle_input.split("\n")]

    scenic_score = []

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            r = l = d = u = 0 # right left down up
            height = grid[x][y]
            for x_ in range(x-1, -1, -1):
                u += 1 
                if grid[x_][y] >= height:
                    break
            for x_ in range(x+1, len(grid)):
                d += 1 
                if grid[x_][y] >= height:
                    break
            for y_ in range(y-1, -1, -1):
                l += 1 
                if grid[x][y_] >= height:
                    break
            for y_ in range(y+1, len(grid[0])):
                r += 1 
                if grid[x][y_] >= height:
                    break
    
            scenic_score.append(l*r*d*u)

    return max(scenic_score)

print("Part 1:", part1(puzzle_input))
print("Part 2:", part2(puzzle_input))

