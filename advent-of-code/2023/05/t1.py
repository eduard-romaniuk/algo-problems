import re
import sys

digit_re = re.compile(r'\d+')
data = [
    [
        [
            int(d) for d in digit_re.findall(line)
        ] for line in matrix.split('\n')[1:]
    ] for matrix in open('input.txt', 'r').read().split('\n\n')
]
seeds = data[0][0]
maps = data[1:]
result = sys.maxsize
for source in seeds:
    for gmap in maps:
        for line in sorted(gmap, key=lambda x: x[1]):
            if source >= line[1] + line[2]:
                continue
            if source < line[1]:
                break
            diff = source - line[1]
            new_source = line[0] + diff
            source = new_source
            break
    if source < result:
        result = source

print('Result:', result)
