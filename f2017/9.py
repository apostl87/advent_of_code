input_ = open("9.in").read().strip()

level = 0
cursor = 0
isGarbage = False
total_score = 0
garbage_counter = 0

while cursor < len(input_):
    c = input_[cursor]
    if not isGarbage:
        if c == '{':
            level += 1
        elif c == '}':
            total_score += level
            level -= 1
        elif c == '<':
            isGarbage = True
    elif isGarbage:
        if c == '!':
            cursor += 2
            continue
        elif c == '>':
            isGarbage = False
        else:
            garbage_counter += 1    
        
    cursor += 1
    
print(total_score)
print(garbage_counter)
