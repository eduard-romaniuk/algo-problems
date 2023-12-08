import collections
import functools


def rank(hand):
    def most_common(counter):
        if len(counter.most_common(1)) == 0:
            return 0
        return counter.most_common(1)[0][1]

    c = collections.Counter(hand)
    jokers = 0
    if c['J'] > 0:
        jokers = c.pop('J')
    mc = most_common(c) + jokers
    if len(c) <= 1:
        return 7
    if len(c) == 2:
        if mc == 4:
            return 6
        else:
            return 5
    if len(c) == 3:
        if mc == 3:
            return 4
        else:
            return 3
    if len(c) == 4:
        return 2
    return 1


hands = []
for line in open('input.txt', 'r').read().split('\n'):
    hand, bid = line.split(' ')
    hands.append((hand, rank(hand), bid))


def card_num(card):
    if card.isdigit():
        return int(card)
    if card == 'T':
        return 10
    if card == 'J':
        return 1
    if card == 'Q':
        return 12
    if card == 'K':
        return 13
    if card == 'A':
        return 14


def comp_hands(h1, h2):
    if h1[1] > h2[1]:
        return 1
    if h1[1] < h2[1]:
        return -1
    i = 0
    while h1[0][i] == h2[0][i] and i < 5:
        i += 1
    if i == 5:
        return 0
    if card_num(h1[0][i]) > card_num(h2[0][i]):
        return 1
    return -1


result = 0
for i, hand in enumerate(sorted(hands, key=functools.cmp_to_key(comp_hands))):
    print(hand, i)
    result += int(hand[2]) * (i + 1)

print('Result:', result)
