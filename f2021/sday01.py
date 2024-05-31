import sys, numpy as np

if "--test" in sys.argv or "-t" in sys.argv:
    test = True
else:
    test = False

input_file = (sys.argv[0].split(".")[0][1:])
input_file += "test.txt" if test==True else ".txt"

with open(input_file, "r") as f:
    input_ = f.read().strip()

input_ = [int(x) for x in input_.split("\n")]

# Part 1
result1 = sum([input_[i+1] > input_[i] for i in range(len(input_)-1)])
print(result1)

# Part 2
result2 = sum([sum(input_[i+1:i+4]) > sum(input_[i:i+3]) for i in range(len(input_)-2)])
print(result2)