import re
import numpy as np

with open("day10_input.txt", "r") as f:
    puzzle_input = f.read()


def part1(puzzle_input):
    lines = puzzle_input.split("\n")

    sketch = [list(line) for line in lines]
    sketch = np.array(sketch)

    ap = np.where(sketch=='S') # animal position
    ap = [x[0] for x in ap]

    pp = {} # pipe parts
    pp['dir1'] = [] # pipe direction 1
    pp['dir2'] = [] # pipe direction 2

    i = 1 # current pipe direction index

    # to the north
    if ap[0] > 0:
        p = (ap[0]-1, ap[1]) # position
        if sketch[p] in ['|', '7', 'F']:
            pp['dir'+str(i)].append((p, 's'))
            i += 1
    # to the east
    if ap[1] < sketch.shape[1]-1:
        p = (ap[0], ap[1]+1)
        if sketch[p] in ['-', '7', 'J']:
            pp['dir'+str(i)].append((p, 'w'))
            i += 1
    # to the south
    if i < 3 and ap[0] < sketch.shape[0]-1:
        p = (ap[0]+1, ap[1])
        if sketch[p] in ['|', 'L', 'J']:
            pp['dir'+str(i)].append((p, 'n'))
            i += 1
    # to the west
    if i < 3 and ap[1] > 0:
        p = (ap[0], ap[1]-1)
        if sketch[p] in ['-', 'L', 'F']:
            pp['dir'+str(i)].append((p, 'e'))
            i += 1

    while pp['dir1'][-1][0] != pp['dir2'][-1][0]:
        parts = (pp['dir1'][-1], pp['dir2'][-1])

        for i, part in enumerate(parts, start=1):
            pipe = sketch[part[0]]
            if pipe == "-":
                if part[1] == "w":
                    p = ((part[0][0], part[0][1]+1), "w")
                else:
                    p = ((part[0][0], part[0][1]-1), "e")
                pp['dir'+str(i)].append(p)
            if pipe == "J":
                if part[1] == "w":
                    p = ((part[0][0]-1, part[0][1]), "s")
                else:
                    p = ((part[0][0], part[0][1]-1), "e")
                pp['dir'+str(i)].append(p)
            if pipe == "7":
                if part[1] == "w":
                    p = ((part[0][0]+1, part[0][1]), "n")
                else:
                    p = ((part[0][0], part[0][1]-1), "e")
                pp['dir'+str(i)].append(p)
            if pipe == "|":
                if part[1] == "n":
                    p = ((part[0][0]+1, part[0][1]), "n")
                else:
                    p = ((part[0][0]-1, part[0][1]), "s")
                pp['dir'+str(i)].append(p)
            if pipe == "F":
                if part[1] == "e":
                    p = ((part[0][0]+1, part[0][1]), "n")
                else:
                    p = ((part[0][0], part[0][1]+1), "w")
                pp['dir'+str(i)].append(p)
            if pipe == "L":
                if part[1] == "e":
                    p = ((part[0][0]-1, part[0][1]), "s")
                else:
                    p = ((part[0][0], part[0][1]+1), "w")
                pp['dir'+str(i)].append(p)

    print(pp)
    assert len(pp['dir1']) == len(pp['dir2'])
    return len(pp['dir1'])

print(part1(puzzle_input))

def part2(puzzle_input):
    pass

print(part2(puzzle_input))