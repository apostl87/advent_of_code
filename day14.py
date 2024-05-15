input_file = 'day14_input.txt'

# To match the format of input files for the Basilisk.
with open(input_file, "r") as f:
    puzzle_input = f.read().strip()

rows = [[*x] for x in puzzle_input.split("\n")]

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