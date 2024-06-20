input_ = open("11.in").read().strip()

steps = input_.split(',')

dirs = ['n', 'ne', 'nw','s','sw','se']

# Part 1
counts = dict()
for dir in dirs:
    #print(dir, steps.count(dir))
    counts[dir] = steps.count(dir)

nsmin = min(counts['n'], counts['s'])
counts['n'] -= nsmin
counts['s'] -= nsmin

neswmin = min(counts['ne'], counts['sw'])
counts['ne'] -= neswmin
counts['sw'] -= neswmin

nwsemin = min(counts['nw'], counts['se'])
counts['nw'] -= nwsemin
counts['se'] -= nwsemin

for dir in dirs:
    #print(dir, counts[dir])
    pass
    
# For my input
nwswmin = min(counts['nw'], counts['sw'])
counts['s'] += nwswmin
counts['nw'] -= nwswmin
counts['sw'] -= nwswmin

print(sum(counts.values()))

# Part 2
x = 0 # south-east direction
y = 0 # north direction
dmax = 0 # at origin
for step in steps:
    if step == 'n':
        y += 1
    elif step == 'ne':
        x += 1
        y += 1
    elif step == 'nw':
        x -= 1
    elif step == 's':
        y -= 1
    elif step == 'sw':
        x -= 1
        y -= 1
    elif step == 'se':
        x += 1
    if (x >= 0 and y >= 0) or (x <= 0 and y <= 0):
        d = max(abs(x), abs(y))
    else:
        d = abs(x) + abs(y)
    dmax = max(d, dmax)
print(dmax)