from collections import deque

FILENAME = 'input.txt'

IN = [tuple(map(int, line.split(','))) for line in open(FILENAME, 'r').read().split('\n')]

faces = {}

offsets = [
    (.5, 0, 0),
    (0, .5, 0),
    (0, 0, .5),
    (-.5, 0, 0),
    (0, -.5, 0),
    (0, 0, -.5)
]

min_x = min_y = min_z = float("inf")
max_x = max_y = max_z = -float(" inf")

droplet = set(IN)

for x, y, z in IN:
    min_x = min(min_x, x)
    min_y = min(min_y, y)
    min_z = min(min_z, z)

    max_x = max(max_x, x)
    max_y = max(max_y, y)
    max_z = max(max_z, z)

    for dx, dy, dz in offsets:
        k = (x + dx, y + dy, z + dz)
        if k not in faces:
            faces[k] = 0
        faces[k] += 1

min_x -= 1
min_y -= 1
min_z -= 1

max_x += 1
max_y += 1
max_z += 1

queue = deque([(min_x, min_y, min_z)])
air = {(min_x, min_y, min_z)}

while queue:
    x, y, z = queue.popleft()

    for dx, dy, dz in offsets:
        nx, ny, nz = k = (x + dx * 2, y + dy * 2, z + dz * 2)

        if not (min_x <= nx <= max_x and min_y <= ny <= max_y and min_z <= nz <= max_z):
            continue

        if k in droplet or k in air:
            continue

        air.add(k)
        queue.append(k)

free = set()

for x, y, z in air:
    for dx, dy, dz in offsets:
        free.add((x + dx, y + dy, z + dz))

print('Task 1:', list(faces.values()).count(1))
print('Task 2:', len(set(faces) & free))
