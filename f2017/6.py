input_ = open("6.in").read().strip()

# Part 1
banks = [int(x) for x in input_.split()]

known_configurations = []
known_configurations.append(tuple(banks))

k = 0
while True:
    k += 1

    argmax = banks.index(max(banks))
    n = banks[argmax]
    banks[argmax] = 0
    for i in range(1, n + 1):
        banks[(argmax + i) % len(banks)] += 1
        
    if tuple(banks) in known_configurations:
        first_k = known_configurations.index(tuple(banks))
        break
    known_configurations.append(tuple(banks))
    
print(k, "cycles performed")
print("cycle length: ", k - first_k)
