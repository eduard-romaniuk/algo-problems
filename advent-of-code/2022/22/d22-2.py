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
    global dr
    global dc
    global r
    global c

    cdr = dr
    cdc = dc
    nr = r + dr
    nc = c + dc

    # Welcome to hell!
    if nr < 0 and 50 <= nc < 100 and dr == -1:
        dr, dc = 0, 1
        nr, nc = nc + 100, 0
    elif nc < 0 and 150 <= nr < 200 and dc == -1:
        dr, dc = 1, 0
        nr, nc = 0, nr - 100
    elif nr < 0 and 100 <= nc < 150 and dr == -1:
        nr, nc = 199, nc - 100
    elif nr >= 200 and 0 <= nc < 50 and dr == 1:
        nr, nc = 0, nc + 100
    elif nc >= 150 and 0 <= nr < 50 and dc == 1:
        dc = -1
        nr, nc = 149 - nr, 99
    elif nc == 100 and 100 <= nr < 150 and dc == 1:
        dc = -1
        nr, nc = 149 - nr, 149
    elif nr == 50 and 100 <= nc < 150 and dr == 1:
        dr, dc = 0, -1
        nr, nc = nc - 50, 99
    elif nc == 100 and 50 <= nr < 100 and dc == 1:
        dr, dc = -1, 0
        nr, nc = 49, nr + 50
    elif nr == 150 and 50 <= nc < 100 and dr == 1:
        dr, dc = 0, -1
        nr, nc = nc + 100, 49
    elif nc == 50 and 150 <= nr < 200 and dc == 1:
        dr, dc = -1, 0
        nr, nc = 149, nr - 100
    elif nr == 99 and 0 <= nc < 50 and dr == -1:
        dr, dc = 0, 1
        nr, nc = nc + 50, 50
    elif nc == 49 and 50 <= nr < 100 and dc == -1:
        dr, dc = 1, 0
        nr, nc = 100, nr - 50
    elif nc == 49 and 0 <= nr < 50 and dc == -1:
        dc = 1
        nr, nc = 149 - nr, 0
    elif nc < 0 and 100 <= nr < 150 and dc == -1:
        dc = 1
        nr, nc = 149 - nr, 50

    if grid[nr][nc] == '#':
        dr = cdr
        dc = cdc
        return r, c

    return nr, nc


for movement in movements:
    if movement == 'R':
        dr, dc = dc, -dr
        continue
    if movement == 'L':
        dr, dc = -dc, dr
        continue
    for _ in range(int(movement)):
        r, c = step()

print(1000 * (r + 1) + 4 * (c + 1) + direction_key(dr, dc))
