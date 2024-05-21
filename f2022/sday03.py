import re
import string

test_input = False
if test_input:
   input_file = "day03test.txt"
else:
    input_file = "day03.txt"

with open(input_file, "r") as f:
    puzzle_input = f.read().strip()

def part1(puzzle_input):
    rucksacks = puzzle_input.split("\n")
    letters = ' ' + string.ascii_letters

    priority = 0
    for r in rucksacks:
        comp1 = r[:int(len(r)/2)]
        comp2 = r[int(len(r)/2):]

        for c in comp1:
            if c in comp2:
                priority += letters.index(c)
                break
    
    return priority

def part2(puzzle_input):
    rucksacks = puzzle_input.split("\n")
    letters = ' ' + string.ascii_letters

    priority = 0
    for i in range(len(rucksacks) // 3):
        r1, r2, r3 = rucksacks[i*3:i*3+3]
        r1, r2, r3 = sorted((r1, r2, r3), key=lambda x: len(x))
        for c in r1:
            if c in r2 and c in r3:
                priority += letters.index(c)
                break
    
    return priority

print("Part 1:", part1(puzzle_input))
print("Part 2:", part2(puzzle_input))
