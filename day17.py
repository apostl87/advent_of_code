from heapq import heappop, heappush

input_file = 'day17_input.txt'

with open(input_file, "r") as f:
    puzzle_input = f.read().strip()


def part1(puzzle_input):
    grid = [[int(d) for d in line] for line in puzzle_input.split('\n')]
    m, n = len(grid), len(grid[0])
    directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]

    # tuple: (heat-loss, x-coord, y-coord, length-of-current-run, x-direction, y-direction)
    q = [(0, 0, 0, 0, 0, 0)] 
    visited = set()
    while q:
        loss, x, y, k, dx, dy = heappop(q)

        if x == m-1 and y == n-1:
            break

        if any((x, y, k_, dx, dy) in visited for k_ in range(1, k+1)):
            continue
    
        visited.add((x, y, k, dx, dy))
        for new_dx, new_dy in directions:
            straight = (new_dx == dx and new_dy == dy)
            new_x, new_y = x + new_dx, y + new_dy

            if any((new_dx == -dx and new_dy == -dy,
                    k == 3 and straight,
                    new_x < 0, new_y < 0, 
                    new_x == m, new_y == n)):
                continue

            new_k = k + 1 if straight else 1            
            heappush(q, (loss + grid[new_x][new_y], new_x, new_y, new_k, new_dx, new_dy))

    return loss

def part2(puzzle_input):
    grid = [[int(d) for d in line] for line in puzzle_input.split('\n')]
    m, n = len(grid), len(grid[0])
    directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]

    # tuple: (heat-loss, x-coord, y-coord, length-of-current-run, x-direction, y-direction)
    q = [(0, 0, 0, 0, 0, 0)] 
    #q = [(39, 4, 8, 4, 1, 0)]
    visited = set()

    while q:

        loss, x, y, k, dx, dy = heappop(q)

        if x == m-1 and y == n-1:
            if k < 4:
                continue
            break

        if (x, y, k, dx, dy) in visited:
            continue
    
        visited.add((x, y, k, dx, dy))

        if k > 0 and k < 4: # go straight
            new_x, new_y = x + dx, y + dy
            if any((new_x < 0, new_y < 0, 
                    new_x == m, new_y == n)):
                continue
            heappush(q, (loss + grid[new_x][new_y], new_x, new_y, k+1, dx, dy))
            continue

        for new_dx, new_dy in directions:
            straight = (new_dx == dx and new_dy == dy)
            new_x, new_y = x + new_dx, y + new_dy

            if any((new_dx == -dx and new_dy == -dy,
                    k == 10 and straight,
                    new_x < 0, new_y < 0, 
                    new_x == m, new_y == n)):
                continue

            new_k = k + 1 if straight else 1            
            heappush(q, (loss + grid[new_x][new_y], new_x, new_y, new_k, new_dx, new_dy))

    return loss

print(part1(puzzle_input))
print(part2(puzzle_input))