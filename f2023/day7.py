import re
from collections import Counter
from functools import cmp_to_key

with open("day7_input.txt", "r") as f:
    puzzle_input = f.read()

def part1(puzzle_input):
    regex = r'(.*) (.*)'
    inputs = re.findall(regex, puzzle_input)

    hands = [x[0] for x in inputs]

    def get_type(hand):
        counters = Counter(hand).values()
        maximum = max(counters)
        if sorted(counters) == [1, 2, 2]:
            return 2
        if 2 in counters and 3 in counters:
            return 4
        if maximum <= 2:
            return maximum-1
        if maximum == 3:
            return maximum
        if maximum >=4:
            return maximum+1


    def compare(a, b):
        type_a = get_type(a[0])
        type_b = get_type(b[0])
        if type_a > type_b:
            return 1
        if type_a < type_b:
            return -1
        for card_a, card_b in zip(a[0], b[0]):
            if card_a == card_b:
                continue
            a_wins = (cardpool.index(card_a) > cardpool.index(card_b))
            return 1 if a_wins else -1

    cardpool = '23456789TJQKA'
    inputs.sort(key=cmp_to_key(compare))

    return sum([(i+1)*int(x[1]) for i, x in enumerate(inputs)])


def part2(puzzle_input):
    regex = r'(.*) (.*)'
    inputs = re.findall(regex, puzzle_input)

    def get_type(hand):
        counters = Counter(hand)
        mykeys = list(counters.keys())
        try:
            mykeys.remove('J')
            jokers = counters['J']
        except:
            jokers = 0
            pass
        counter_values_excluding_jokers = sorted([counters[x] for x in mykeys], reverse=True)

        counter_values_with_jokers = counter_values_excluding_jokers
        if len(counter_values_with_jokers)>0:
            counter_values_with_jokers[0] += jokers
        else:
            counter_values_with_jokers.append(jokers)
        maximum = max(counter_values_with_jokers)

        if sorted(counter_values_with_jokers) == [1, 2, 2]:
            return 2
        if 2 in counter_values_with_jokers and 3 in counter_values_with_jokers:
            return 4
        if maximum <= 2:
            return maximum-1
        if maximum == 3:
            return maximum
        if maximum >=4:
            return maximum+1

    def compare(a, b):
        type_a = get_type(a[0])
        type_b = get_type(b[0])
        if type_a > type_b:
            return 1
        if type_a < type_b:
            return -1
        for card_a, card_b in zip(a[0], b[0]):
            if card_a == card_b:
                continue
            a_wins = (cardpool.index(card_a) > cardpool.index(card_b))
            return 1 if a_wins else -1

    cardpool = 'J23456789TQKA'
    inputs.sort(key=cmp_to_key(compare))

    return sum([(i+1)*int(x[1]) for i, x in enumerate(inputs)])

print(part1(puzzle_input))
print(part2(puzzle_input))