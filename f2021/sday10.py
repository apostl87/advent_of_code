import sys, numpy as np

if "--test" in sys.argv or "-t" in sys.argv:
    test = True
else:
    test = False

input_file = (sys.argv[0].split(".")[0][1:])
input_file += "test.txt" if test==True else ".txt"

with open(input_file, "r") as f:
    input_ = f.read().strip()

opening_signs = ['(', '[', '{', '<']
closing_signs = [')', ']', '}', '>']

def part1():
    lines = input_.split("\n")
    corruptions = ''
    for line in lines.copy():
        openers = []
        for c in line:
            if c in opening_signs:
                openers.append(opening_signs.index(c))
            else:
                if closing_signs.index(c) == openers[-1]:
                    openers.pop()
                else:
                    lines.remove(line)
                    corruptions += c
                    break

    return corruptions.count(')')*3 + corruptions.count(']')*57 + corruptions.count('}')*1197 + corruptions.count('>')*25137, lines

res1, incomplete_lines = part1()
print("Part 1:", res1)

def part2():
    scores = []

    for line in incomplete_lines:
        openers = []
        completion_string = ''
        for c in line:
            if c in opening_signs:
                openers.append(opening_signs.index(c))
            else:
                openers.pop()
        while openers:
            #idx = openers.pop()
            completion_string += closing_signs[openers.pop()]
        # calculate score
        score = 0
        while completion_string:
            score = score * 5 + closing_signs.index(completion_string[0]) + 1
            completion_string = completion_string[1:]
        scores.append(score)
    
    return sorted(scores)[len(scores)//2]

print("Part 2:", part2())