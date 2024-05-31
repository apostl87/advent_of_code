import os, sys
from collections import defaultdict

test_input = False

if test_input:
    input_file = "day25test.txt"
else:
    input_file = "day25.txt"

if os.getcwd().split('/')[-1] != "f2022":
    input_file = 'f2022/' + input_file

with open(input_file, "r") as f:
    input_ = f.read().strip()

def part1(input):
    digits = {'2': 2, '1': 1, '0': 0, '-': -1, '=': -2}
    reverse_digits = {5: '0', 4: '-', 3: '=', 2: '2', 1: '1', 0: '0'}
    result_decimal = sum([digits[c]*5**i for line in input_.split("\n") for i, c in enumerate(line.strip() [::-1])])
    print(result_decimal)
    
    transfer = 0
    x = result_decimal
    snafu = []
    while x:
        r = x % 5 + transfer
        transfer = 1 if r in [3, 4, 5] else 0
        snafu.append(reverse_digits[r])
        x //= 5
    
    result = ''.join(reversed(snafu))
    print(result)

    return result
  
part1(input_)