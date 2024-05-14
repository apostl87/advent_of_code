import numpy as np
import re

with open("day2_input.txt", "r") as f:
    lines = f.readlines()

p1 = re.compile(r'\d+')
p2 = re.compile("red|green|blue")

# Part 1

colors2limits = {
    "red": 12,
    "green": 13,
    "blue": 14
}

result = 0

for line in lines:
    parts = line.split(':')
    id = eval(p1.search(parts[0]).group())

    subsets = parts[-1].split(';')

    impossible = False
    for subset in subsets:
        if impossible:
            break
        numbers = p1.findall(subset)
        colors = p2.findall(subset) 

        for number, color in zip(numbers, colors):
            if eval(number) > colors2limits[color]:
                impossible = True
                break
    
    if not impossible:
        result += id

print(result)

# Part 2

colors = ['red', 'green', 'blue']

result = 0

for line in lines:
    parts = line.split(':')
    subsets = parts[-1].split(';')
    maxima = {
        'red': 0, 
        'green': 0, 
        'blue': 0
        }

    for subset in subsets:
        numbers = p1.findall(subset)
        colors = p2.findall(subset) 

        for number, color in zip(numbers, colors):
            maxima[color] = max(maxima[color],eval(number))

    power = 1
    for max_value in maxima.values():
        power *= max_value
    
    result += power

print(result)