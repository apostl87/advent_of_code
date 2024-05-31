import sys, numpy as np, re
from aoclib import *
from collections import defaultdict
from aoclib import string2list

if "--test" in sys.argv or "-t" in sys.argv:
    test = True
else:
    test = False

input_file = (sys.argv[0].split(".")[0][1:])
input_file += "test.txt" if test==True else ".txt"
with open(input_file, "r") as f:
    input_ = f.read().strip()

trench_coords = re.findall(r'(\d+)..(\d+), y=([-]*\d+)..([-]*\d+)', input_)[0]

def shoot_probe(v, trench_coords):
    xmin, xmax, ymin, ymax = [int(c) for c in trench_coords]
    y, x = 0, 0
    highest_y = y
    while True:
        x, y = x + v[0], y + v[1]
        highest_y = max(y, highest_y)
        if xmin <= x <= xmax and ymin <= y <= ymax:
            return 1, highest_y
        if x > xmax:
            return -1, None
        elif y < ymin:
            return -2, None
        elif (x < xmin and v[0] == 0):
            return -3, None
        if v[0] > 0: v[0] -= 1
        elif v[0] < 0: v[0] += 1
        v[1] -= 1


def plot(v, trench_coords):
    xmin, xmax, ymin, ymax = [int(c) for c in trench_coords]
    trajectory = [(0, 0)]
    while True:
        x, y = trajectory[-1]
        if xmin <= x <= xmax and ymin <= y <= ymax:
            break
        trajectory.append((x+v[0], y+v[1]))
        if v[0] > 0: v[0] -= 1
        elif v[0] < 0: v[0] += 1
        v[1] -= 1

    ymax_plot = max(ymax, max([y for x, y in trajectory]))
    ymin_plot = ymin
    grid = ('.'*(xmax+1) + "\n")*(ymax_plot - ymin_plot + 1)
    grid = string2list(grid.strip())

    print(len(grid))
    grid.reverse()
    print(len(grid))
    for x in range(xmin, xmax+1):
        for y in range(ymin, ymax+1):
            print(y-ymin_plot)
            print(len(grid[y-ymin_plot]))
            print(x)
            grid[y-ymin_plot][x] = 'T'
    for x, y in trajectory:
        grid[y-ymin_plot][x] = '#'
    grid[0-ymin_plot][0] = 'S'
    grid.reverse()
    print(list2string(grid))


# Part 1
vy_max = -np.infty
vy_test = 100
ytested = set()
while True:
    if vy_test in ytested:
        break
    else:
        ytested.add(vy_test)
    vx_test = vy_test // 2
    xtested = set()
    while True:
        if vx_test in xtested:
            break
        else:
            xtested.add(vx_test)
        result = shoot_probe([vx_test, vy_test], trench_coords)
        match result[0]:
            case 1: break
            case -1: vx_test -= 1
            case -2: vx_test += 1
            case -3: vx_test += 1
    #print(result, vx_test, vy_test)
    if result[0] < 0:
        if vy_test == vy_max + 1:
            break
        else:
            vy_test //= 2
    else:
        if vy_test > vy_max:
            vy_max = vy_test
            vx_vy_max = vx_test
            highest_y = result[1]
        vy_test += 1

#plot([vx_vy_max, vy_max], trench_coords)
print("Part 1: Initial velocity:", vx_vy_max, vy_max, "| Highest y:", highest_y)


# Part 2
vy_min = int(trench_coords[2])
i = 0
while True:
    i += 1
    distance_till_stopped = sum(range(i+1))
    if distance_till_stopped >= int(trench_coords[0]):
        break
vx_min = i
vx_max = int(trench_coords[1])

initial_velocities = set()
for vx in range(vx_min, vx_max + 1):
    for vy in range(vy_min, vy_max + 1):
        success, _ = shoot_probe([vx, vy], trench_coords)
        if success == 1: initial_velocities.add((vx, vy))

print(len(initial_velocities), "distinct init. velocities")