import re
import numpy as np

def list2string(lst):
    result = ''
    for row in lst:
        for col in row:
            result += col
        result += '\n'
    return result

input_file = 'day18_input.txt'

with open(input_file, "r") as f:
    puzzle_input = f.read().strip()

digs = re.findall(r'([A-Z]) ([0-9]+) \((\#[0-9a-f]{6})\)', puzzle_input)
#digs = re.findall(r'\((\#[0-9a-f]{6})\)', puzzle_input)

#print(digs)

pos = [0, 0]
digged_tiles = set([tuple(pos)])
for dig in digs:
    for k in range(int(dig[1])):
        if dig[0] == 'R': pos[1] += 1
        if dig[0] == 'L': pos[1] -= 1
        if dig[0] == 'D': pos[0] += 1
        if dig[0] == 'U': pos[0] -= 1
        digged_tiles.add(tuple(pos))

#print(digged_tiles)

#m, n = max([x[0] for x in digged_tiles]), max([x[1] for x in digged_tiles])
#M = np.full((m+1, n+1), '.')
#for tile in digged_tiles:
#    M[tile] = '#'


directions = ['R', 'L', 'D', 'U']
x, y = 1, 1
queue = [(x, y)]
while queue:
    x, y = queue.pop()
    for d in directions:
        if d == 'R': x_, y_ = x, y+1
        if d == 'L': x_, y_ = x, y-1
        if d == 'D': x_, y_ = x+1, y
        if d == 'U': x_, y_ = x-1, y
        if (x_, y_) not in digged_tiles:
            queue.append((x_, y_))
            digged_tiles.add((x_, y_))

#m, n = max([x[0] for x in digged_tiles]), max([x[1] for x in digged_tiles])
#M = np.full((m+1, n+1), '.')
#for tile in digged_tiles:
#    M[tile] = '#'

#print(list2string(M))
#print(list2string(M).count('#'))

print(len(digged_tiles))

### Part 2

pos = [0, 0]
digged_tiles = set([tuple(pos)])
corners = [(0, 0)]
for dig in digs:
    direction, distance, color = dig
    distance = int(color[1:-1], 16)
    direction = color[-1]

    for k in range(distance):
        if direction == '0': pos[1] += 1
        if direction == '2': pos[1] -= 1
        if direction == '1': pos[0] += 1
        if direction == '3': pos[0] -= 1
        digged_tiles.add(tuple(pos))
        if k == distance - 1:
            corners.append(tuple(pos))


#print(digged_tiles)

#m, n = max([x[0] for x in digged_tiles]), max([x[1] for x in digged_tiles])
#M = np.full((m+1, n+1), '.')
#for tile in digged_tiles:
#    M[tile] = '#'

#print("Number of edge tiles: ", len(digged_tiles))

# directions = ['R', 'L', 'D', 'U']
# x, y = 1, 1
# queue = [(x, y)]
# i = 0
# # unpractical
# while queue:
#     i += 1
#     if i % 1e7 == 0:
#         print("Length of queue: ", len(queue))
#         break
#     x, y = queue.pop()
#     for d in directions:
#         if d == 'R': x_, y_ = x, y+1
#         if d == 'L': x_, y_ = x, y-1
#         if d == 'D': x_, y_ = x+1, y
#         if d == 'U': x_, y_ = x-1, y
#         if (x_, y_) not in digged_tiles:
#             queue.append((x_, y_))
#             digged_tiles.add((x_, y_))

# #m, n = max([x[0] for x in digged_tiles]), max([x[1] for x in digged_tiles])
# #M = np.full((m+1, n+1), '.')
# #for tile in digged_tiles:
# #    M[tile] = '#'

# #print(list2string(M))
# #print(list2string(M).count('#'))

# print(len(digged_tiles))

# Shoelace method
A = 0
for k in range(len(corners)-1):
    A += corners[k][0]*corners[k+1][1] - corners[k][1]*corners[k+1][0]
A /= 2

print(int(abs(A)+len(digged_tiles)/2+1))