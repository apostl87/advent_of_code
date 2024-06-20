input_ = open("4.in").read().strip()

result = 0
for line in input_.split("\n"):
    words1 = list(line.split())
    words2 = set(words1)
    if len(words1) == len(words2):
        result += 1
print("Part 1:", result)

result = 0
for line in input_.split("\n"):
    words = list(line.split())
    
    letterpools = set()
    for word in words:
        letterpools.add(frozenset(word))
        
    if len(letterpools) == len(words):
        result += 1
print("Part 2:", result)