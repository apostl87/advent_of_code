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

def interpret(x):
    try:
        return int(x)
    except:
        if x == '=':
            return -2
        if x == '-':
            return -1

def part1(input):
    numbers = []
    for line in input.split("\n"):
        n = 0
        for i, c in enumerate(line [::-1]):
            n += 5**i * interpret(c)
        numbers.append(n)
    result_decimal = sum(numbers)
    print(result_decimal)
    
    # Calculate SNUFA number
    remaining = result_decimal

    exp = 0
    result_snafu = defaultdict(int)
    while remaining or exp:
        if remaining < 0:
            break
        quotient_floor = remaining // (5**exp)
        if quotient_floor > 4:
            exp += 1
        else:
            result_snafu[exp] = quotient_floor
            exp -= 1
        
        remaining = result_decimal - sum([result_snafu[x]*5**x for x in result_snafu])
        
        print("test", remaining, exp, result_snafu)

    for k in sorted(result_snafu):
        if result_snafu[k] == 3:
            result_snafu[k] = '='
            result_snafu[k+1] += 1
        elif result_snafu[k] == 4:
            result_snafu[k] = '-' 
            result_snafu[k+1] += 1
        elif result_snafu[k] == 5:
            result_snafu[k] = '0' 
            result_snafu[k+1] += 1
        else:
            result_snafu[k] = result_snafu[k]
        
        # match qoutient_floor:
        #     case 4 | 3:
        #         result_snafu[exp+1] += 1
        #         if result_snafu[exp+1] > 2:
        #             exp += 1
        #             continue
        #         remaining -= 5**(exp+1)
        #     case 2 | 1 | 0:
        #         result_snafu[exp] = qoutient_floor
        #         remaining -= qoutient_floor*5**(exp)
        #     case _:
        #         exp += 1
        #         continue
        # exp -= 1
        # print(remaining)

    #result = sum([result_snafu[x] for x in sorted(result_snafu, reverse=True)])

    result_snafu = ''.join([str(result_snafu[x]) for x in range(max(result_snafu), -1, -1)])
    print(result_snafu)
    return result_snafu

part1(input_)
