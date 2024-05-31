import sys, numpy as np, re
import heapq

if "--test" in sys.argv or "-t" in sys.argv:
    test = True
else:
    test = False

input_file = (sys.argv[0].split(".")[0][1:])
input_file += "test.txt" if test==True else ".txt"

with open(input_file, "r") as f:
    input_ = f.read().strip()

lines = input_.splitlines()
ranges = [[int(x_) for x_ in re.findall(r'[-]*\d+', x)] for x in lines]
commands = [line.split()[0] for line in lines]

active_cubes = set()
for r, c in zip(ranges, commands):
    if c == 'on':
        for x in range(max(-50, r[0]), min(r[1]+1, 51)):
            for y in range(max(-50, r[2]), min(r[3]+1, 51)):
                for z in range(max(-50, r[4]), min(r[5]+1, 51)):
                    active_cubes.add((x, y, z))
    else:
        for x in range(max(-50, r[0]), min(r[1]+1, 51)):
            for y in range(max(-50, r[2]), min(r[3]+1, 51)):
                for z in range(max(-50, r[4]), min(r[5]+1, 51)):
                    active_cubes -= {(x, y, z)}
print(len(active_cubes))

# Part 2 Brute force
active_cubes = set()
for i, (r, c) in enumerate(zip(ranges, commands)):
    if c == 'on':
        for x in range(r[0], r[1]+1):
            for y in range(r[2], r[3]+1):
                for z in range(r[4], r[5]+1):
                    active_cubes.add((x, y, z))
    else:
        for x in range(r[0], r[1]+1):
            for y in range(r[2], r[3]+1):
                for z in range(r[4], r[5]+1):
                    active_cubes -= {(x, y, z)}
    print(i+1, "-th command finished")
print(len(active_cubes))