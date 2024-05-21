import re

test_input = False
if test_input:
   input_file = "day01test.txt"
else:
    input_file = "day01.txt"

with open(input_file, "r") as f:
    puzzle_input = f.read().strip()

def part1(puzzle_input):
    elves = puzzle_input.split("\n\n")
    calories = []
    for elf in elves:
        calories.append(sum(map(int, elf.split("\n"))))
    return max(calories)

def part2(puzzle_input):
    elves = puzzle_input.split("\n\n")
    calories = []
    for elf in elves:
        calories.append(sum(map(int, elf.split("\n"))))
    return sum(sorted(calories, reverse=True)[:3])

print(part1(puzzle_input))
print(part2(puzzle_input))
