from math import prod


class Round:
    red = 0
    green = 0
    blue = 0

    def __init__(self, r):
        def cubes_of_color(r, color):
            for turn in r.split(', '):
                [cubes, turn_color] = turn.strip().split(' ')
                if turn_color == color:
                    return int(cubes)
            return 0

        self.red = cubes_of_color(r, 'red')
        self.green = cubes_of_color(r, 'green')
        self.blue = cubes_of_color(r, 'blue')


class Game:
    id = 0
    rounds = []

    def __init__(self, line):
        self.id = int(line.split(':')[0].split(' ')[-1])
        self.rounds = [Round(r) for r in line.split(':')[1].split('; ')]

    def is_qualified(self):
        for r in self.rounds:
            if r.red > 12 or r.green > 13 or r.blue > 14:
                return False
        return True

    def minimum_required_cubes(self):
        red = 0
        green = 0
        blue = 0
        for r in self.rounds:
            if r.red > red:
                red = r.red
            if r.green > green:
                green = r.green
            if r.blue > blue:
                blue = r.blue
        return [red, green, blue]

    def power(self):
        return prod(self.minimum_required_cubes())
