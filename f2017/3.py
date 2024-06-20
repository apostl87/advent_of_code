from collections import defaultdict

input_ = open("3.in").read()
input_ = int(input_)

# Part 1
# Starting variables
cursor = 0
number = 1
grid = dict()
grid[cursor] = number
dir = 1j
# Constructing loop
while True:
    number += 1
    if cursor + dir*-1j not in grid:
        dir *= -1j
    cursor += dir
    grid[cursor] = number
    if number == input_:
        print(cursor)
        print(int(abs(cursor.real) + abs(cursor.imag)))
        break
    
# Part 2
# Starting variables
cursor = 0
grid = defaultdict(int)
print(grid)
grid[cursor] = 1
dir = 1j
adjacent = [1, 1+1j, 1j, -1+1j, -1, -1-1j, -1j, 1-1j]
# Constructing loop
while True:
    if grid[cursor + dir*-1j] == 0:
        dir *= -1j # Change direction by turning left
    cursor += dir
    grid[cursor] = sum([grid[x+cursor] for x in adjacent])

    if grid[cursor] > input_:
        print(grid[cursor])
        break
    