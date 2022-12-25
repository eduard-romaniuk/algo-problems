FILENAME = 'input.txt'
rocks = [
    [0, 1, 2, 3],
    [1, 1j, 1 + 1j, 2 + 1j, 1 + 2j],
    [0, 1, 2, 2 + 1j, 2 + 2j],
    [0, 1j, 2j, 3j],
    [0, 1, 1j, 1 + 1j]
]
jets = [1 if x == '>' else -1 for x in open(FILENAME, 'r').read()]
solid = {x - 1j for x in range(7)}
height = 0
rock_count = 0
rock_index = 0
rock = {x + 2 + (height + 3) * 1j for x in rocks[rock_index]}
seen = {}
offset = 0
TARGET_ROCK = 1_000_000_000_000


def summarize():
    o = [-20] * 7

    for x in solid:
        r = int(x.real)
        i = int(x.imag)
        o[r] = max(o[r], i)
    top = max(o)
    return tuple(x - top for x in o)


while rock_count < TARGET_ROCK:
    for jet_index, jet in enumerate(jets):
        moved = {x + jet for x in rock}
        if all(0 <= x.real < 7 for x in moved) and not moved & solid:
            rock = moved
        moved = {x - 1j for x in rock}
        if moved & solid:
            solid |= rock
            rock_count += 1
            height = max(x.imag for x in solid) + 1
            if rock_count >= TARGET_ROCK:
                break
            rock_index = (rock_index + 1) % 5
            rock = {x + 2 + (height + 3) * 1j for x in rocks[rock_index]}
            key = (jet_index, rock_index, summarize())
            if key in seen:
                last_rock_count, last_height = seen[key]
                remainder = TARGET_ROCK - rock_count
                repetition = remainder // (rock_count - last_rock_count)
                offset = repetition * (height - last_height)
                rock_count += repetition * (rock_count - last_rock_count)
                seen = {}
            seen[key] = (rock_count, height)
        else:
            rock = moved

print('Task 2:', int(height + offset))
