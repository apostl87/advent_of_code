import sys, numpy as np
import heapq

if "--test" in sys.argv or "-t" in sys.argv:
    test = True
else:
    test = False

input_file = (sys.argv[0].split(".")[0][1:])
input_file += "test.txt" if test==True else ".txt"

with open(input_file, "r") as f:
    input_ = f.read().strip()

def roll_100(seed):
    return (seed)%100 + 1, (seed+1)%100 + 1, (seed+2)%100 + 1

positions = [int(line.split()[-1]) for line in input_.splitlines()]
scores, n_rolls = [0, 0], 0
next_player = 0
while all([x < 1000 for x in scores]):
    positions[next_player] = (positions[next_player] + sum(roll_100(n_rolls)))%10
    scores[next_player] += positions[next_player] if positions[next_player] > 0 else 10
    n_rolls += 3
    next_player = 1 if next_player == 0 else 0
print("Part 1:", min(scores)*n_rolls )


# score 20: player wins 3 / 3
# score 19: player wins 2 / 3
# score 18: player wins 1 / 3
# score 17: opponent 
# 6 8 10
# 10 2 4 6