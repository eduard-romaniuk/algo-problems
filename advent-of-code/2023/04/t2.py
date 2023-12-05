import re

lines = open('input.txt', 'r').read().split('\n')

cards = [1] * len(lines)

for i, line in enumerate(lines):
    winning, owned = list(map(lambda x: re.findall(r'\d+', x), line.split(':')[1].split('|')))
    wins = len(set(winning).intersection(set(owned)))

    if wins == 0:
        continue

    for j in range(i + 1, i + 1 + wins):
        cards[j] += cards[i]

print(sum(cards))
