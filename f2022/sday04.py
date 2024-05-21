import re

test_input = False
if test_input:
   input_file = "day04test.txt"
else:
    input_file = "day04.txt"

with open(input_file, "r") as f:
    puzzle_input = f.read().strip()

def part1(puzzle_input):
    regex = r'(\d+)-(\d+),(\d+)-(\d+)'
    sectionpairs = re.findall(regex, puzzle_input)
    n = 0
    for sp in sectionpairs:
        sp = [int(x) for x in sp]
        if (sp[0] >= sp[2] and sp[1] <= sp[3]) or (sp[0] <= sp[2] and sp[1] >= sp[3]):
            n += 1
    return n
    
def part2(puzzle_input):
    regex = r'(\d+)-(\d+),(\d+)-(\d+)'
    sectionpairs = re.findall(regex, puzzle_input)
    n = 0
    for sp in sectionpairs:
        sp = [int(x) for x in sp]
        #if (sp[1] >= sp[2] and sp[0] <= sp[2]) or (sp[0] <= sp[3] and sp[1] >= sp[3]):
        if (sp[1] >= sp[2] and sp[0] <= sp[3]):
            n += 1
    return n

print("Part 1:", part1(puzzle_input))
print("Part 2:", part2(puzzle_input))
