import numpy as np
import re
import copy
from operator import mul

with open("day3_input.txt", "r") as f:
    lines = f.readlines()

p2 = re.compile(r'\d+')

# Part 1

p1 = re.compile(r'[^0-9^.^\n]')

symbol_positions_previous = []
number_positions_previous = []
numbers_previous = []

symbol_positions_now = []
number_positions_now = []
numbers_now = []

result = 0

for i, line in enumerate(lines):
    #print(line)

    symbol_positions_previous = copy.copy(symbol_positions_now)
    symbol_positions_now = []
    number_positions_previous = copy.copy(number_positions_now)
    number_positions_now = []
    numbers_previous = copy.copy(numbers_now)

    symbol_matches = p1.finditer(line)
    for symbol_match in symbol_matches:
        symbol_positions_now.append((symbol_match.start()))
    
    number_matches = p2.finditer(line)
    for number_match in number_matches:
        number_positions_now.append((number_match.start(), number_match.end()))

    numbers_now = p2.findall(line)

    # check numbers of previous row
    for i, number_previous in enumerate(numbers_previous):
        number_is_eligible = False
        number_position = number_positions_previous[i]

        for symbol_position in symbol_positions_now:
            if (symbol_position >= number_position[0]-1) and (symbol_position <= number_position[1]):
                number_is_eligible = True
                result += eval(number_previous)
                #print("case 3 ", number_previous)
                break

    # check numbers of this row
    to_check_ids = []
    for i, number_now in enumerate(numbers_now):
        number_is_eligible = False
        number_position = number_positions_now[i]

        for symbol_position in symbol_positions_now:
            if (symbol_position == number_position[0]-1) or (symbol_position == number_position[1]):
                number_is_eligible = True
                result += eval(number_now)
                #print("case 1 ", number_now)
                break
        
        if number_is_eligible:
            continue

        for symbol_position in symbol_positions_previous:
            if (symbol_position >= number_position[0]-1) and (symbol_position <= number_position[1]):
                number_is_eligible = True
                result += eval(number_now)
                #print("case 2 ", number_now)
                break

        if not number_is_eligible:
            to_check_ids.append(i)

    tmp1 = []
    tmp2 = []
    for id in to_check_ids:
        tmp1.append(numbers_now[id])
        tmp2.append(number_positions_now[id])

    numbers_now = copy.copy(tmp1)
    number_positions_now = copy.copy(tmp2)
 
print(result)


# Part 2

def get_adjacent_numbers(yx_position, lines):
    out = []
    try:
        line = lines[yx_position[0]-1]
        number_matches = p2.finditer(line)
        for number_match in number_matches:
            if (yx_position[1] >= number_match.start()-1) and (yx_position[1] <= number_match.end()):
                out.append(eval(number_match.group()))
    except:
        pass
    
    line = lines[yx_position[0]]
    number_matches = p2.finditer(line)
    for number_match in number_matches:
            if (yx_position[1] == number_position[0]-1) or (yx_position == number_position[1]):
                out.append(eval(number_match.group()))
    
    try:
        line = lines[yx_position[0]+1]
        number_matches = p2.finditer(line)
        for number_match in number_matches:
            if (yx_position[1] >= number_match.start()-1) and (yx_position[1] <= number_match.end()):
                out.append(eval(number_match.group()))
    except:
        pass

    return out
    

p3 = re.compile(r'[*]')
result = 0

for i, line in enumerate(lines):
    star_matches = p3.finditer(line)
    for star_match in star_matches:
        star_position = (i, star_match.start())
        adjacent_numbers = get_adjacent_numbers(star_position, lines)
        if len(adjacent_numbers) == 2:
            result += adjacent_numbers[0]*adjacent_numbers[1]

print(result)

def part2(puzzle_input):
    lines = puzzle_input.split('\n')

    gear_regex = r'\*'
    gears = dict()
    for i, line in enumerate(lines):
        for m in re.finditer(gear_regex, line):
            gears[(i, m.start())] = []

    number_regex = r'\d+'
    for i, line in enumerate(lines):
        for m in re.finditer(number_regex, line):
            for r in range(i-1, i+2):
                for c in range(m.start()-1, m.end()+1):
                    if (r, c) in gears:
                        gears[(r, c)].append(int(m.group()))

    gear_ratio_sum = 0
    for nums in gears.values():
        if len(nums) == 2:
            gear_ratio_sum += mul(*nums)

    return gear_ratio_sum