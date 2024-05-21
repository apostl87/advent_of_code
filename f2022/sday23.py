import re
from collections import defaultdict
import copy
from functools import cmp_to_key

test_input = False
if test_input:
    input_file = "day23test.txt"
else:
    input_file = "day23.txt"

with open(input_file, "r") as f:
    puzzle_input = f.read().strip()

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

def get_elongation(elves):
    xmin = ymin = +1e9
    xmax = ymax = -1e9
    for elf in elves:
        xmin = min(xmin, elf.real)
        xmax = max(xmax, elf.real)
        ymin = min(ymin, elf.imag)
        ymax = max(ymax, elf.imag)
    return int(xmin), int(xmax), int(ymin), int(ymax)

def make_grid(elves):
    xmin, xmax, ymin, ymax = get_elongation(elves)
    line = ['.']*(xmax - xmin +1)
    grid = []
    for _ in range(ymax - ymin + 1):
        grid.append(copy.copy(line))
    for elf in elves:
        x, y = int(elf.real - xmin), int(elf.imag - ymin)
        grid[y][x] = '#'

    return list2string(grid)

# def part1(puzzle_input):
lines = puzzle_input.split("\n")
elves = [complex(x, y) for y, line in enumerate(lines) for x, c in enumerate(line) if c == '#']

look_dirs_char = {'N': -1j, 'S': 1j, 'W': -1, 'E': 1}
dirs = [-1-1j, 0-1j, 1-1j, -1, 1, -1+1j, 0+1j, 1+1j]

def look_around(order_look_dirs, neighbors_at):
    for look_dir in order_look_dirs:        
        if look_dir in ['N', 'S']:
            logic = any(n.imag==look_dirs_char[look_dir].imag for n in neighbors_at)
        if look_dir in ['W', 'E']:
            logic = any(n.real==look_dirs_char[look_dir].real for n in neighbors_at)
        if not logic:
            return look_dirs_char[look_dir]
    return False

for round in range(10000):
    elves_set = set(elves)

    print("Round", round)
    proposed_pos = defaultdict(complex)
    for i, elf in enumerate(elves):
        neighbors_at = []

        for d in dirs:
            if elf + d in elves_set:
                #print(d)
                neighbors_at.append(d)

        if len(neighbors_at) == 0:
            continue

        first_look_dir = round%4
        order_look_dirs = [list(look_dirs_char.keys())[x%4] for x in range(round, round+4)]

        proposed_dir = look_around(order_look_dirs, neighbors_at)
        
        if proposed_dir:
            proposed_pos[i] = elf + proposed_dir

    #print(proposed_pos)
    candidates = list(proposed_pos.keys())
    if len(candidates) == 0:
        break

    while candidates:
        i = candidates.pop(0)
        move_i = True
        for j in candidates:
            if proposed_pos[i] == proposed_pos[j]:
                candidates.remove(j)
                move_i = False
        if move_i:
            elves[i] = proposed_pos[i]
        
    if round == 4:
        grid = make_grid(elves)
        print(grid)
        print("Part 1: ", grid.count('.'))

print("Part 2:", round+1)

