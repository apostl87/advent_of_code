import sys, numpy as np, re
from aoclib import *
from collections import defaultdict

if "--test" in sys.argv or "-t" in sys.argv:
    test = True
else:
    test = False

input_file = (sys.argv[0].split(".")[0][1:])
input_file += "test.txt" if test==True else ".txt"
with open(input_file, "r") as f:
    input_ = f.read().strip()

length = len(input_)*4
binary = format(int(input_, 16), f'0>{length}b')

global versions   
def decode(binary):
    #print(binary)
    literal_values = []
    #while not all([x in ['', '0'] for x in binary]):
    versions.append(int(binary[:3], 2))
    typeid = int(binary[3:6], 2)
    idx = 6
    match typeid:
        case 4:
            group = '1'
            literal_value = ''
            while group[0] == '1':
                group = binary[idx:idx+5]
                literal_value += group[1:]
                idx += 5
            binary = binary[idx:]
            return binary, int(literal_value, 2)

        case _:
            lengthid = binary[idx]
            idx += 1
            values = []

            if lengthid == '0':
                numbits = int(binary[idx:idx+15], 2)
                idx += 15
                binary = binary[idx:]
                curr_length = len(binary)
                while curr_length - len(binary) < numbits:
                    binary, value = decode(binary)
                    values.append(value)

            elif lengthid == '1':
                numsubpackets = int(binary[idx:idx+11], 2)
                idx += 11
                binary = binary[idx:]
                for i in range(numsubpackets):
                    binary, value = decode(binary)
                    values.append(value)

            match typeid:
                case 0: return binary, sum(values)
                case 1: return binary, np.prod(values)
                case 2: return binary, min(values)
                case 3: return binary, max(values)
                case 5: return binary, int(values[0]>values[1])
                case 6: return binary, int(values[0]<values[1])
                case 7: return binary, int(values[0]==values[1])

            #subversions, literal_values = decode_subpackets(subpackets, numsubpackets)
            #return (*versions, subversions), (None, literal_values)
    
    #return tuple(versions), tuple(literal_values)

versions = []  
_, value = decode(binary)
print("Part 1:", sum(versions))
print("Part 2:", value)
        