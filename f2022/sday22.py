import re
from collections import defaultdict
import copy
from functools import cmp_to_key

test_input = False
if test_input:
    input_file = "day22test.txt"
else:
    input_file = "day22.txt"

with open(input_file, "r") as f:
    puzzle_input = f.read()

def list2string(lst):
    result = ''
    for row in lst:
        for col in row:
            result += col
        result += '\n'
    return result

def string2list(str_):
    result = str_.split("\n")
    for r in result:
        result[result.index(r)] = list(r)
    return result

def next_instruction(main_idx, d, ins_turns, ins_lengths):
    if main_idx == len(ins_turns)-1:
        return None, d, None
    main_idx += 1
    d = directions[(directions.index(d) + 1) % 4] if ins_turns[main_idx]=='R' else directions[directions.index(d) - 1]
    steps_to_go = ins_lengths[main_idx]
    return main_idx, d, steps_to_go

#def part1(puzzle_input):
grid, instructions = puzzle_input.split("\n\n")

grid = string2list(grid)
m, n = len(grid), max(len(line) for line in grid)
for line in grid:
    while len(line) < n:
        line.append(' ')

ins_lengths = [int(x) for x in re.findall(r'(\d+)', instructions)]
ins_turns = ['R'] + re.findall(r'([RL])', instructions)

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

x, y = 0, [k == '.' for k in grid[0]].index(True) # start coordinates
main_idx = 0
d = directions[0] # to the right
steps_to_go = ins_lengths[main_idx]

while True:
    print(main_idx, steps_to_go, x, y, d)
    if main_idx is None or main_idx > len(ins_turns)-1:
        break
    if steps_to_go == 0:
        main_idx, d, steps_to_go = next_instruction(main_idx, d, ins_turns, ins_lengths)
        continue
    x_new = x + d[0]
    y_new = y + d[1]
    g = grid[x_new%m][y_new%n]
    if g == '#':
        main_idx, d, steps_to_go = next_instruction(main_idx, d, ins_turns, ins_lengths)
        continue
    elif g == ' ':
        if d == (0, 1):
            for y_new in range(n):
                g = grid[x_new][y_new]
                if g == ' ':
                    continue
                elif g == '#':
                    main_idx, d, steps_to_go = next_instruction(main_idx, d, ins_turns, ins_lengths)
                    break
                else:
                    steps_to_go -= 1
                    x, y = x_new, y_new
                    break
        elif d == (1, 0):
            for x_new in range(m):
                g = grid[x_new][y_new]
                if g == ' ':
                    continue
                elif g == '#':
                    main_idx, d, steps_to_go = next_instruction(main_idx, d, ins_turns, ins_lengths)
                    break
                else:
                    steps_to_go -= 1
                    x, y = x_new, y_new
                    break
        elif d == (0, -1):
            for y_new in range(n-1, -1, -1):
                g = grid[x_new][y_new]
                if g == ' ':
                    continue
                elif g == '#':
                    main_idx, d, steps_to_go = next_instruction(main_idx, d, ins_turns, ins_lengths)
                    break
                else:
                    steps_to_go -= 1
                    x, y = x_new, y_new
                    break
        else:
            for x_new in range(m-1, -1, -1):
                print(m)
                print(x_new)
                g = grid[x_new][y_new]
                if g == ' ':
                    continue
                elif g == '#':
                    main_idx, d, steps_to_go = next_instruction(main_idx, d, ins_turns, ins_lengths)
                    break
                else:
                    steps_to_go -= 1
                    x, y = x_new, y_new
                    break
    else:
        steps_to_go -= 1
        x, y = x_new, y_new

print(x, y, d)
print((x+1)*1000 + (y+1)*4 + directions.index(d))

