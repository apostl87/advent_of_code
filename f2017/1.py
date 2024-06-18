input = open("1.in").read().strip()

result = 0
for i in range(len(input)):
    other_idx = (i + 1) % len(input)
    if input[i] == input[other_idx]:
        result += int(input[i])
    
print(result)

# Part 2
result = 0
for i in range(len(input)):
    other_idx = (i + len(input) // 2) % len(input)
    if input[i] == input[other_idx]:
        result += int(input[i])
        
print(result)