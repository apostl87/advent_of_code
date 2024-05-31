import re
from itertools import count
import copy

def get_id():
    num = 0
    while True:
        yield num
        num += 1

def list2string(list_):
    result = ""
    for line in list_:
        for char in line:
            result += str(char)
        result += "\n"
    return result

def string2list(str_):
    result = str_.split("\n")
    for r in result:
        result[result.index(r)] = list(r)
    return result

input_file = './day23_input.txt'

with open(input_file, "r") as f:
    puzzle_input = f.read().strip()

### Part 1
grid = puzzle_input.split("\n")
directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
direction_signs = 'v>^<.'

visited = []
positions = []

n = 0 # steps so far
x, y, last_d = 0, 1, 0
gen = get_id()
idx = next(gen)
queue = [(idx, n, x, y, last_d, list())]

xmark = []
ymark = []

it = 0
counter = 0
while queue:
    it += 1
    if it % 10000 == 0:
        #print("Iteration", it)
        print("Length of queue:", len(queue))
        print("x =", x, ", y =", y)
    #print(queue)
    idx, n, x, y, last_d, visited_ = queue.pop(0)

    if idx>len(positions)-1:
        positions.append((n, x, y, last_d))
        visited.append(visited_)

    positions[idx] = (n, x, y, last_d)
    visited[idx] = visited_
    visited[idx].append((x, y))

    if x == len(grid)-1 and y == len(grid[0])-2:
        print("end reached")
        #print(sorted(visited[idx], key=lambda x: x[1]))
        print(idx, visited[idx][-1])
        counter += 1
        continue

    #print(positions[idx])

    direction_id = direction_signs.index(grid[x][y]) # Part 1
    direction_id = 4 # Part 2
    if direction_id < 4:
        d_ = [directions[direction_id]] 
    else:
        d_ = []
        for direction_id in range(4):
            if abs(direction_id-last_d)==2:
                continue
            else:
                d_.append(directions[direction_id])

    j = 0
    #print(len(d_))
    for d__ in d_:
        #print(d__)
        #print(x, y)
        x_new = x + d__[0]
        y_new = y + d__[1]
        n_new = n + 1
        #print(x_new, y_new)
        if x_new<0 or x_new>len(grid)-1 or \
            y_new<0 or y_new>len(grid[0])-1 or \
            grid[x_new][y_new] == '#' or \
            (x_new, y_new) in visited[idx]:
            continue
        j += 1
        if j > 1:
            nextidx = next(gen)
            #print(idx)
            queue.append((nextidx, n_new, x_new, y_new, directions.index(d__), copy.copy(visited[idx])))
            #print([q[:4] for q in queue])
            #print("Iteration:", it)
            #counter += 1
        else:
            queue.insert(0, (idx, n_new, x_new, y_new, directions.index(d__), visited[idx]))
    #if len(queue) > 100:
        if (last_d == 0 and directions.index(d__) == 3) or \
            (last_d == 1 and directions.index(d__) == 2):
            xmark.append(x_new)
            ymark.append(y_new)
    
    if counter == 100:
        break
    #print(j)

print(positions[63])

# debugging
fullgrid = string2list(puzzle_input)
for q in queue:
    fullgrid[q[2]][q[3]] = 'O'
for v in visited:
    for v_ in v:
        if fullgrid[v_[0]][v_[1]] != 'O':
            fullgrid[v_[0]][v_[1]] = 'X'
            pass
#for x, y in zip(xmark, ymark):
    #fullgrid[x][y] = str(x)+", "+str(y)
#print(list2string(fullgrid))
with open("output.txt", "w") as f:
    f.write(list2string(fullgrid))

# Part 1
imax, vmax = max([[i, len(v)] for i, v in enumerate(visited)], key=lambda x: x[1])

# Part 2
imax, pmax = max([[i, p[0]] for i, p in enumerate(positions) if p[1]==len(grid)-1 and p[2]==len(grid[0])-2], key=lambda x: x[1])

# Display of longest path
fullgrid = string2list(puzzle_input)
for v in visited[imax]:
   fullgrid[v[0]][v[1]] = 'O'
#print(list2string(fullgrid))
print("Part 1:", imax, vmax-1)
print("Part 2:", imax, pmax)