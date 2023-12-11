from enum import Enum


class Direction(Enum):
    RIGHT = (0, 1)
    LEFT = (0, -1)
    UP = (-1, 0)
    DOWN = (1, 0)


directions_map = {
    'S': {},
    '.': {},
    '|': {
        Direction.UP: Direction.UP,
        Direction.DOWN: Direction.DOWN
    },
    '-': {
        Direction.RIGHT: Direction.RIGHT,
        Direction.LEFT: Direction.LEFT
    },
    'L': {
        Direction.LEFT: Direction.UP,
        Direction.DOWN: Direction.RIGHT
    },
    'J': {
        Direction.RIGHT: Direction.UP,
        Direction.DOWN: Direction.LEFT
    },
    '7': {
        Direction.RIGHT: Direction.DOWN,
        Direction.UP: Direction.LEFT
    },
    'F': {
        Direction.LEFT: Direction.DOWN,
        Direction.UP: Direction.RIGHT
    }
}


def pipe_to_direction(pipe, direction):
    return directions_map[pipe].get(direction)


def get_starting_position(matrix):
    for i, line in enumerate(matrix):
        for j, cell in enumerate(line):
            if cell == 'S':
                return i, j


def get_pipe(matrix, position):
    return matrix[position[0]][position[1]]


def follow_path(matrix, position, direction):
    steps = 0
    while direction is not None:
        position = (position[0] + direction.value[0], position[1] + direction.value[1])
        direction = pipe_to_direction(get_pipe(matrix, position), direction)
        steps += 1
        if get_pipe(matrix, position) == 'S':
            return steps // 2
    return 0


matrix = open('input.txt', 'r').read().split('\n')
starting_position = get_starting_position(matrix)
for direction in Direction:
    x = follow_path(matrix, starting_position, direction)
    if x != 0:
        print('Result:', x)
        break
