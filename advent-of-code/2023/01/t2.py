import re

dw = list(enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']))
lines = open('input.txt', 'r').read().split('\n')
result = 0

for x in lines:
    for d, w in dw:
        x = x.replace(w, w[0] + str(d + 1) + w[-1])
    z = re.findall(r'\d', x)
    result += int(z[0] + z[-1])

print(result)
