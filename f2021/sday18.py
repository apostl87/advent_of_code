import sys, numpy as np, re, copy
from aoclib import *
from collections import defaultdict
from aoclib import string2list

if "--test" in sys.argv or "-t" in sys.argv:
    test = True
else:
    test = False

input_file = (sys.argv[0].split(".")[0][1:])
input_file += "test.txt" if test==True else ".txt"
with open(input_file, "r") as f:
    input_ = f.read().strip()

def indexer(sfnumber, dict_ = dict(), praeindices = ''):
    left, right = sfnumber
    if type(left) == list:
        dict_ |= indexer(left, dict_, praeindices + '0')
    else:
        dict_[praeindices + '0'] = left
    if type(right) == list:
        dict_ |= indexer(right, dict_, praeindices + '1')
    else:
        dict_[praeindices + '1'] = right
    return dict_

def indexerdict2list(dict_):
    list_ = []
    for key, value in dict_.items():
        list_ += [key, value] 
    return list_

def right(list_, key_):
    return list_[list_.index(key_) + 1]

def left(list_, key_):
    return list_[list_.index(key_) - 1]

def explode(list_):
    for i in range(0, len(list_), 2):
        if len(list_[i]) > 4:
            if i > 0:
                list_[i-1] += list_[i+1]
            if i+3 < len(list_)-1:
                list_[i+5] += list_[i+3]
            new_key = list_[i][:-1]
            for _ in range(4):
                list_.pop(i)
            list_.insert(i, 0)
            list_.insert(i, new_key)
            return True
    return False

def split(list_):
    for i in range(1, len(list_), 2):
        if list_[i] >= 10:
            key_, value = list_.pop(i-1), list_.pop(i-1)
            splitvalue1 = value//2
            splitvalue2 = splitvalue1 + value%2
            list_.insert(i-1, splitvalue2)
            list_.insert(i-1, key_ + '1')
            list_.insert(i-1, splitvalue1)
            list_.insert(i-1, key_ + '0')
            return True
    return False

def reduce(list_):
    while True:
        if explode(list_):
            continue
        if not split(list_):
            break

def add(xlist, ylist):
    if not xlist or not ylist:
        return xlist + ylist
    for i in range(0, len(xlist), 2):
        xlist[i] = '0' + xlist[i]
    for i in range(0, len(ylist), 2):
        ylist[i] = '1' + ylist[i]
    return xlist + ylist

def convert2ordinarylist(list_):
    maxdepth = max(len(list_[i]) for i in range(0, len(list_), 2))
    ordinary_list = []
    for _ in range(maxdepth):
        ordinary_list = [copy.deepcopy(ordinary_list), copy.deepcopy(ordinary_list)]
    #print(ordinary_list)
    for i in range(0, len(list_), 2):
        indexstring = list_[i]
        #print(indexstring)
        sublist = ordinary_list.copy()
        #print(sublist, 'before')
        while len(indexstring) > 1:
            sublist = sublist[int(indexstring[0])]
            indexstring = indexstring[1:]
        #print(sublist)
        sublist[int(indexstring[0])] = list_[i+1]
        #print(ordinary_list)
    return ordinary_list

def magnitude(list_):
    left, right = list_
    if type(left) == list:
        left = magnitude(left)
    if type(right) == list:
        right = magnitude(right)
    return 3*left + 2*right

# Part 1
snailfish_numbers = input_.splitlines()
snailfish_numbers = [eval(x) for x in snailfish_numbers]
#print(snailfish_numbers)

resulting_number = []
while snailfish_numbers:
    #print(resulting_number)
    resulting_number = add(resulting_number, indexerdict2list(indexer(snailfish_numbers.pop(0), dict())))
    #print(resulting_number)
    reduce(resulting_number)
    #print(resulting_number)
    print(convert2ordinarylist(resulting_number))
    #print(snailfish_number)

#print(resulting_number)
print(resulting_number_ordinary := convert2ordinarylist(resulting_number))
print("Part 1: Magnitude:", magnitude(resulting_number_ordinary))

# Part 2
snailfish_numbers = input_.splitlines()
snailfish_numbers = [eval(x) for x in snailfish_numbers]

max_magnitude = 0
for sn1 in snailfish_numbers:
    for sn2 in snailfish_numbers:
        result = add(indexerdict2list(indexer(sn1, dict())), indexerdict2list(indexer(sn2, dict())))
        reduce(result)
        x = convert2ordinarylist(result)
        max_magnitude = max(magnitude(x), max_magnitude)
print("Part 2: Max Magnitude:", max_magnitude)

quit()


a = [[[[[9,8],1],2],3],4]
dict_indices = indexer(a)
list_indices = indexerdict2list(dict_indices)

print(list_indices)
reduce(list_indices)
print(list_indices)

list_indices = add(list_indices, list_indices.copy())
print(list_indices)

reduce(list_indices)
print(list_indices)


