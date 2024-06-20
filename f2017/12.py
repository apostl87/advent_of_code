from collections import defaultdict, deque
import re

input_ = open("12.in").read().strip()

# init
pipes = dict()
for line in input_.splitlines():
    regex = r'\d+'
    programs = re.findall(regex, line)
    pipes[int(programs[0])] = [int(x) for x in programs[1:]]

# Parts 1 and 2
groups =  defaultdict(set)
cursor = 0
while cursor < len(pipes):
    if not any(cursor in gv for gv in groups.values()):
        q = deque([cursor])
    else:
        cursor += 1
        continue
    
    while q:
        p = q.pop()
        if p in groups[cursor]:
            continue
        groups[cursor].add(p)
        for p2 in pipes[p]:
            q.append(p2)
        
print("Part 1:", len(groups[0]))
print("Part 2:", len(groups))