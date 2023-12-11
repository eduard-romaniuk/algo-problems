from itertools import combinations


def expansion(space):
    result = ([], [])
    y = 0
    h = len(space)
    while y < h:
        if all(c == '.' for c in space[y]):
            result[1].append(y)
        y += 1

    x = 0
    w = len(space[0])
    while x < w:
        if all(space[y][x] == '.' for y in range(h)):
            result[0].append(x)
        x += 1

    return result


def get_galaxies(space):
    galaxies = []
    for y, line in enumerate(space):
        for x, c in enumerate(line):
            if c == '#':
                galaxies.append((x, y))
    return galaxies


def inter(p1, p2, ps):
    s = min(p1, p2)
    f = max(p1, p2)
    res = 0
    for p in ps:
        if p < s:
            continue
        if p > f:
            break
        res += 1
    return res


def shortest_path(galaxy1, galaxy2, x_expansions, y_expansions):
    x1, y1 = galaxy1
    x2, y2 = galaxy2
    xe = inter(x1, x2, x_expansions)
    ye = inter(y1, y2, y_expansions)
    return xe + abs(x2 - x1) + ye + abs(y2 - y1)


space = list(map(list, open('input.txt', 'r').read().split('\n')))
exp = expansion(space)
result = sum(shortest_path(*pair, *exp) for pair in combinations(get_galaxies(space), 2))
print('Result:', result)
