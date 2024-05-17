import re
import numpy as np

def list2string(lst):
    result = ''
    for row in lst:
        for col in row:
            result += col
        result += '\n'
    return result

input_file = 'day19_input.txt'

with open(input_file, "r") as f:
    puzzle_input = f.read().strip()

workflows_raw, ratings_raw = puzzle_input.split("\n\n")

workflows = re.findall(r'(\w+){([^}]+)}', workflows_raw)
workflow = {}
for name, rules in workflows:
    conditions = re.findall(r'(\w+)([<>])(\w+):(\w+)', rules)
    final = rules.split(",")[-1]
    workflow[name] = [*conditions, final]
    #print(workflow[name])

ratings = [re.findall(r'(\w=\d+)', x) for x in ratings_raw.split("\n")]

total = 0
for rating in ratings:
    ratingdict = {}
    for r in rating:
        name, points = r.split("=")
        ratingdict[name] = points

    workflowname = 'in'
    i = 0
    while workflowname not in ['A', 'R']:
        if type(workflow[workflowname][i]) == str:
            workflowname = workflow[workflowname][i]
            i = 0
            continue
        
        #print(workflow[workflowname][i])
        name, op, points, res = workflow[workflowname][i]
        
        if eval(ratingdict[name]+op+points):
            workflowname = res
            i = 0
            continue
        else:
            i += 1
    if workflowname == 'A':
        total += sum([int(ratingdict[x]) for x in ratingdict])
print(total)
