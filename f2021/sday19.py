from collections import defaultdict
from itertools import combinations

def dist_tup(t1,t2): return abs(t1[0] - t2[0]) + abs(t1[1] - t2[1]) + abs(t1[2] - t2[2])
def add_tup(t1,t2): return (t1[0] + t2[0], t1[1] + t2[1], t1[2] + t2[2])
def sub_tup(t1,t2): return (t1[0] - t2[0], t1[1] - t2[1], t1[2] - t2[2])
def inv_tup(t): return (-t[0], -t[1], -t[2])
def rot_tuple(t, r):
    x, y, z = t
    rotates = [ (x, y, z),(-y, x, z),(-x, -y, z),(y, -x, z),(-z, y, x),(-y, -z, x),
                (z, -y, x),(y, z, x),(-x, y, -z),(-y, -x, -z),(x, -y, -z),(y, x, -z),
                (z, y, -x),(-y, z, -x),(-z, -y, -x),(y, -z, -x),(x, -z, y),(z, x, y),
                (-x, z, y),(-z, -x, y),(x, z, -y),(-z, x, -y),(-x, -z, -y),(z, -x, -y)]
    return rotates[r]

data = [a.splitlines()[1:] for a in open("day19.txt").read().split("\n\n")]
scanners = [[(int(s.split(",")[0]), int(s.split(",")[1]), int(s.split(",")[2])) for s in a] for a in data]
grid, scanners = set(scanners[0]), scanners[1:]

positions = [(0, 0, 0)]
while scanners:
    for i, scanner_curr in enumerate(scanners[:]):
        for r in range(24):
            off = defaultdict(lambda: 0)
            for b in grid:
                for t in scanner_curr:
                    offset = sub_tup(rot_tuple(t, r), b)
                    off[offset] += 1
            for offset, ct in off.items():
                if ct >= 12:
                    scanners.remove(scanner_curr)
                    pos = inv_tup(offset)
                    positions.append(pos)
                    for t in scanner_curr:
                        t = rot_tuple(t, r)
                        grid.add(add_tup(t, pos))

print(len(grid)) # Part 1
print(max([sum([abs(x1 - x2) for x1, x2 in zip(pos[0], pos[1])]) for pos in combinations(positions, 2)])) # Part 2