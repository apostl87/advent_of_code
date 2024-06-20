from functools import reduce

def sparse_hash(line, iterations = 1):
    x = list(range(256))
    first_pos = 0 # using this as a marker for the first position
    for i in range(iterations):
        skip_base = i * (len(line))
        for skip, length in enumerate(line):
            x = x[length-1::-1] + x[length:] if length > 1 else x
            jump = (length + skip + skip_base) % len(x)
            first_pos = first_pos - jump if jump > first_pos else first_pos - jump
            x = x[jump:] + x[:jump]
    first_pos %= len(x)
    x = x[first_pos:] + x[:first_pos]
    return x

def dense_hash(sh):
    return [reduce(lambda x, y: x ^ y, sh[i:i+16]) for i in range(0, len(sh), 16)]

def to_hex(dh):
    return ''.join([format(x, '02x') for x in dh])

def knot_hash(str_):
    lst = [ord(i) for i in str_]
    lst.extend([17, 31, 73, 47, 23])
    sh = sparse_hash(lst, 64)
    dh = dense_hash(sh)
    return to_hex(dh)



input_ = open("14.in").read().strip()
print(knot_hash(input_))

n = 128
grid = []
result = 0
for i in range(n):
    hashinput = input_ + '-' + str(i)
    binary = format(int(knot_hash(hashinput), 16), 'b').rjust(n, '0')
    result += binary.count('1')
    grid.append([int(x) for x in list(binary)])
print(result)

n_regions = 0
while any(x for row in grid for x in row):
    for y in range(n):
        for x in range(n):
            if grid[y][x] == 1:
                n_regions += 1
                q = [(x, y)]
                while q:
                    x_, y_ = q.pop()
                    grid[y_][x_] = 0
                    for x_, y_ in [(x_, y_ - 1), (x_, y_ + 1), (x_ - 1, y_), (x_ + 1, y_)]:
                        if 0 <= x_ < n and 0 <= y_ < n and grid[y_][x_] == 1:
                            q.append((x_, y_))
                        
print(n_regions)
    