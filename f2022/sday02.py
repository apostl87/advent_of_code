import re

test_input = False
if test_input:
   input_file = "day02test.txt"
else:
    input_file = "day02.txt"

with open(input_file, "r") as f:
    puzzle_input = f.read().strip()

def part1(puzzle_input):
    guidelines = re.findall(r'(\w) (\w)', puzzle_input)

    oppplays = 'ABC' # opponent plays
    couplays = 'YZX' # winning counterplays
    shapevalues = {'X': 1, 'Y': 2, 'Z': 3}

    score = 0
    for game in guidelines:
        score += shapevalues[game[1]]
        id0 = oppplays.index(game[0])
        id1 = couplays.index(game[1])
        if id0 == id1:
            score += 6
        elif id1-id0 in [-1, 2]:
            score += 3

    return score

def part2(puzzle_input):
    guidelines = puzzle_input.split("\n")

    oppvalues = {'A': 1, 'B': 2, 'C': 3}
    couplayvalues = {'X': 0, 'Y': 3, 'Z': 6}

    score = 0
    for game in guidelines:
        game = game.replace(" ", "")
        score += couplayvalues[game[-1]]
        if game in ['AY', 'BX', 'CZ']:
            score += 1
        elif game in ['BY', 'CX', 'AZ']:
            score += 2
        else:
            score += 3

    return score

print(part1(puzzle_input))
print(part2(puzzle_input))
