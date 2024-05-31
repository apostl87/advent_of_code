import sys, numpy as np, re
from aoclib import *
from collections import defaultdict

if "--test" in sys.argv or "-t" in sys.argv:
    test = True
else:
    test = False
if test:
    input_ = "16,1,2,0,4,2,7,1,2,14"
else:
    input_file = (sys.argv[0].split(".")[0][1:])
    input_file += "test.txt" if test==True else ".txt"
    with open(input_file, "r") as f:
        input_ = f.read().strip()

positions = [int(x) for x in input_.split(",")]

# Part 1
fuel_consumption = np.infty
for i in range(min(positions), max(positions)+1):
    val = sum([abs(i - x) for x in positions])
    if fuel_consumption > val:
        fuel_consumption = val
    else:
        break
print(fuel_consumption)

# Part 2
fuel_consumption = np.infty
for i in range(min(positions), max(positions)+1):
    val = sum([sum(range(abs(i - x) + 1)) for x in positions])
    if fuel_consumption > val:
        fuel_consumption = val
    else:
        break
print(fuel_consumption)