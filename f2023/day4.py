import re
import numpy as np

with open("day4_input.txt", "r") as f:
    input_file = f.read()

def part1(input_file):
    regex = r':(.*)\|(.*)'
    points = 0
    for win_nums, true_nums in re.findall(regex, input_file):
        overlap = set(win_nums.split()) & set(true_nums.split())
        if overlap:
            points += 2 ** (len(overlap) - 1)

    return points

def part2(input_file):
    lines = input_file.split("\n")
    regex = r':(.*)\|(.*)'
    count_of_cards = np.ones(len(lines))
    for i, line in enumerate(lines):
        win_nums, true_nums = re.findall(regex, line)[0]
        matches = len(set(win_nums.split()) & set(true_nums.split()))
        count_of_cards[i+1:i+matches+1] += count_of_cards[i]

    return int(count_of_cards.sum())


print("Part 1: ", part1(input_file))
print("Part 2: ", part2(input_file))