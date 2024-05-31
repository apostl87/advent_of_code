import re
from collections import deque
from itertools import count
import math

input_file = 'day20_input.txt'

with open(input_file, "r") as f:
    puzzle_input = f.read().strip()

configuration = re.findall(r'([%&]*)(\w+) -> ([\w ,]*)', puzzle_input)

# Initialization
modules = {}
for type, name, destinations in configuration:
    modules[name] = {}
    modules[name]['type'] = type
    modules[name]['destinations'] = [x.strip() for x in destinations.split(",")]
for name in modules:
    if modules[name]['type'] == '%': modules[name]['state'] = False
    if modules[name]['type'] == '&':
        modules[name]['inputstates'] = {}
        for m in modules:
            if name in modules[m]['destinations']:
                modules[name]['inputstates'][m] = False

#[print(x, modules[x]) for x in modules]

n_low, n_high = 0, 0
for k in range(1000):
    # Button push
    queue = [('button', 'broadcaster', False)]
    while queue:
        sender, name, pulse = queue.pop(0)
        if pulse:  n_high += 1
        else:      n_low += 1
        if name == 'rx': # output module
            if not pulse:
                print("Part 2: Button presses:", k+1)
            continue
        mp = modules[name] # module properties
        if mp['type'] == '':
            [queue.append((name, x, pulse)) for x in mp['destinations']]
        if mp['type'] == '%':
            if not pulse:
                modules[name]['state'] = not modules[name]['state']
                [queue.append((name, x, modules[name]['state'])) for x in mp['destinations']]
        if mp['type'] == '&':
            modules[name]['inputstates'][sender] = pulse
            if all(modules[name]['inputstates'].values()):
                new_pulse = False
            else:
                new_pulse = True
            [queue.append((name, x, new_pulse)) for x in mp['destinations']]

print("Low pulses: ", n_low)
print("High pulses: ", n_high)
print("Product: ", n_low*n_high)
print("Sum: ", n_low+n_high)

### Part 2
def part2(puzzle_input):
    graph = {}
    flip_flop = {}
    memory = {}
    for line in puzzle_input.split('\n'):
        source, destinations = line.split(' -> ')
        destinations = destinations.split(', ')
        graph[source.lstrip('%&')] = destinations
        if source.startswith('%'):
            flip_flop[source[1:]] = 0   # each flip flip is off (0) by default
        elif source.startswith('&'):
            memory[source[1:]] = {}

    for conjunction in memory.keys():   # get source modules for conjunctions 
        for source, destinatons in graph.items():
            if conjunction in destinatons:
                memory[conjunction][source] = 0   # initialize memory at low (0)

    final_layer = [m1 for m1 in graph if 'rx' in graph[m1]]
    assert len(final_layer) == 1, "Assumption #1: There is only 1 module pointing to rx"
    assert final_layer[0] in memory, "Assumption #2: The final module before rx is a conjunction"

    semi_final_layer = set(module for module in graph if final_layer[0] in graph[module])
    cycle_lengths = []  # Assumption #3: The modules on semi_final_layer signal high in regular intervals / cycles
    
    for button_push in count(1):
        queue = deque([('broadcaster', in_module, 0) for in_module in graph['broadcaster']])
        while queue:
            out_module, in_module, signal = queue.popleft()

            case = None
            if in_module in flip_flop and signal == 0:
                flip_flop[in_module] = 1 - flip_flop[in_module]
                out_signal = flip_flop[in_module]
                case = 1

            elif in_module in memory:
                memory[in_module][out_module] = signal
                out_signal = 1 if 0 in memory[in_module].values() else 0
                case = 2
            
            if in_module in semi_final_layer and out_signal == 1:
                    cycle_lengths.append(button_push)
                    semi_final_layer.remove(in_module)

            if not case:   # no output
                continue
            
            queue.extend([(in_module, nxt, out_signal) for nxt in graph[in_module]])

        if not semi_final_layer:
            break

    return math.lcm(*cycle_lengths)

print('Part 2:', part2(puzzle_input))


# Initialization
modules = {}
for type, name, destinations in configuration:
    modules[name] = {}
    modules[name]['type'] = type
    modules[name]['destinations'] = [x.strip() for x in destinations.split(",")]
for name in modules:
    if modules[name]['type'] == '%': modules[name]['state'] = False
    if modules[name]['type'] == '&':
        modules[name]['inputstates'] = {}
        for m in modules:
            if name in modules[m]['destinations']:
                modules[name]['inputstates'][m] = False

