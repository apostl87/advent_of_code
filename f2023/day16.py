import copy
import numpy as np
from itertools import product

input_file = 'day16_input.txt'

with open(input_file, "r") as f:
    puzzle_input = f.read().strip()


def propagate_beam(beam, tile):
    new_beam = None
    if beam[-1] == 'r':
        if tile in '.-': beam[1] += 1
        if tile == '\\':
            beam[0] += 1
            beam[2] = 'd'
        if tile == '|':
            new_beam = copy.copy(beam)
            new_beam[0] -= 1
            new_beam[2] = 'u'
            beam[0] += 1
            beam[2] = 'd'
        if tile == '/':
            beam[0] -= 1
            beam[2] = 'u'
    elif beam[-1] == 'l':
        if tile in '.-': beam[1] -= 1
        if tile == '\\':
            beam[0] -= 1
            beam[2] = 'u'
        if tile == '|':
            new_beam = copy.copy(beam)
            new_beam[0] -= 1
            new_beam[2] = 'u'
            beam[0] += 1
            beam[2] = 'd'
        if tile == '/':
            beam[0] += 1
            beam[2] = 'd'
    elif beam[-1] == 'd':
        if tile in '.|': beam[0] += 1
        if tile == '\\':
            beam[1] += 1
            beam[2] = 'r'
        if tile == '-':
            new_beam = copy.copy(beam)
            new_beam[1] -= 1
            new_beam[2] = 'l'
            beam[1] += 1
            beam[2] = 'r'
        if tile == '/':
            beam[1] -= 1
            beam[2] = 'l'
    elif beam[-1] == 'u':
        if tile in '.|': beam[0] -= 1
        if tile == '\\':
            beam[1] -= 1
            beam[2] = 'l'
        if tile == '-':
            new_beam = copy.copy(beam)
            new_beam[1] -= 1
            new_beam[2] = 'l'
            beam[1] += 1
            beam[2] = 'r'
        if tile == '/':
            beam[1] += 1
            beam[2] = 'r'
    return [beam, new_beam]

def position_is_valid(beam, grid):
    if beam[0] >= len(grid) or beam[1] >= len(grid[0]) or beam[0]<0 or beam[1]<0:
        return False
    return True

def list2string(lst):
    result = ''
    for row in lst:
        for col in row:
            result += col
        result += '\n'
    return result

## Part 1
grid = puzzle_input.split("\n")

energy_grid = np.array([['.']*len(grid[0])]*len(grid))
visited_states = set()

beams = []
beams.append([0,0,'r'])

while beams:
    beam = beams.pop()
    x, y, direction = beam
    energy_grid[x][y] = '#'

    if tuple(beam) not in visited_states:
        suggested_beams = propagate_beam(copy.copy(beam), grid[x][y])
        #print(suggested_beams)
        for sb in suggested_beams:
            if sb and position_is_valid(sb, grid):
                beams.append(sb)

    #print(beam)
    visited_states.add(tuple(beam))

#print(list2string(energy_grid))
print(list2string(energy_grid).count('#'))

## Part 2
grid = puzzle_input.split("\n")

start_beams = []
energy = []

for k in range(1, len(grid[0])-1):
    start_beams.append([0, k, 'd'])
    start_beams.append([len(grid)-1, k, 'u'])
for k in range(1, len(grid)-1):
    start_beams.append([k, 0, 'r'])
    start_beams.append([k, len(grid[0])-1, 'l'])
p = product((0, len(grid)-1),(0, len(grid[0])-1))
while pos:=next(p, False):
    if pos[0] == 0: dir1 = 'd'
    else: dir1 = 'u'
    if pos[1] == 0: dir2 = 'r'
    else: dir2 = 'l'
    start_beams.append([pos[0], pos[0], dir1])
    start_beams.append([pos[0], pos[0], dir2])

for beam in start_beams:
    energy_grid = np.array([['.']*len(grid[0])]*len(grid))
    visited_states = set()

    beams = []
    beams.append(beam)

    while beams:
        beam = beams.pop()
        x, y, direction = beam
        energy_grid[x][y] = '#'

        if tuple(beam) not in visited_states:
            suggested_beams = propagate_beam(copy.copy(beam), grid[x][y])
            #print(suggested_beams)
            for sb in suggested_beams:
                if sb and position_is_valid(sb, grid):
                    beams.append(sb)

        #print(beam)
        visited_states.add(tuple(beam))

    #print(list2string(energy_grid))
    energy.append(list2string(energy_grid).count('#'))

print(max(energy))