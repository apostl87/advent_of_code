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

#def part1():
grid = [list([int(x_) for x_ in x]) for x in input_.split("\n")]
m, n = len(grid), len(grid[0])

queue = [(0, 0, 0)] # x, y, risk-level
visited_ = set()
min_risk = 1e10
it = 0
deltas = [(0, 1), (1, 0), (0, -1), (-1, 0)]
#deltas = [(0, 1), (1, 0)]
while queue:
    it += 1
    y, x, risk = queue.pop(0)
    if (y, x) in visited_:
        continue
    # if it == 100000 or (y == 10 and x == 10):
    #     print(y, x, risk, visited_)
    #     break
    # if y == (m-1)//10 and x == (n-1)//10:
    #     print(y, x, risk, visited_)
    #     break
    if y == m-1 and x == n-1:
        min_risk = min(min_risk, risk)
        continue
    visited_.add((y, x))
    print(len(visited_))

    for delta in deltas:
        y_new, x_new = y+delta[0], x+delta[1]
        if (y_new, x_new) not in visited_ and 0 <= y_new <= m-1 and 0 <= x_new <= n-1:
            queue.append((y_new, x_new, risk+grid[y_new][x_new]))
print(min_risk)