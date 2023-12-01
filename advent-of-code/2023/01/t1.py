import re

lines = open('input.txt', 'r').read().split('\n')
result = 0

for x in lines:
    z = re.findall(r'\d', x)
    result += int(z[0] + z[-1])

print(result)
