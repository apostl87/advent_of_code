import re

with open("day9_input.txt", "r") as f:
    puzzle_input = f.read()

def part1(puzzle_input):
    histories = puzzle_input.split("\n")
    total = 0
    for history in histories:
        numbers = [int(x) for x in history.split()]
        final_numbers = []
        while set(numbers) != set([0]):
            final_numbers.append(numbers[-1])
            numbers = [numbers[i+1]-numbers[i] for i in range(len(numbers)-1)]
        total += sum(final_numbers)
    return total

print(part1(puzzle_input))

def part2(puzzle_input):
    histories = puzzle_input.split("\n")
    total = 0
    for history in histories:
        numbers = [int(x) for x in history.split()]
        initial_numbers = []
        while set(numbers) != set([0]):
            initial_numbers.append(numbers[0])
            numbers = [numbers[i+1]-numbers[i] for i in range(len(numbers)-1)]
        while len(initial_numbers)>1:
            sub = initial_numbers.pop()
            initial_numbers[-1] -= sub
        total += initial_numbers[0]
    return total

print(part2(puzzle_input))
