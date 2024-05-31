import copy

input_file = "day20.txt"
with open(input_file, "r") as f:
    input_ = f.read().strip()
#input_ = "Test"

### Part 1
class Number(object):
    def __init__(self, value):
        self.value = value

def part1():
    if input_ == "Test":
        original_list = [1, 2, -3, 3, -2, 0, 4]
    else:
        original_list = [int(x) for x in input_.split("\n")]
   
    # solution1: does not work with duplicates
    new_list = copy.deepcopy(original_list)
    n = len(new_list)
    for value in original_list:
        idx = new_list.index(value)
        new_list.remove(value)
        ins = idx + value if idx + value <= n-1 else (idx + value)%(n-1)
        ins = (idx + value)%(n-1)
        new_list.insert(ins, value)
        #print(new_list)
    result = 0
    for i in [1000, 2000, 3000]:
        idx = i + new_list.index(0)
        result += new_list[idx%n]
        #print(new_list[idx%n])
    # end solution1

def mix(original_list, new_list, zero):
    n = len(new_list)
    for item in original_list:
        value = item.value
        idx = new_list.index(item)
        new_list.remove(item)
        ins = (idx + value)%(n-1)
        new_list.insert(ins, item)
        #print(new_list)
    result = 0
    for i in [1000, 2000, 3000]:
        idx = i + new_list.index(zero)
        result += new_list[idx%n].value
        #print(new_list[idx%n])

    return result, new_list

# Part 1
new_list = []
for item in input_.split("\n"):
    n = Number(int(item))
    new_list.append(n)
    if item == '0':
        zero = n
res, nl = mix(copy.copy(new_list), new_list, zero)
print(res)

# Part 2
new_list = []
for item in input_.split("\n"):
    n = Number(int(item)*811589153)
    new_list.append(n)
    if item == '0':
        zero = n
copy_of_list = copy.copy(new_list)
for i in range(10):
    res, new_list = mix(copy_of_list, new_list, zero)
print(res)

