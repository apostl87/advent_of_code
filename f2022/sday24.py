import os

test_input = False
if test_input:
    input_file = "day24test.txt"
else:
    input_file = "day24.txt"
if os.getcwd().split('/')[-1] != "f2022":
    input_file = 'f2022/' + input_file

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

y_end_, x_end_ = [m-2, 1, m-2], [n-2, 1, n-2]
actor_positions_ = [{(0, 1)}, {(m-1, n-2)}, {(0, 1)}]

part2 = True

for y_end, x_end, actor_positions in zip(y_end_, x_end_, actor_positions_):
    print(y_end, x_end, actor_positions)
    while True:

        #print("check 1")

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
        #print("Time", time)

        #print("check 2")
        new_actor_positions = set()
        #print(len(actor_positions))
        for pos in actor_positions:
            
            #print(pos)
            candidates = [(pos[0]+y, pos[1]+x) for y, x in dir2coords.values()] + [(pos[0], pos[1])]

            for (y, x) in candidates:
                valid = (y, x) == (0, 1) or (y, x) == (m-1, n-2) or (y > 0 and y < m-1 and x > 0 and x < n-1)

                if valid:
                    if new_blizzards[y][x] == []:
                        #print("here")
                        new_actor_positions.add((y,x))
        #print("check 2a")

        actor_positions = new_actor_positions

        #print("check 3")

        if (y_end, x_end) in actor_positions:
  
            break

        if time ==  2300:
            break
        #    print(list2string(blizzards))
        #    print([x if x==n-4 else '' for y, x in actor_positions])
        #    print(actor_positions)
        #    break
        
        #if time == 18:
        #    break
    if not part2: break

if part2:
    print("Part 2:", time+1)
else:
    print("Part 1:", time+1)