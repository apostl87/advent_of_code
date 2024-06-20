from functools import reduce

input_ = '3, 4, 1, 6'
input_ = open("10.in").read().strip()

# Part 1
line = [int(i) for i in input_.split(',')]

x = list(range(5))
x = list(range(256))

first_pos = 0 # using this as a marker for the first position
for skip, length in enumerate(line):
    x = x[length-1::-1] + x[length:] if length > 1 else x
    jump = (length + skip) % len(x)
    first_pos = first_pos - jump if jump > first_pos else first_pos - jump
    x = x[jump:] + x[:jump]
first_pos %= len(x)
print(x[first_pos] * x[(first_pos+1) % len(x)])


# Part 2
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

line = [ord(i) for i in input_]
line.extend([17, 31, 73, 47, 23])
sh = sparse_hash(line, 64)
dh = dense_hash(sh)
result = to_hex(dh)
print(result)