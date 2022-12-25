from utils import read_input, find_bounds, Directions

FILENAME = 'input.txt'
elves = read_input(FILENAME)
directions = Directions()

round_number = 0
while True:
    round_number += 1
    for elf in elves.values():
        if not elf.has_neighbours(elves, directions):
            continue
        for direction in directions.get():
            if elf.could_move(elves, direction):
                elf.set_planned(direction)
                break

    directions.iterate()

    elves_plans = {}
    for elf in elves.values():
        if elf.is_planning_to_stay():
            continue
        if elf.planned not in elves_plans:
            elves_plans[elf.planned] = []
        elves_plans[elf.planned].append(elf)

    for position, maybe_colliding_elves in list(elves_plans.items()):
        if len(maybe_colliding_elves) > 1:
            for elf in maybe_colliding_elves:
                elf.planned = elf.current
            del elves_plans[position]

    elves_to_move = [_elf[0] for _elf in elves_plans.values()]
    if len(elves_to_move) == 0:
        break

    for elf in elves_to_move:
        del elves[elf.current]
        elf.current = elf.planned
        elves[elf.current] = elf

    if round_number == 10:
        ((min_x, max_x), (min_y, max_y)) = find_bounds(elves.keys())
        print('Task 1:', (max_x - min_x + 1) * (max_y - min_y + 1) - len(elves))

print('Task 2:', round_number)
