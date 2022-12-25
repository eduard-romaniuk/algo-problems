import re


def read_input(filename):
    pattern = re.compile(r'-?\d+')
    result = []
    for line in open(filename, 'r').read().split('\n'):
        result.append(tuple(map(int, pattern.findall(line))))
    return result


INPUT = read_input('input.txt')


def solution1():
    target_y = 10
    covered = set()
    beacons = set()

    for sx, sy, bx, by in INPUT:
        distance = abs(sx - bx) + abs(sy - by)
        offset = distance - abs(sy - target_y)

        if offset < 0:
            continue

        low_x = sx - offset
        high_x = sx + offset
        for x in range(low_x, high_x + 1):
            covered.add(x)

        if by == target_y:
            beacons.add(bx)

    return len(covered) - len(beacons)


def solution2():
    _max = 4_000_000
    for target_y in range(_max + 1):
        covered_intervals = []

        for sx, sy, bx, by in INPUT:
            distance = abs(sx - bx) + abs(sy - by)
            offset = distance - abs(sy - target_y)

            if offset < 0:
                continue

            start = sx - offset
            end = sx + offset
            covered_intervals.append((start, end))

        covered_intervals.sort()

        covered_zone = [list(covered_intervals[0])]
        for start, end in covered_intervals[1:]:
            q_low, q_high = covered_zone[-1]
            if start > q_high + 1:
                covered_zone.append([start, end])
            else:
                covered_zone[-1][1] = max(q_high, end)

        x = 0
        for start, end in covered_zone:
            if x < start:
                return x * 4_000_000 + target_y
            else:
                x = end + 1

            if x > _max:
                break


if __name__ == '__main__':
    print('Task 1:', solution1())
    print('Task 2:', solution2())
