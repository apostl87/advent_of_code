import sys, numpy as np
from itertools import cycle
from math import lcm

if "--test" in sys.argv or "-t" in sys.argv:
    test = True
else:
    test = False

input_file = "day17.txt"

with open(input_file, "r") as f:
    input_ = f.read().strip()

with open("day17rocks.txt", "r") as f:
    input__ = f.read().strip()

def print_cavern(x_indices, occupied):
    ymax = max([y for (y, x) in occupied])
    cavern = ''
    for y in range(ymax, -1, -1):
        for x in x_indices:
            cavern += '#' if (y, x) in occupied else '.'
        cavern += '\n'
    print(cavern)
    return cavern

# Parts 1 and 2
part2 = True
x_indices = [0, 1, 2, 3, 4, 5, 6]
xmax = max(x_indices)
rocks = input__.split("\n\n")
rocks = [[[x for x in line] for line in rock.split("\n")] for rock in rocks]
N = len(rocks)
rock_relative = []
for rock in rocks:
    rock.reverse()
    rock_relative.append(set())
    for y in range(len(rock)):
        for x in range(len(rock[0])):
            if rock[y][x] == '#':
                rock_relative[-1].add((y, x))
if test:
    jet_pattern = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"
else:
    jet_pattern = input_

M = len(jet_pattern)
jets = cycle(jet_pattern)
rocks = cycle(rocks)

def calc_height(num_stones):
 occupied = set()
 highest_y = -1
 heights = {}
 states = []
 rock_idx, jet_idx = 0, 0
 for i in range(10_000):
    rock = next(rocks)
    rock_idx = (rock_idx + 1) % N
    #print(i, rock, highest_y)

    rock_corner = (highest_y + 4, x_indices[2])

    movement = cycle(['jet', 'fall'])
    freeze = False
    while not freeze:
        m = next(movement)
        match m:
            case 'jet':
                jet_idx = (jet_idx + 1) % M
                if next(jets) == '>':
                    rock_corner_proposed = (rock_corner[0], rock_corner[1] + 1)
                else:
                    rock_corner_proposed = (rock_corner[0], rock_corner[1] - 1)
            case 'fall':
                rock_corner_proposed = (rock_corner[0] - 1, rock_corner[1])

        rock_pos = set()
        for (y, x) in rock_relative[i%N]:
            rock_pos.add((y + rock_corner_proposed[0], x + rock_corner_proposed[1]))

        # if i == 2:
        #     print(rock_pos)
        #     print(occupied)

        # print(m)
        # if occupied:
        #     print_cavern(x_indices, occupied)

        if m == 'fall': 
            if len(occupied & rock_pos) > 0 or rock_corner_proposed[0] == -1: # here, rock gets frozen
                for (y, x) in rock_pos:
                    occupied.add((y + 1, x))
                highest_y = max(highest_y, max(y for (y, x) in rock_pos) + 1)
                freeze = True

                # for Part 2: construct top row
                row = list('.'*(xmax + 1))
                for (y, x) in sorted(occupied, key=lambda x_: x_[0], reverse=True):
                    if y == highest_y:
                        row[x] = '#'
                    if y < highest_y:
                        break
                state = (rock_idx, jet_idx, row)
                if state in states:
                    #print(state)
                    cycle_start = states.index(state)
                    cycle_length = i - cycle_start
                    num_cycles = (num_stones-cycle_start-1)//cycle_length
                    remainder = (num_stones-cycle_start-1)%cycle_length

                    height_diff_per_cycle = highest_y - heights[cycle_start]
                    remainder_diff = heights[cycle_start+remainder] - heights[cycle_start]
                    print(i, num_cycles, cycle_start, cycle_length, remainder, highest_y, height_diff_per_cycle)

                    #return heights[num_stones] + 1
                    return heights[cycle_start] + height_diff_per_cycle*num_cycles + remainder_diff + 1
                else:
                    states.append(state)
                heights[i] = highest_y
                
            else:
                rock_corner = rock_corner_proposed
                # print("moved")
        else:
            if len(occupied & rock_pos) == 0 and min(x for (y, x) in rock_pos) >= 0 and max(x for (y, x) in rock_pos) <= xmax:
                rock_corner = rock_corner_proposed
                # print("moved")
   
    if i+1 == num_stones:
        return highest_y + 1

#print_cavern(x_indices, occupied)
print("Part 1: Height:", calc_height(2022))
print("Part 2: Height:", calc_height(1_000_000_000_000))
#num_stones = 1_000_000_000_000 if part2 else 2022