import sys, numpy as np, re
from aoclib import *
from collections import defaultdict

if "--test" in sys.argv or "-t" in sys.argv:
    test = True
else:
    test = False
if test:
    input_ = "3,4,3,1,2"
else:
    input_file = (sys.argv[0].split(".")[0][1:])
    input_file += "test.txt" if test==True else ".txt"
    with open(input_file, "r") as f:
        input_ = f.read().strip()

timers = [int(x) for x in input_.split(",")]


# Part 1
def time_evolve(timers, n_steps):
    for i in range(n_steps):
        if i % 10 == 0: print(i)
        timers = [x-1 if x > 0 else 6 for x in timers] + [8]*timers.count(0)
    return timers

res1 = time_evolve(timers, 80)
print(len(res1))


# Part 2
def time_evolve_stacked(timers, n_steps):
    counts = {i: timers.count(i) for i in range(9) for x in timers}
    for i in range(n_steps):
        #if i % 10 == 0: print(i)
        count_zero = counts[0]
        for idx in range(0, 8):
            counts[idx] = counts[idx+1]
        counts[6] += count_zero
        counts[8] = count_zero
    return sum(counts.values())

res2 = time_evolve_stacked(timers, 256)
print(res2)