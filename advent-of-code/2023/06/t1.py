import re
import math


def solutions(race_time, record_distance):
    record_distance += 1
    D = race_time * race_time - 4 * record_distance
    if D < 0:
        print(f'race_time={race_time}\nrecord_distance={record_distance}')
        print(f'D={D}')
        exit()
    if D == 0:
        return 1
    x1 = math.ceil((race_time - math.sqrt(D)) / 2)
    x2 = math.floor((race_time + math.sqrt(D)) / 2)
    return x2 - x1 + 1


digit_regex = re.compile(r'\d+')
races = zip(*[map(int, digit_regex.findall(line)) for line in open('input.txt', 'r').read().split('\n')])
result = math.prod([solutions(*race) for race in races])
print('Result:', result)
