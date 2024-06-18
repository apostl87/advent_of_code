input = 939601

recipes = [3, 7]
elf1 = 0
elf2 = 1

# Part 1
while len(recipes) < input + 10:
    scoresum = recipes[elf1] + recipes[elf2]
    if scoresum >= 10:
        recipes.append(scoresum // 10)
        recipes.append(scoresum % 10)
    else:
        recipes.append(scoresum)
    elf1 = (elf1 + 1 + recipes[elf1]) % len(recipes)
    elf2 = (elf2 + 1 + recipes[elf2]) % len(recipes)
print(''.join(map(str,recipes[input:input + 10])))

# Part 2
recipes = [3, 7]
digits = [int(x) for x in str(input)]
elf1 = 0
elf2 = 1

while True:
    scoresum = recipes[elf1] + recipes[elf2]
    if scoresum >= 10:
        recipes.append(1)
        recipes.append(scoresum - 10)
    else:
        recipes.append(scoresum)
        
    if digits == recipes[-len(digits):]:
        print("Part 2:", len(recipes) - len(digits))
        break
    if digits == recipes[-len(digits)-1:-1]:
        print("Part 2:", len(recipes) - len(digits) - 1)
        break
        
    elf1 = (elf1 + 1 + recipes[elf1]) % len(recipes)
    elf2 = (elf2 + 1 + recipes[elf2]) % len(recipes)