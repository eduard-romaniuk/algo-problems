import sys
from typing import Iterable


class Directions:
    _directions = [
        [-1 - 1j, -1j, 1 - 1j],  # north
        [-1 + 1j, 1j, 1 + 1j],  # south
        [-1 - 1j, -1, -1 + 1j],  # west
        [1 - 1j, 1, 1 + 1j]  # east
    ]
    _around = set([pos for direction in _directions for pos in direction])

    def get(self):
        return self._directions

    def iterate(self):
        self._directions = self._directions[1:] + [self._directions[0]]

    def around(self):
        return self._around


class Elf:
    def __init__(self, position):
        self.planned = position
        self.current = position
        self.previous = position

    def __repr__(self):
        return f'Elf{self.current}'

    def has_neighbours(self, elves, directions):
        for route in directions.around():
            if self.current + route in elves:
                return True
        return False

    def could_move(self, elves, direction):
        for route in direction:
            if self.current + route in elves:
                return False
        return True

    def set_planned(self, direction):
        self.planned = self.current + direction[1]
        self.previous = self.current

    def is_planning_to_stay(self):
        return self.planned == self.current


def read_input(filename: str) -> dict[complex, Elf]:
    result = {}
    for y, line in enumerate(open(filename, 'r').read().split('\n')):
        for x, c in enumerate(line):
            if c == '#':
                position = x + y * 1j
                result[position] = Elf(position)
    return result


def find_bounds(elf_positions: Iterable[complex]) -> ((int, int), (int, int)):
    return minmax(map(int, map(lambda x: x.real, elf_positions))), \
        minmax(map(int, map(lambda x: x.imag, elf_positions)))


def minmax(values: Iterable[int]) -> (int, int):
    min = sys.maxsize
    max = -sys.maxsize - 1
    for value in values:
        if value > max:
            max = value
        if value < min:
            min = value
    return min, max


def print_grid(elf_positions: Iterable[complex], name: str):
    ((min_x, max_x), (min_y, max_y)) = find_bounds(elf_positions)
    elves = set(elf_positions)

    print(f'== {name} ==')
    for row in range(min_y, max_y + 1):
        for column in range(min_x, max_x + 1):
            char = '.' if column + row * 1j not in elves else '#'
            print(char, end='')
        print()
