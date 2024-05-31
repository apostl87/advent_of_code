import sys, numpy as np

if "--test" in sys.argv or "-t" in sys.argv:
    test = True
else:
    test = False

input_file = (sys.argv[0].split(".")[0][1:])
input_file += "test.txt" if test==True else ".txt"

with open(input_file, "r") as f:
    input_ = f.read().strip()

class Submarine(object):
    def __init__(self) -> None:
        self.depth = 0
        self.horizontal = 0
        self.aim = 0
    def move_part1(self, direction, steps):
        match direction:
            case 'forward':
                self.horizontal += steps
            case 'up':
                self.depth -= steps
            case 'down':
                self.depth += steps
    def move_part2(self, command, value):
        match command:
            case 'forward':
                self.horizontal += value
                self.depth += value*self.aim
            case 'up':
                self.aim -= value
            case 'down':
                self.aim += value

# Part 1
mySubmarine = Submarine()
for line in input_.split("\n"):
    direction, steps = line.split()
    mySubmarine.move_part1(direction, int(steps))
print(mySubmarine.depth * mySubmarine.horizontal)

# Part 2
mySubmarine = Submarine()
for line in input_.split("\n"):
    command, value = line.split()
    mySubmarine.move_part2(command, int(value))
print(mySubmarine.depth * mySubmarine.horizontal)