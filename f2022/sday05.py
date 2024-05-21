import re
from collections import defaultdict

test_input = False
if test_input:
   input_file = "day05test.txt"
else:
    input_file = "day05.txt"

with open(input_file, "r") as f:
    puzzle_input = f.read()

def read_stacks(puzzle_input):
    stacks, moves = puzzle_input.split("\n\n")
    stacks = stacks.split("\n")
    crates = defaultdict(list)
    for i in range(len(stacks)-2, -1, -1):
        for k, j in enumerate(range(1, len(stacks[i]), 4)):
            if stacks[i][j] != ' ':
                crates[k+1].append(stacks[i][j])
    return crates, moves

def solve_part1(crates, moves):
    for count_, from_, to_ in re.findall(r'\w+ (\d+) \w+ (\d+) \w+ (\d+)', moves):
        for i in range(int(count_)):
            crates[int(to_)].append(crates[int(from_)].pop())

    result = ''
    for x in crates:
        result += crates[x][-1]
    return result

def solve_part2(crates, moves):
    for count_, from_, to_ in re.findall(r'\w+ (\d+) \w+ (\d+) \w+ (\d+)', moves):
        crates[int(to_)] += crates[int(from_)][-int(count_):]
        crates[int(from_)] = crates[int(from_)][:-int(count_)]

    result = ''
    for x in crates:
        result += crates[x][-1]
    return result

result = solve_part1(*read_stacks(puzzle_input))
print("Part 1:", result)
result = solve_part2(*read_stacks(puzzle_input))
print("Part 2:", result)


    
    
def part2(puzzle_input):
    pass

