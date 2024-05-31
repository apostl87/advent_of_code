import re
import time

with open("day6_input.txt", "r") as f:
    input_file = f.read()

def part1(input_file):
    line1, line2 = input_file.split("\n")
    regex = r'\d+'
    times = re.findall(regex, line1)
    records = re.findall(regex, line2)

    result = 1
    for time, record in zip(map(int, times), map(int, records)):
        counter = 0
        for charging_time in range(1, time):
            distance = (time-charging_time)*charging_time
            if distance > record:
                counter += 1
            elif counter:
                break
        result *= counter

    return result

def part2(input_file):
    line1, line2 = input_file.split("\n")
    regex = r'\d+'
    time_fragments = re.findall(regex, line1)
    record_fragments = re.findall(regex, line2)

    time = ""
    for f in time_fragments:
        time += f
    record = ""
    for r in record_fragments:
        record += r

    time = int(time)
    record = int(record)

    counter = 0
    for charging_time in range(1, time):
            distance = (time-charging_time)*charging_time
            if distance > record:
                counter += 1
            elif counter:
                break
    
    return counter

t = time.time()
print(part1(input_file))
print(time.time()-t)
print(part2(input_file))