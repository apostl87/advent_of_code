import string, copy
from collections import deque

inp = open("17.in").read().strip()

skip = int(inp)

buffer = deque([0])
for i in range(2017):
    buffer.rotate(-skip)
    buffer.append(i+1)
    
print("Part 1:", buffer[0])

buffer = deque([0])
last = -1
for i in range(50_000_000):
    buffer.rotate(-skip)
    buffer.append(i+1)
    
print("Part 2:", buffer[buffer.index(0)+1])