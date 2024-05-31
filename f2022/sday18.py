import sys, numpy as np

if "--test" in sys.argv or "-t" in sys.argv:
    test = True
else:
    test = False

input_file = (sys.argv[0].split(".")[0][1:])
input_file += "test.txt" if test==True else ".txt"

with open(input_file, "r") as f:
    input_ = f.read().strip()

# Part 1
positions = set()
for line in input_.split("\n"):
    x, y, z = [int(n) for n in line.split(",")]
    positions.add((x, y, z))

def get_neighbors(pos):
    return [(pos[0]+1, pos[1], pos[2]), (pos[0]-1, pos[1], pos[2]), \
                 (pos[0], pos[1]+1, pos[2]), (pos[0], pos[1]-1, pos[2]), \
                 (pos[0], pos[1], pos[2]+1), (pos[0], pos[1], pos[2]-1)]

exposed_sides = []
for pos in positions:
    neighbors = get_neighbors(pos)
    count = 0
    for n in neighbors:
        count += 1 if tuple(n) in positions else 0
    exposed_sides.append(6 - count)

print("Part 1:", sum(exposed_sides))


# Part 2
start_corner = (-1, -1, -1)
end_corner = tuple([max([pos[i] for pos in positions]) for i in range(3)])
steam, ext_surface = set(), set()
steam.add(start_corner)

it = 0
queue = [start_corner]
while queue:
    steampos = queue.pop(0)
    neighbors = get_neighbors(steampos)
    for nb in neighbors:
        if all([x > -2 for x in nb]) and all([x < end+2 for x, end in zip(nb, end_corner)]):
            if nb not in steam:
                if nb not in positions:
                    steam.add(nb)
                    queue.append(nb)
                else:
                    ext_surface.add((steampos, nb))

print(len(ext_surface))