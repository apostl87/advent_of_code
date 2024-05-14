import re

with open("day9_input.txt", "r") as f:
    puzzle_input = f.read()

histories = puzzle_input.split("\n")

total = 0
for history in histories:
    numbers = [int(x) for x in history.split()]
    final_numbers = []
    while set(numbers) != set([0]):
        final_numbers.append(numbers[-1])
        numbers = [numbers[i+1]-numbers[i] for i in range(len(numbers)-1)]
    total += sum(final_numbers)

print(total)