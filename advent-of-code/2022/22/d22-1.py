from parsing import read_input

FILENAME = 'input.txt'

grid, movements = read_input(FILENAME)

r = 0
c = 0
dr = 0
dc = 1

while grid[r][c] == ' ':
    c += 1


def direction_key(dr, dc):
    if dr == 0 and dc == 1:
        return 0
    if dr == 0 and dc == -1:
        return 2
    if dr == 1 and dc == 0:
        return 1
    if dr == -1 and dc == 0:
        return 3


def step():
    nr = r
    nc = c
    while True:
        nr = (nr + dr) % len(grid)
        nc = (nc + dc) % len(grid[r])
        if grid[nr][nc] != ' ':
            break
    return nr, nc


for movement in movements:
    if movement == 'R':
        dr, dc = dc, -dr
        continue
    if movement == 'L':
        dr, dc = -dc, dr
        continue
    for _ in range(int(movement)):
        nr, nc = step()
        if grid[nr][nc] == '#':
            break
        r = nr
        c = nc

print(1000 * (r + 1) + 4 * (c + 1) + direction_key(dr, dc))
