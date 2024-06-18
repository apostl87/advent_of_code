import re, json
from collections import defaultdict

input = open("8.input").read().strip()
#input = open("8.example").read().strip()

def get_children(node, n_c):
    global desc
    global sum_metadata
    for i in range(n_c):
        n_c = desc.pop(0)
        n_m = desc.pop(0)
        node['children'].append(defaultdict(list))
        if n_c > 0:
            get_children(node['children'][i], n_c)
        
        for j in range(n_m):
            entry = desc.pop(0)
            sum_metadata += entry
            node['children'][i]['metadata'].append(entry)
    # print(psuedoroot)

# Part 1
global desc, sum_metadata
desc = [int(x) for x in input.split()]
pseudoroot = defaultdict(list)

sum_metadata = 0
get_children(pseudoroot, 1)
root = pseudoroot['children'][0]
# print(json.dumps(root, indent=2))
print("Part 1:", sum_metadata)

# Part 2
def get_value(node):
    if 'children' in node:
        return sum([get_value(node['children'][i-1]) for i in node['metadata'] if -1 < i-1 < len(node['children'])])
    else:
        return sum(node['metadata'])

print("Part 2:", get_value(root))
