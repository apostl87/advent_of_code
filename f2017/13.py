from collections import defaultdict, deque
import re

input_ = open("13.in").read().strip()

def init():
    scanners = defaultdict(lambda: defaultdict(int))
    for line in input_.splitlines():
        depth, range_ = line.split(': ')
        scanners[int(depth)]['range'] = int(range_)
        scanners[int(depth)]['position'] = 0
        scanners[int(depth)]['direction'] = 1
    return scanners

# Part 1
scanners = init()
severity = 0
for i in range(max(scanners)):
    if i in scanners and scanners[i]['position'] == 0:
        severity += i * scanners[i]['range']
    for scanner in scanners:
        dir_ = scanners[scanner]['direction']
        pos = scanners[scanner]['position']
        rng = scanners[scanner]['range']
        if dir_ == 1:
            if pos == rng - 1:
                scanners[scanner]['direction'] = -1
                scanners[scanner]['position'] -= 1
            else:
                scanners[scanner]['position'] += 1
        else:
            if pos == 0:
                scanners[scanner]['direction'] = 1
                scanners[scanner]['position'] += 1
            else:
                scanners[scanner]['position'] -= 1
print(severity)

# Part 2
def scanner_position(range_, time):
    cycle_length = (range_ - 1) * 2
    additional_time = time % cycle_length
    return (range_ - 1) - abs(additional_time - cycle_length//2)

scanners = init()
# Variant 1
delay = 10
while any(scanner_position(scanners[x]['range'], x + delay) == 0 for x in scanners):
    delay += 1
print("Delay:", delay)

# Variant 2
delay = 10
while any((x + delay) % ((scanners[x]['range'] - 1) * 2) == 0 for x in scanners):
    delay += 1
print("Delay:", delay)