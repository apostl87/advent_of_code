import sys, numpy as np

if "--test" in sys.argv or "-t" in sys.argv:
    test = True
else:
    test = False

input_file = (sys.argv[0].split(".")[0][1:])
input_file += "test.txt" if test==True else ".txt"

with open(input_file, "r") as f:
    input_ = f.read().strip()

binary_numbers = [x for x in input_.split("\n")]
n = len(binary_numbers)

def part1():
    gamma_rate = ['1' if sum_>=n/2 else '0' for sum_ in [sum([int(x[i]) for x in binary_numbers]) for i in range(len(binary_numbers[0]))]]
    epsilon_rate = ['1' if x == '0' else '0' for x in gamma_rate]
    gr_dec, er_dec = int(''.join(gamma_rate), 2), int(''.join(epsilon_rate), 2)
    return "Part 1", gr_dec*er_dec

print(part1())

def part2():
    numbers = binary_numbers.copy()
    i = 0
    while len(numbers) > 1:
        if ''.join([x[i] for x in numbers]).count('1') >= len(numbers)/2:
            [numbers.remove(x) for x in numbers.copy() if x[i]=='0']
        else:
            [numbers.remove(x) for x in numbers.copy() if x[i]=='1']
        i += 1
    oxygen_generator = numbers[0]

    numbers = binary_numbers.copy()
    i = 0
    while len(numbers) > 1:
        if ''.join([x[i] for x in numbers]).count('1') >= len(numbers)/2:
            [numbers.remove(x) for x in numbers.copy() if x[i]=='1']
        else:
            [numbers.remove(x) for x in numbers.copy() if x[i]=='0']
        i += 1
    co2scrubber = numbers[0]
    
    return "Part 2", int(oxygen_generator, 2) * int(co2scrubber, 2)

print(part2())