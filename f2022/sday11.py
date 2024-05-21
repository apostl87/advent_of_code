import re
from collections import defaultdict
import copy
import numpy as np

test_input = False
if test_input:
   input_file = "day11test.txt"
else:
    input_file = "day11.txt"

with open(input_file, "r") as f:
    puzzle_input = f.read().strip()

def part1(puzzle_input):
    segments = puzzle_input.split("\n\n")

    items = defaultdict(list)
    op = defaultdict(list)
    divisor = defaultdict(list)
    action = defaultdict(list)
    counts = defaultdict(int)

    #print(segments)

    for i, segment in enumerate(segments):
        lines = segment.split("\n")
        items[i] = [int(x) for x in re.findall(r'(\d+)', lines[1])]
        op[i] = lines[2].split()[-2:]
        divisor[i] = int(lines[3].split()[-1])
        action[i] = [int(lines[x].split()[-1]) for x in range(4, 6)]

    for i in range(20):
        for j in range(len(items)):
            counts[j] += len(items[j])
            while items[j]:
                item = items[j].pop(0)
                if op[j][0] == '*':
                    if op[j][1] == 'old':
                        item **= 2
                    else:
                        item *= int(op[j][1])
                if op[j][0] == '+':
                    item += int(op[j][1])
                item //= 3
                testresult = min(item % divisor[j], 1)
                items[action[j][testresult]].append(item)

    vals = sorted(counts.values(), reverse=True)
    return vals, vals[0]*vals[1]
    
def part2(puzzle_input):
    segments = puzzle_input.split("\n\n")

    items = defaultdict(list)
    op = defaultdict(list)
    divisor = defaultdict(list)
    action = defaultdict(list)
    counts = defaultdict(int)

    #print(segments)
    lcm = 1
    for i, segment in enumerate(segments):
        lines = segment.split("\n")
        items[i] = [int(x) for x in re.findall(r'(\d+)', lines[1])]
        op[i] = lines[2].split()[-2:]
        divisor[i] = int(lines[3].split()[-1])
        action[i] = [int(lines[x].split()[-1]) for x in range(4, 6)]
        lcm *= divisor[i]

    for _ in range(10000):
        for j in range(len(items)):
            counts[j] += len(items[j])
            op_ = op[j]
            div_ = divisor[j]
            act_ = action[j]

            for item in items[j]:
                if op_[0] == '*':
                    if op_[1] == 'old':
                        item **= 2
                    else:
                        item *= int(op_[1])
                elif op_[0] == '+':
                    item += int(op_[1])
                
                item %= lcm

                if item % div_ == 0:
                    items[act_[0]].append(item)
                else:
                    items[act_[1]].append(item)
                
            items[j] = []

    vals = sorted(counts.values(), reverse=True)
    return vals, vals[0]*vals[1]

print("Part 1:", part1(puzzle_input))
print("Part 2:")
print(part2(puzzle_input))