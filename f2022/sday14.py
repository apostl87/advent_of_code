import re
from collections import defaultdict
import copy
from functools import cmp_to_key

test_input = False
if test_input:
    input_file = "day14test.txt"
else:
    input_file = "day14.txt"

with open(input_file, "r") as f:
    puzzle_input = f.read().strip()

def list2string(lst):
    result = ''
    for row in lst:
        for col in row:
            result += col
        result += '\n'
    return result

#def part1(puzzle_input):
lines = [[[int(x) for x in coords.split(",")] for coords in line.split(" -> ")] for line in puzzle_input.split("\n")]
# print(lines)
min_x = min(min([coords[0] for coords in line]) for line in lines)
max_x = max(max([coords[0] for coords in line]) for line in lines)
# print(max_x)
max_y = max(max([coords[1] for coords in line]) for line in lines)
# print(min_x)

grid = [['.' for x in range(max_x-min_x+1)] for y in range(max_y+1)]

for line in lines:
    for i in range(len(line)-1):
        x1, y1 = line[i]
        x2, y2 = line[i+1]
        if x1 == x2:
            for y in range(min(y1,y2), max(y1,y2)+1):
                grid[y][x1-min_x] = '#'
        else:
            for x in range(min(x1,x2)-min_x, max(x1,x2)+1-min_x):
                grid[y1][x] = '#'

void = False
counter = 0
while not void:
    x, y = 500-min_x, 0
    stopped = False
    while not stopped:
        if y+1 > max_y:
            void = True
            break
        elif grid[y+1][x] == '.':
            y += 1
        elif x-1 < 0:
            void = True
            break
        elif grid[y+1][x-1] == '.':
            y += 1
            x -= 1
        elif x+1 > max_x-min_x:
            void = True
            break
        elif grid[y+1][x+1] == '.':
            y += 1
            x += 1
        else:
            stopped = True
            grid[y][x] = 'o'
            counter += 1
 
print(list2string(grid))
print(counter)

### Part 2
#def part1(puzzle_input):
lines = [[[int(x) for x in coords.split(",")] for coords in line.split(" -> ")] for line in puzzle_input.split("\n")]
# print(lines)
min_x = min(min([coords[0] for coords in line]) for line in lines)
max_x = max(max([coords[0] for coords in line]) for line in lines)
# print(max_x)
max_y = max(max([coords[1] for coords in line]) for line in lines)
# print(min_x)

grid = [['.' for x in range(max_x-min_x+1001)] for y in range(max_y+3)]
min_x -= 500
max_x += 500
max_y += 2

for line in lines:
    for i in range(len(line)-1):
        x1, y1 = line[i]
        x2, y2 = line[i+1]
        #x1 += 2
        #x2 += 2
        if x1 == x2:
            for y in range(min(y1,y2), max(y1,y2)+1):
                grid[y][x1-min_x] = '#'
        else:
            for x in range(min(x1,x2)-min_x, max(x1,x2)+1-min_x):
                grid[y1][x] = '#'
for x in range(len(grid[0])):
    grid[-1][x] = '#'

void = False
counter = 0
while not void:
    x, y = 500-min_x, 0
    stopped = False
    while not stopped:
        if grid[y+1][x] == '.':
            y += 1
        elif grid[y+1][x-1] == '.':
            y += 1
            x -= 1
        elif grid[y+1][x+1] == '.':
            y += 1
            x += 1
        else:
            stopped = True
            grid[y][x] = 'o'
            counter += 1
            if y==0 and x==500-min_x:
                void=True
                break
 
#print(list2string(grid))
print(counter)
