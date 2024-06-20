A = 16807
B = 48271
M = 2147483647

def genA(part2 = False):
    val = 591
    while True:
        val = val * A % M
        if not part2 or val % 4 == 0:
            yield val
        
def genB(part2 = False):
    val = 393
    while True:
        val = val * B % M
        if not part2 or val % 8 == 0:
            yield val

result = 0
a = genA()
b = genB()
for i in range(40_000_000):
    if next(a) & (2**16-1) == next(b) & (2**16-1):
        result += 1
print("Part 1:", result)
        

result = 0
a = genA(True)
b = genB(True)
for i in range(5_000_000):
    if next(a) & (2**16-1) == next(b) & (2**16-1):
        result += 1
print("Part 2:", result)   