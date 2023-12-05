import re
import math

lines = open('input.txt', 'r').read().split('\n')
result = 0

for line in lines:
    winning, owned = list(map(lambda x: re.findall(r'\d+', x), line.split(':')[1].split('|')))
    wins = len(set(winning).intersection(set(owned)))

    if wins == 0:
        continue

    points = int(math.pow(2, wins - 1))
    result += points

print(result)
