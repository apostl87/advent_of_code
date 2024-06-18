input_ = open("2.in").read()
results1, results2 = [], []
for line in input_.splitlines():
    numbers = [int(x) for x in line.split()]
    results1.append(max(numbers) - min(numbers))
    
    for n in numbers:
        for d in numbers:
            if d == n:
                continue
            q = n/d
            if q == int(q):
                results2.append(int(q))

print(sum(results1))
print(sum(results2))
