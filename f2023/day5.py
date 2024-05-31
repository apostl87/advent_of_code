import re
import time

with open("day5_input.txt", "r") as f:
    input_file = f.read()

def part1(input_file):
    segments = input_file.split("\n\n")
    seeds = re.findall(r'\d+', segments[0])

    regex = r'(\d+) (\d+) (\d+)'

    destinations = []
    for seed in map(int,seeds):
        source = seed
        for seg in segments[1:]:
            destination = False
            for mapping_rule in re.findall(regex, seg):
                map_dest, map_src, map_rng = map(eval, mapping_rule)
                if source in range(map_src, map_src+map_rng):
                    destination = map_dest+source-map_src
                    break
            if not destination:
                destination = source
            source = destination
        destinations.append(destination)
    
    return(min(destinations))

def part2(input_file):
    segments = input_file.split("\n\n")
    seed_line = re.findall(r'\d+', segments[0])

    seeds = []
    for i in range(int(len(seed_line)/2)):
        initial_seed = int(seed_line[i*2])
        for k in range(int(seed_line[i*2+1])):
            print(initial_seed+k)
            seeds.append(initial_seed+k)

    regex = r'(\d+) (\d+) (\d+)'

    destinations = []
    for seed in map(int,seeds):
        source = seed
        for seg in segments[1:]:
            destination = False
            for mapping_rule in re.findall(regex, seg):
                map_dest, map_src, map_rng = map(eval, mapping_rule)
                if source in range(map_src, map_src+map_rng):
                    destination = map_dest+source-map_src
                    break
            if not destination:
                destination = source
            source = destination
        destinations.append(destination)
    
    return(min(destinations))

def part2_optimized(puzzle_input):
    segments = puzzle_input.split('\n\n')
    intervals = []

    for seed in re.findall(r'(\d+) (\d+)', segments[0]):
        x1, dx = map(int, seed)
        x2 = x1 + dx
        intervals.append((x1, x2, 1))

    min_location = float('inf')
    counter = 0
    while intervals:
        counter += 1
        x1, x2, level = intervals.pop()
        if level == 8:
            min_location = min(x1, min_location)
            continue

        for conversion in re.findall(r'(\d+) (\d+) (\d+)', segments[level]):
            z, y1, dy = map(int, conversion)
            y2 = y1 + dy
            diff = z - y1
            if x2 <= y1 or y2 <= x1:    # no overlap
                continue
            if x1 < y1:                 # split original interval at y1
                intervals.append((x1, y1, level))
                x1 = y1
            if y2 < x2:                 # split original interval at y2
                intervals.append((y2, x2, level))
                x2 = y2
            intervals.append((x1 + diff, x2 + diff, level + 1)) # perfect overlap -> make conversion and let pass to next nevel 
            break

        else:
            intervals.append((x1, x2, level + 1))
  
    print("count: ", counter)
    return min_location


print(part1(input_file))
t = time.time()
print(part2_optimized(input_file))
print((time.time()-t)*1e6)