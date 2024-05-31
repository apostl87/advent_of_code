import copy

input_file = 'day14_input.txt'

# To match the format of input files for the Basilisk.
with open(input_file, "r") as f:
    puzzle_input = f.read().strip()

rows = [[*x] for x in puzzle_input.split("\n")]

def visual(rows):
    output = ""
    for i, row in enumerate(rows):
        for c in row:
            output += c
        output += "\n"
    return output

def north_tilt(rows):
    for i, row in enumerate(rows[1:], start=1):
        for j, tile in enumerate(row):
            if tile == 'O':
                ii = i
                while ii > 0:
                    if rows[ii-1][j] == '.':
                        rows[ii-1][j] = 'O'
                        rows[ii][j] = '.'
                        ii -= 1
                    else:
                        break
    return rows

def west_tilt(rows):
    for i, row in enumerate(rows):
        for j, tile in enumerate(row):
            if tile == 'O':
                jj = j
                while jj > 0:
                    if rows[i][jj-1] == '.':
                        rows[i][jj-1] = 'O'
                        rows[i][jj] = '.'
                        jj -= 1
                    else:
                        break
    return rows

def south_tilt(rows):
    rows.reverse()
    for i, row in enumerate(rows[1:], start=1):
        for j, tile in enumerate(row):
            if tile == 'O':
                ii = i
                while ii > 0:
                    if rows[ii-1][j] == '.':
                        rows[ii-1][j] = 'O'
                        rows[ii][j] = '.'
                        ii -= 1
                    else:
                        break
    rows.reverse()
    return rows

def east_tilt(rows):
    for i in range(len(rows)):
        rows[i].reverse()
    for i, row in enumerate(rows):
        for j, tile in enumerate(row):
            if tile == 'O':
                jj = j
                while jj > 0:
                    if rows[i][jj-1] == '.':
                        rows[i][jj-1] = 'O'
                        rows[i][jj] = '.'
                        jj -= 1
                    else:
                        break
    for i in range(len(rows)):
        rows[i].reverse()
    return rows

## Part 1

north_tilt(rows)

load = 0
output = ""
for i, row in enumerate(rows):
    load += row.count('O')*(len(rows)-i)
    for c in row:
        output += c
    output += "\n"

print(output)
print(load)

## Part 2

storage = []
k = 0
while True and k <= 1e9:
    storage.append(copy.deepcopy(rows))
    rows = north_tilt(rows)
    #print('north\n',visual(rows))
    rows = west_tilt(rows)
    #print('west\n',visual(rows))
    rows = south_tilt(rows)
    #print('south\n',visual(rows))
    rows = east_tilt(rows)
    #print('east\n',visual(rows))
    if rows in storage:
        break
    k+=1

try:
    period_start = storage.index(rows)
except:
    period_start = 0

period_length = len(storage) - period_start

rows = storage[(int(1e9)-period_start) % period_length + period_start]

load = 0
for i, row in enumerate(rows):
    load += row.count('O')*(len(rows)-i)

print(visual(rows))
print(load)