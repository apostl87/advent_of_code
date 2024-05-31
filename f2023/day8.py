import re
from math import lcm

with open("day8_input.txt", "r") as f:
    puzzle_input = f.read()

def part1(puzzle_input):
    segments = puzzle_input.split("\n\n")

    regex = r'[RL]'
    instructions = re.findall(regex, segments[0])

    regex = r'([A-Z]{3}) = \(([A-Z]{3}), ([A-Z]{3})\)'
    network = re.findall(regex, segments[-1])

    network_dict = dict()
    for element in network:
        network_dict[element[0]] = [element[1], element[2]]
    #print(network_dict)

    i = 0
    start_node = 'AAA'
    while True:
        instruction = instructions[i % len(instructions)] # i mod len(instructions)
        i += 1

        if instruction == 'L':
            start_node = network_dict[start_node][0]
        elif instruction == 'R':
            start_node = network_dict[start_node][1]
    
        if start_node == 'ZZZ':
            break

    return i

with open("day8_input.txt", "r") as f:
    puzzle_input = f.read()

def part2(puzzle_input):
    segments = puzzle_input.split("\n\n")

    regex = r'[RL]'
    instructions = re.findall(regex, segments[0])

    regex = r'([A-Z0-9]{3}) = \(([A-Z0-9]{3}), ([A-Z0-9]{3})\)'
    network = re.findall(regex, segments[-1])

    network_dict = dict()
    for element in network:
        network_dict[element[0]] = [element[1], element[2]]
    #print(network_dict)

    start_nodes = []
    for origin_node in network_dict:
        if origin_node[-1] == 'A':
            start_nodes.append(origin_node)

    print("number of nodes: ", len(start_nodes))

    steps = []
    for k in range(len(start_nodes)):
        i = 0
        while True:
            instruction = instructions[i % len(instructions)] # i mod len(instructions)
            i += 1

            if instruction == 'L':
                idx = 0
            elif instruction == 'R':
                idx = 1

            start_nodes[k] = network_dict[start_nodes[k]][idx]

            if start_nodes[k][-1] == 'Z':
                steps.append(i)
                break

    print(steps)
    return lcm(*steps)

print(part2(puzzle_input))

from itertools import cycle

def part2(puzzle_input):
    directions, connections = puzzle_input.split('\n\n')
    directions = [0 if d == 'L' else 1 for d in directions]
    graph = {}
    regex = r'(\w{3}) = \((\w{3}), (\w{3})\)'
    for node, left, right in re.findall(regex, connections):
        graph[node] = [left, right]

    starting_nodes = [node for node in graph if node[2] == 'A']
    cycles = []
    for node in starting_nodes:
        for steps, d in enumerate(cycle(directions), start=1):
            node = graph[node][d]
            if node[2] == 'Z':
                cycles.append(steps)
                break

    print(cycles)
    return lcm(*cycles)

print(part2(puzzle_input))
