import numpy as np

input_file = "day21test.txt"
input_file = "day21.txt"

with open(input_file, "r") as f:
    input_ = f.read().strip()

def monkey_number(monkeys, name):
    if type(monkeys[name]) in [int, float]:
        return monkeys[name]
    if len(monkeys[name]) == 1:
        return int(monkeys[name][0])
    else:
        x, y = monkey_number(monkeys, monkeys[name][0]), monkey_number(monkeys, monkeys[name][2])
        match monkeys[name][1]:
            case '+':
                return x+y
            case '-':
                return x-y
            case '/':
                return x/y
            case '*':
                return x*y

## Part 1
monkeys = dict()
for line in input_.split("\n"):
    name, job = line.split(": ")
    monkeys[name] = job.split()
result = monkey_number(monkeys, 'root')
print(int(result))


## Part 2
monkeys = dict()
for line in input_.split("\n"):
    name, job = line.split(": ")
    monkeys[name] = job.split()
monkeys['root'][1] = '-'

monkeys['humn'] = x1 = 1
y1 = monkey_number(monkeys, 'root')
monkeys['humn'] = x2 = 2
y2 = monkey_number(monkeys, 'root')

while abs(y2) > 0.1:
    k = (y1-y2)/(x1-x2)
    d = y1 - k*x1
    x1 = x2
    monkeys['humn']= x2 = -d/k
    y1 = y2
    y2 = monkey_number(monkeys, 'root')

print(int(monkeys['humn']))

# y1 = k x1 + d
# y2 = k x2 + d
# y1-y2 = k(x1-x2)
# k = (y1-y2)/(x1-x2)
# d = y1 - k x1

# 0 = k x3 + d
# x3 = -d / k