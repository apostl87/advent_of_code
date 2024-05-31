import re
from collections import defaultdict

input_file = 'day15_input.txt'

with open(input_file, "r") as f:
    puzzle_input = f.read().strip()


## Part 1
steps = puzzle_input.split(",")
values = []
for step in steps:
    value = 0
    for char in step:
        value += ord(char)
        value *= 17
        value %= 256
    values.append(value)
result = sum(values)
print(result)


## Part 2
steps = puzzle_input.split(",")
boxes = {}
for step in steps:
    value = 0
    chain = re.findall("[a-z]*", step)[0]
    for char in chain:
        value += ord(char)
        value *= 17
        value %= 256

    if '-' in step:
        if value in boxes:
            logical = [lens[:len(chain)]==chain for lens in boxes[value]]
            if any(logical):
                boxes[value].remove(boxes[value][logical.index(True)])
                if boxes[value] == []:
                    boxes.pop(value)
    else:
        if value in boxes:
            logical = [lens[:len(chain)]==chain for lens in boxes[value]]
            if any(logical):
                boxes[value][logical.index(True)] = step
            else:
                boxes[value].append(step)
        else:
            boxes[value] = [step]

focusing_power = 0
for value in boxes:
    for i, lens in enumerate(boxes[value]):
        focusing_power += (1+value)*(1+i)*int(lens[-1])

print(focusing_power)



print([(v:=0) or [v:=(v+ord(c))*17%256 for c in s] and v for s in puzzle_input.split(',')])