from collections import defaultdict

input_ = open("7.in").read().strip()

# Part 1
towers = defaultdict(list)
program_weights = dict()
for line in input_.split("\n"):
    parts = line.split()
    program_weights[parts[0]] = int(parts[1][1:-1])
    
    if len(parts) > 2:
        for p in parts[3:]:
            p = p.replace(",", "")
            towers[parts[0]].append(p)

programsondiscs = set.union(*[set(towers[x]) for x in towers])
bottom = (set(program_weights.keys()) - programsondiscs).pop()
print(bottom)

# Part 2
def get_weight(node):
    weight = program_weights[node]
    if node in towers:
        ondisc = towers[node]
        for o in ondisc:
            weight += get_weight(o)
    return weight


def getIndexAndDifference(valuelist):
    for i in range(len(valuelist)):
        if valuelist[i] != valuelist[(i+1)%len(valuelist)] and valuelist[(i+2)%len(valuelist)]!= valuelist[i]:
            return [i, valuelist[i] - valuelist[(i+1)%len(valuelist)]]
    return [-1, 0]

idx_and_diff = []
current = bottom
while True:
    w = [0]*len(towers[current])
    
    for i, node in enumerate(towers[current]):
        w[i] = get_weight(node)
       
    print(current, towers[current]) 
    print(w)
    idx_and_diff.append(getIndexAndDifference(w))
    
    if idx_and_diff[-1][0] == -1:
        print("Found the cause of the imbalance")
        print(current, "should weigh", program_weights[current] - idx_and_diff[-2][1])
        break
    else:
        print("going right")
        current = towers[current][idx_and_diff[-1][0]]
    