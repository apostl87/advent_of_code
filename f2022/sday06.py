import re

test_input = False
if test_input:
   input_file = "day06test.txt"
else:
    input_file = "day06.txt"

with open(input_file, "r") as f:
    puzzle_input = f.read().strip()

def part1(puzzle_input):
    i = 0
    while True:
        str_ = puzzle_input[i:i+4]
        if all([str_.count(x) == 1 for x in str_]):
            return i+4
        i += 1
    
def part2(puzzle_input):
    i = 0
    while True:
        str_ = puzzle_input[i:i+14]
        if all([str_.count(x) == 1 for x in str_]):
            return i+14
        i += 1

print("Part 1:", part1(puzzle_input))
print("Part 2:", part2(puzzle_input))
