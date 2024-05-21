import re
from collections import defaultdict

test_input = False
if test_input:
   input_file = "day07test.txt"
else:
    input_file = "day07.txt"

with open(input_file, "r") as f:
    puzzle_input = f.read().strip()
with open(input_file, "r") as f:
    lines = [line.split() for line in f.read().strip().split('\n')]

def part1(puzzle_input):
    sizes = defaultdict(int)
    
    for line in puzzle_input.split("\n"):
        #line = line.split()
        if '$ cd' in line:
            target_dir = re.findall(r'cd ([\S]*)', line)[0]
            if target_dir == '/':
                path = [target_dir]
            elif target_dir == '..':
                path.pop()
            else:
                path.append(path[-1] + '/' + target_dir)
        elif line[0].isnumeric():
            for p in path:
                sizes[p] += int(re.findall(r'\d+', line)[0])
 
    return sum([val for val in sizes.values() if val <= 100_000])


def part2(puzzle_input):
    sizes = defaultdict(int)
    
    for line in puzzle_input.split("\n"):
        #line = line.split()
        if '$ cd' in line:
            target_dir = re.findall(r'cd ([\S]*)', line)[0]
            if target_dir == '/':
                path = [target_dir]
            elif target_dir == '..':
                path.pop()
            else:
                path.append(path[-1] + '/' + target_dir)
        elif line[0].isnumeric():
            for p in path:
                sizes[p] += int(re.findall(r'\d+', line)[0])

    unused_space = 7e7 - sizes['/']
    threshold = 3e7 - unused_space

    for p in sorted(sizes, key=lambda x: sizes[x]):
        if sizes[p] >= threshold:
            return p, sizes[p]
    
    return None

print("Part 1:", part1(puzzle_input))
print("Part 2:", part2(puzzle_input))

