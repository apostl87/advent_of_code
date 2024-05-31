import sys, numpy as np, re
from aoclib import *
from collections import defaultdict

if "--test" in sys.argv or "-t" in sys.argv:
    test = True
else:
    test = False

input_file = (sys.argv[0].split(".")[0][1:])
input_file += "test.txt" if test==True else ".txt"
with open(input_file, "r") as f:
    input_ = f.read().strip()

polymer_start, insertions = input_.split("\n\n")
dots = []

rules = dict()
for line in insertions.splitlines():
    (pair, element) = line.split(' -> ') 
    rules[pair] = element

# Part 1
def grow(polymer, rules, n_steps):
    for i in range(n_steps):
        insertions = ''
        for j in range(len(polymer)-1):
            pair = ''.join(polymer[j:j+2])
            insertions += rules[pair]
        polymer = list(polymer)
        for k, element in enumerate(list(insertions)):
            polymer.insert(2*k+1, element)
        print("Step", i)
    return polymer

polymer_result1 = grow(polymer_start, rules, 10)
letters = set(polymer_result1) 
max_ = max([polymer_result1.count(x) for x in letters])
min_ = min([polymer_result1.count(x) for x in letters])            
print("Part 1:", max_ - min_)

# Part 2
def stats(polymer, rules, n_steps):
    letters = defaultdict(int)
    pairs = defaultdict(int)

    for letter in polymer:
        letters[letter] += 1
    for i in range(len(polymer) - 1):
        pairs[polymer[i] + polymer[i+1]] += 1

    for i in range(n_steps):
        new_pairs = defaultdict(int)
        for pair in pairs:
            letters[rules[pair]] += pairs[pair]
            new_pairs[pair[0] + rules[pair]] += pairs[pair]
            new_pairs[rules[pair] + pair[1]] += pairs[pair]
        pairs = new_pairs
        print("Step", i+1, "complete.")

    return max(letters.values()) - min(letters.values())

polymer_result2 = stats(polymer_start, rules, 40)
# letters = set(polymer_result2) 
# max_ = max([polymer_result2.count(x) for x in letters])
# min_ = min([polymer_result2.count(x) for x in letters])            
print("Part 2:", polymer_result2)