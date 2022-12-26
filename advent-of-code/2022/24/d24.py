from collections import defaultdict, deque

grid = open('input.txt').read().splitlines()
HEIGHT = len(grid)
WIDTH = len(grid[0])

init_blizzards = defaultdict(list)

start_x, start_y = 1, 0
goal_x, goal_y = WIDTH - 2, HEIGHT - 1

walls = set()
for y, line in enumerate(grid):
    for x, c in enumerate(line):
        if c in '><v^':
            init_blizzards[(x, y)].append(c)
        elif c == '#':
            walls.add((x, y))

directions = {'>': (1, 0), '<': (-1, 0), 'v': (0, 1), '^': (0, -1)}


def next_state(prev_state):
    blizzards = defaultdict(list)
    for pos, kinds in prev_state.items():
        for kind in kinds:
            dx, dy = directions[kind]
            x, y = pos
            x += dx
            y += dy
            if grid[y][x] == '#':
                match directions[kind]:
                    case 0, 1:
                        y = 1
                    case 0, -1:
                        y = HEIGHT - 2
                    case 1, 0:
                        x = 1
                    case -1, 0:
                        x = WIDTH - 2
            blizzards[(x, y)].append(kind)

    return blizzards


_states = {}
_states[0] = init_blizzards


def states(time):
    if time not in _states:
        _states[time] = next_state(_states[time - 1])
    return _states[time]


que = deque([(start_x, start_y, 0, [])])
seen = set()
time = 0
while que:
    x, y, time, goals = que.popleft()
    if (x, y, time) in seen:
        continue
    seen.add((x, y, time))

    state = states(time)

    if (x, y) == (goal_x, goal_y) and sum(goals) == 2:
        print('Task 2:', time)
        break
    elif len(state[(x, y)]) == 0 and (x, y) not in walls and x >= 0 and y >= 0 and x < WIDTH and y < HEIGHT:
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1), (0, 0)]:
            new_pos = x + dx, y + dy
            if new_pos == (goal_x, goal_y) and sum(goals) == 0:
                que = deque([(*new_pos, time + 1, goals + [True])])
                print('Task 1:', time + 1)
            elif new_pos == (start_x, start_y) and sum(goals) == 1:
                que = deque([(*new_pos, time + 1, goals + [True])])
            else:
                que.append((*new_pos, time + 1, goals))