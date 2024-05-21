import re
from collections import defaultdict
import copy
from functools import cmp_to_key

test_input = False
if test_input:
   input_file = "day13test.txt"
else:
    input_file = "day13.txt"

with open(input_file, "r") as f:
    puzzle_input = f.read().strip()

def cmp(x1, x2):
    if x1 < x2:
        return 1
    elif x1 > x2:
        return -1
    else:
        return 0

def rightorder(p1, p2):
    idx = 0
    while True:
        if p1 == [] and p2 == []:
            return 0
        elif idx > len(p1)-1:
            result = 1
        elif idx > len(p2)-1:
            result =  -1
        elif all([type(p[idx])==int for p in [p1, p2]]):
            result = cmp(p1[idx], p2[idx])
        elif all([type(p[idx])==list for p in [p1, p2]]):
            result = rightorder(p1[idx], p2[idx])
        elif type(p1[idx])==list and type(p2[idx])==int:
            result = rightorder(p1[idx], [p2[idx]])
        else: # type(p1[idx])==int and type(p2[idx])==list:
            result = rightorder([p1[idx]], p2[idx])

        if result == 0:
            idx += 1
        else:
            return result

def part1(puzzle_input):
    pairs = puzzle_input.split("\n\n")
    sum_rightorder = 0       
    for i, pair in enumerate(pairs, start=1):
        packets = [eval(x) for x in pair.split("\n")]
            
        if r := rightorder(*packets) == 1:
            sum_rightorder += i
        #print(i, r)

    return sum_rightorder
    
def part2(puzzle_input):
    pairs = puzzle_input.split("\n\n")
    packets = [] + [[[2]], [[6]]]
    for pair in pairs:
        [packets.append(eval(x)) for x in pair.split("\n")]

    sorted_packets = sorted(packets, key=cmp_to_key(rightorder), reverse=True)
    
    result = (sorted_packets.index([[2]])+1)*(sorted_packets.index([[6]])+1)

    return result

print("Part 1:", part1(puzzle_input))
print("Part 2:", part2(puzzle_input))
