from collections import defaultdict

input_ = open("8.in").read().strip()

# Part 1 and 2
registers = defaultdict(int)
max_all = 0
for line in input_.split("\n"):
    modify, action, value, _, condoperand, condop, condvalue = line.split()
    
    match condop:
        case '==':
            condfunc = lambda x, y: x == y
        case '<=':
            condfunc = lambda x, y: x <= y
        case '>=':
            condfunc = lambda x, y: x >= y
        case '!=':
            condfunc = lambda x, y: x != y
        case '<':
            condfunc = lambda x, y: x < y
        case '>':
            condfunc = lambda x, y: x > y
        case _default:
            raise Exception("Invalid condition operator")

    if condfunc(registers[condoperand], int(condvalue)):
        match action:
            case 'inc':
                registers[modify] += int(value)
            case 'dec':
                registers[modify] -= int(value)
            case _default:
                raise Exception("Invalid action")
            
    max_all = max(max_all, max(registers.values()))
    
print("Part 1:", max(registers.values()))
print("Part 2:", max_all)