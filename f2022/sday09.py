import re
from collections import defaultdict
import copy
import numpy as np

test_input = False
if test_input:
   input_file = "day09test.txt"
else:
    input_file = "day09.txt"

with open(input_file, "r") as f:
    puzzle_input = f.read().strip()

def part1(puzzle_input):
    moves = puzzle_input.split("\n")
    
    dir_delta = {'L': (0, -1), 'R': (0, 1),
                  'D': (1, 0), 'U': (-1, 0)}

    start = [0, 0]
    head_pos = copy.copy(start)
    tail_pos = copy.copy(start)
    visited = set((0,0))
    
    for move in moves:
        dir_, count = move[0], int(move[2:])
        for _ in range(count):
            head_pos[0] += dir_delta[dir_][0]
            head_pos[1] += dir_delta[dir_][1]
            headtaildelta = [x1-x2 for x1, x2 in zip(head_pos, tail_pos)]
            #print('before ', headtaildelta)
            sum_ = sum([abs(x) for x in headtaildelta])
            if sum_ == 1 or (sum_ == 2 and 0 not in headtaildelta):
                continue
            #elif 0 in headtaildelta:
            #    tail_pos[0] += headtaildelta[0]/2
            #    tail_pos[1] += headtaildelta[1]/2
            else:
                tail_pos[0] += headtaildelta[0]/max(1, abs(headtaildelta[0]))
                tail_pos[1] += headtaildelta[1]/max(1, abs(headtaildelta[1]))
            visited.add(tuple(tail_pos))
            headtaildelta = [x1-x2 for x1, x2 in zip(head_pos, tail_pos)]
            #print('afterwards', headtaildelta)

    return len(visited)
    
def part2(puzzle_input):
    moves = puzzle_input.split("\n")
    
    dir_delta = {'L': (0, -1), 'R': (0, 1),
                  'D': (1, 0), 'U': (-1, 0)}

    n_knots = 10
    x = [0 for _ in range(n_knots)]
    y = [0 for _ in range(n_knots)]
    visited = set()
    visited.add((0, 0))
    
    for k, move in enumerate(moves):
        dir_, count = move[0], int(move[2:])
        for l in range(count):
            x[0] += dir_delta[dir_][0]
            y[0] += dir_delta[dir_][1]
            for i in range(1, n_knots):
                if abs(x[i] - x[i-1]) > 1 or abs(y[i] - y[i-1]) > 1:
                    x[i] += np.sign(x[i-1] - x[i])
                    y[i] += np.sign(y[i-1] - y[i])
                    #if i == n_knots - 1:
                    #    print(k, l, i, "Tail moved", x[-1], y[-1])
                     #   print(len(visited))
            visited.add((x[-1], y[-1]))

    return len(visited)

print("Part 1:", part1(puzzle_input))
print("Part 2:", part2(puzzle_input))