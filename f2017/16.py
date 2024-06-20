import string, copy

inp = open("16.in").read().strip()

def dance(line):
  line = copy.deepcopy(line)
  for move in inp.split(','):
    if move[0] == 's':
        x = -int(move[1:])
        line = line[x:] + line[:x]
    elif move[0] == 'x':
        x, y = [int(x) for x in move[1:].split('/')]
        sav = line[x]
        line[x] = line[y]
        line[y] = sav
    else:
        p1, p2 = move[1:].split('/')
        x, y = line.index(p1), line.index(p2)
        sav = line[x]
        line[x] = line[y]
        line[y] = sav
  return line


# Initial
known = []
programs = list(string.ascii_lowercase[:16])
known.append(programs)  

# Part 1: One cycle
programs = dance(programs)
known.append(programs)
print(''.join(programs))

# Part 2: 1_000_000_000 cycles
i = 1
find_cycle_length = True
while i < 1_000_000_000:
    i += 1
    programs = dance(programs)
    if find_cycle_length:
        if programs in known:
            cycle_length = i - known.index(programs)
            find_cycle_length = False
            i += ((1_000_000_000 - i) // cycle_length) * cycle_length
        else:
            known.append(programs)
print(''.join(programs))