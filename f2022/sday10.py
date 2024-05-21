import re
from collections import defaultdict
import copy
import numpy as np

test_input = False
if test_input:
   input_file = "day10test.txt"
else:
    input_file = "day10.txt"

with open(input_file, "r") as f:
    puzzle_input = f.read().strip()

#def next_cycle(cycle, value):


def part1(puzzle_input):
    cycle = 0
    value = 1
    signal_strength = 0
    CRT = ''
    for line in puzzle_input.split("\n"):
        cycle += 1
        if cycle == 41: cycle -= 40
        CRT += '#' if abs(cycle - 1 - value)<= 1 else '.'
        if (cycle - 20) % 40 == 0:
            signal_strength += cycle*value
        if "noop" in line:
            value_to_add = 0
            continue
        else:
            cycle += 1
            if cycle == 41: cycle -= 40
            CRT += '#' if abs(cycle - 1 - value)<= 1 else '.'
            CRT += '\n' if cycle % 40 == 0 else ''
            if (cycle - 20) % 40 == 0:
                signal_strength += cycle*value
            value_to_add = int(line.split()[-1])
            value += value_to_add
    return signal_strength, CRT
    
def part2(puzzle_input):
    pass

print("Part 1:", part1(puzzle_input)[0])
print("Part 2:")
print(part1(puzzle_input)[1])