input_ = open("5.in").read().strip()

# Part 1
maze = [int(x) for x in input_.split()]
cursor = 0
i = 0
while cursor >= 0 and cursor < len(maze):
    i += 1
    maze[cursor] += 1
    cursor += maze[cursor] - 1
print(i)

# Part 2
maze = [int(x) for x in input_.split()]
cursor = 0
i = 0
while cursor >= 0 and cursor < len(maze):
    i += 1
    inc = -1 if maze[cursor] >= 3 else 1
    maze[cursor] += inc
    cursor += maze[cursor] - inc
print(i)