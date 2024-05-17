import re
import copy
from itertools import combinations
import sympy as sp

input_file = './day24_input.txt'

with open(input_file, "r") as f:
    puzzle_input = f.read().strip()

hailstones = re.findall(r'([ -]*\d+), ([ -]*\d+), ([ -]*\d+) @ ([ -]*\d+), ([ -]*\d+), ([ -]*\d+)', puzzle_input)

for i, h in enumerate(hailstones):
    hailstones[i] = list(h)
    hailstones[i].insert(0, i)
#print(hailstones)

### Part 1
c = combinations(hailstones, 2)

results = set()
count = 0
while c_:=next(c, False):
    (idx1, px1, py1, pz1, vx1, vy1, vz1), (idx2, px2, py2, pz2, vx2, vy2, vz2) = map(float, c_[0]), map(float, c_[1])

    if (vx1/vx2 == vy1/vy2):
        results.add((idx1, idx2, None, None, None, None, 'parallel'))
        continue

    #t_intersect = (px1-py1-px2+py2)/(-vx1+vy1+vx2-vy2)
    t2 = (px1*vy1 - py1*vx1 - px2*vy1 + py2*vx1)/(vx2*vy1 - vy2*vx1)
    t1 = (px2 + t2*vx2 - px1)/vx1
    x = px2 + t2*vx2
    y = py2 + t2*vy2
    results.add((idx1, idx2, t1, t2, x, y, 'regular'))

    #if t1 >= 0 and t2 >= 0 and \
    #    x >= 7 and x <= 27 and y >= 7 and y <= 27:
    if t1 >= 0 and t2 >= 0 and \
        x >= 200000000000000 and y >= 200000000000000 and \
        x <= 400000000000000 and y <= 400000000000000:
        count += 1

print("Part 1: Intersecting hailstone paths:", count)

### Part 2

three_hailstones = hailstones[1:4]
three_hailstones = [tuple(map(int, x)) for x in three_hailstones]
#print(three_hailstones)

unknowns = sp.symbols('x y z dx dy dz t1 t2 t3')
x, y, z, dx, dy, dz, *time = unknowns

equations = []
for t, h in zip(time, three_hailstones):
    i = 1
    equations.append(sp.Eq(x + t*dx, h[i] + t*h[i+3]))
    i = 2
    equations.append(sp.Eq(y + t*dy, h[i] + t*h[i+3]))
    i = 3
    equations.append(sp.Eq(z + t*dz, h[i] + t*h[i+3]))

#print(equations)
solution = sp.solve(equations, unknowns).pop()

print(sum(solution[:3]))

# x1 = dx1+t*vx1
# y1 = dy1+t*vy1
# x2 = dx2+t*vx2
# y2 = dy2+t*vy2

# dx1 + t1*vx1 = dx2 + t2*vx2
# dy1 + t1*vy1 = dy2 + t2*vy2

# dx1*vy1 - dy1*vx1 = dx2*vy1 - dy2*vx1 + t2(vx2*vy1 - vy2*vx1)
# (px1*vy1 - py1*vx1 - px2*vy1 + py2*vx1)/(vx2*vy1 - vy2*vx1) = t
# t1 = (px2 + t2*vx2 - px1)/vx1

# px1 + t*vx1 = px2 + t*vx2
# py1 + t*vy1 = py2 + t*vy2
# pz1 + t*vz1 = pz2 + t*vz2

# dx1*vy1 - dy1*vx1 = dx2*vy1 - dy2*vx1 + t2(vx2*vy1 - vy2*vx1)
# (px1*vy1 - py1*vx1 - px2*vy1 + py2*vx1)/(vx2*vy1 - vy2*vx1) = t
# t1 = (px2 + t2*vx2 - px1)/vx1
