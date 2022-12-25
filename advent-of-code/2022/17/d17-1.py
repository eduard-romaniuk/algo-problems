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

while rock_count < 2022:
    for jet in jets:
        moved = {x + jet for x in rock}
        if all(0 <= x.real < 7 for x in moved) and not moved & solid:
            rock = moved
        moved = {x - 1j for x in rock}
        if moved & solid:
            solid |= rock
            rock_count += 1
            height = max(x.imag for x in solid) + 1
            if rock_count >= 2022:
                break
            rock_index = (rock_index + 1) % 5
            rock = {x + 2 + (height + 3) * 1j for x in rocks[rock_index]}
        else:
            rock = moved

print('Task 1:', int(height))
