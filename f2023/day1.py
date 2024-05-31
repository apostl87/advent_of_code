import numpy as np
import re

spelled_out_numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

exp = ""
for word in spelled_out_numbers:
    if exp != "":
        exp += '|'
    exp += word

p = re.compile(exp+r'|\d{1}')

print(exp+r'|\d{1}')

result = 0

with open("day1_input.txt", "r") as f:

    line = f.readline()
    while line != "":

        numbers = p.findall(line) # does not work correctly with regular expressions for overlapping number strings, e.g. "oneight"
        if not numbers[0].isnumeric():
            numbers[0] = str(spelled_out_numbers.index(numbers[0]) + 1)
        if not numbers[-1].isnumeric():
            numbers[-1] = str(spelled_out_numbers.index(numbers[-1]) + 1)

        number = eval(numbers[0]+numbers[-1])
        print(number)
        
        result += number

        line = f.readline()
        #print(line)

print(result)