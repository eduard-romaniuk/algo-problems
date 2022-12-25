hands = {
    'A': 0,
    'B': 1,
    'C': 2,
    'X': 0,
    'Y': 1,
    'Z': 2,
}

inp = list(map(
    lambda line: tuple(map(
        lambda n: hands[n],
        line.split()
    )),
    open('input.txt', 'r').read().splitlines()
))

print('Task 1: ', sum([(b - a + 1) % 3 * 3 + b + 1 for a, b in inp]))
print('Task 2: ', sum([b * 3 + (a + b - 1) % 3 + 1 for a, b in inp]))
