
test_input = False
if test_input:
    input_file = "day24test.txt"
else:
    input_file = "day24.txt"

with open(input_file, "r") as f:
    input_ = f.read().strip()

def list2string(lst):
    result = ''
    for row in lst:
        for col in row:
            match len(col):
                case 0:
                    result += '.'
                case 1:
                    result += col[0]
                case _:
                    result += str(len(col))
        result += '\n'
    return result

blizzards = []
for y, line in enumerate(input_.split("\n")):
    for x, char in enumerate(line):
        print(char)

blizzards = [[[char] if char in ['<', '>', '^', 'v'] else [] for char in line] for line in input_.split("\n")]
m, n = len(blizzards), len(blizzards[0])

print(list2string(blizzards))

dir2coords = {'<': (0, -1), '>': (0, 1), '^': (-1, 0), 'v': (1, 0)}

time = 0
y_end, x_end = m-2, n-2

actor_positions = [(0, 1)]
while True:
    new_blizzards = [[[] for x in range(n)] for y in range(m)]
    
    for y, line in enumerate(blizzards):
        for x, blizz in enumerate(line):
            for b in blizz:
                delta_y, delta_x = dir2coords[b]
                y_new = y + delta_y
                x_new = x + delta_x
                if y_new < 1: y_new = m-2
                if y_new > m-2: y_new = 1
                if x_new < 1: x_new = n-2
                if x_new > n-2: x_new = 1
                new_blizzards[y_new][x_new].append(b)

    blizzards = new_blizzards

    time += 1
    #print(list2string(blizzards))
    print(time)

    new_actor_positions = []
    for pos in actor_positions:
        candidates = [(pos[0]+y, pos[1]+x) for y, x in dir2coords.values()] + [(pos[0], pos[1])]
        valid = [y > 0 and y < m-1 and x > 0 and x < n-1 for y, x in candidates]
        for valid_, candidate in zip(valid, candidates):
            if not valid_:
                continue
            if not new_blizzards[candidate[0]][candidate[1]]:
                new_actor_positions.append(candidate)
    
    actor_positions = new_actor_positions
    actor_positions_set = set(actor_positions)

    if (y_end, x_end) in actor_positions_set:
        print("Part 1:", time+1)
        break

    if time ==  16:
        print(list2string(blizzards))
        print([x if x==n-4 else '' for y, x in actor_positions])
        print(actor_positions)
        break
    
    #if time == 18:
    #    break
