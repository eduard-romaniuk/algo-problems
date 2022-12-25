import functools
import re
from collections import deque

FILENAME = 'input.txt'


def read_input():
    valves = {}
    tunnels = {}
    num_pattern = re.compile(r'\d+')
    valve_pattern = re.compile(r'[A-Z]{2}')
    for line in open(FILENAME, 'r').read().split('\n'):
        _valves = valve_pattern.findall(line)
        _valve = _valves[0]
        flow_rate = int(num_pattern.findall(line)[0])
        valves[_valve] = flow_rate
        tunnels[_valve] = _valves[1:]
    return valves, tunnels


STARTING_VALVE = 'AA'
VALVES, TUNNELS = read_input()
DISTANCES = {}
NOT_EMPTY = []
# print(VALVES)
# print(TUNNELS)

for valve in VALVES:
    if valve != STARTING_VALVE and not VALVES[valve]:
        continue

    if valve != STARTING_VALVE:
        NOT_EMPTY.append(valve)

    DISTANCES[valve] = {valve: 0, STARTING_VALVE: 0}

    visited = {valve}
    queue = deque([(0, valve)])

    while queue:
        distance, position = queue.popleft()
        for neighbour in TUNNELS[position]:
            if neighbour in visited:
                continue
            else:
                visited.add(neighbour)

            if VALVES[neighbour]:
                DISTANCES[valve][neighbour] = distance + 1

            queue.append((distance + 1, neighbour))

    del DISTANCES[valve][valve]
    if valve != STARTING_VALVE:
        del DISTANCES[valve][STARTING_VALVE]

INDICES = {element: index for index, element in enumerate(NOT_EMPTY)}


# print(json.dumps(DISTANCES, indent=2))

@functools.lru_cache(maxsize=None)
def dfs(time, bitmask, valve=STARTING_VALVE):
    _max = 0
    for neighbour in DISTANCES[valve]:
        _bit = 1 << INDICES[neighbour]
        if bitmask & _bit:
            continue
        remaining_time = time - DISTANCES[valve][neighbour] - 1
        if remaining_time <= 0:
            continue
        _max = max(_max, dfs(remaining_time, bitmask | _bit, neighbour) + VALVES[neighbour] * remaining_time)
    return _max


print('Task 1:', dfs(30, 0))

b = (1 << len(NOT_EMPTY)) - 1

_max = 0

for i in range(b + 1):
    _max = max(_max, dfs(26, i) + dfs(26, b ^ i))

print('Task 2:', _max)
