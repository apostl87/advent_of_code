import copy, re
import sys
if "--test" in sys.argv or "-t" in sys.argv:
    test = True
else:
    test = False

input_file = "day19test.txt" if test==True else "day19.txt"
with open(input_file, "r") as f:
    input_ = f.read().strip()

def parse_input(input_, test=test):
    bps = dict()
    separator = "\n" if test==False else "\n"
    for segment in input_.split(separator):
        x = re.findall(r'(\d+)', segment)
        x = [int(y) for y in x]
        bps[x[0]] = [(x[1], 0, 0, 0), (x[2], 0, 0, 0), (x[3], x[4], 0, 0), (x[5], 0, x[6], 0)]
    return bps

def do_blueprint(bp, minute, stock, robots, next_robot=None, last_minute=None):
    global max_geodes

    if minute == last_minute:
        max_geodes = max(max_geodes, stock[-1]+robots[-1])
        return

    next_minute = minute

    if next_robot is not None: # build robot
        while any([s < c for s, c in zip(stock, bp[next_robot])]):
            next_minute += 1
            stock = [s + r for s, r in zip(stock, robots)]
            if next_minute == last_minute:
                do_blueprint(bp, next_minute, [s for s in stock], [r for r in robots], None, last_minute)
                return
            if next_minute > last_minute:
                print('error')
                return

        next_minute = next_minute + 1
        stock = [s + r for s, r in zip(stock, robots)]
        if next_minute <= last_minute:
            robots[next_robot] += 1
            stock = [stock[j]-bp[next_robot][j] for j in range(4)]

    else:
        next_minute = next_minute + 1
        stock = [s + r for s, r in zip(stock, robots)]
    for new_robot in range(4):
        if new_robot == 3 or robots[new_robot] < max([bp[z][new_robot] for z in range(new_robot, 4)]):
            do_blueprint(bp, next_minute, [s for s in stock], [r for r in robots], new_robot, last_minute)


part2 = True
# Part 1
if not part2:
    bps = parse_input(input_)
    stock = [0, 0, 0, 0]
    robots = [1, 0, 0, 0]

    quality_levels = []
    for key in bps:
        max_geodes = 0
        for next_robot in range(4):
            do_blueprint(bps[key], 0, [s for s in stock], [r for r in robots], next_robot, last_minute=23)
        print("Max geodes:", max_geodes)
        quality_levels.append( max_geodes )
   
    print("Part 1:", sum([q * (i) for q, i in zip(quality_levels, bps)]))
    quit()

# Part 2
bps = parse_input(input_)
stock = [0, 0, 0, 0]
robots = [1, 0, 0, 0]

result = []
for key in [1, 2, 3]:
    max_geodes = 0
    for next_robot in range(4):
        do_blueprint(bps[key], 0, [s for s in stock], [r for r in robots], next_robot, last_minute=31)
    print("Max geodes:", max_geodes)
    result.append(max_geodes)

print("Part 2:", result[0]*result[1]*result[2])

