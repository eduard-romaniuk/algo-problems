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
result = sys.maxsize
maps = [sorted(m, key=lambda x: x[1]) for m in data[1:]]
seeds = []
for i in range(0, len(data[0][0]), 2):
    start = data[0][0][i]
    size = data[0][0][i + 1]
    seeds.append([start, start + size])


# source = [start, end]
def mapping(sources, map_i):
    global result, maps
    if map_i == len(maps):
        for source in sources:
            if source[0] < result:
                result = source[0]
        return

    new_sources = []

    for source in sources:
        for line in maps[map_i]:
            start = line[1]
            end = line[1] + line[2]
            if source[0] >= end:
                if line == maps[map_i][-1]:
                    new_sources.append(source)
                continue
            if source[1] < start:
                new_sources.append(source)
                break

            if start > source[0]:
                new_sources.append([source[0], start])
                source[0] = start

            if end < source[1]:
                diff = source[0] - start
                new_source_start = line[0] + diff
                new_sources.append([new_source_start, new_source_start + end - source[0]])
                source[0] = end
                continue

            diff = source[0] - start
            new_source_start = line[0] + diff
            new_sources.append([new_source_start, new_source_start + source[1] - source[0]])
            break
    mapping(new_sources, map_i + 1)


mapping(seeds, 0)
print('Result:', result)
