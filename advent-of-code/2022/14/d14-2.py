SAND_START_POINT = (500, 0)
SAND = "▼"
SAND_REST = "o"
ROCK = "#"
AIR = "."


def parse_coords(coords_str):
    [x, y] = coords_str.split(',')
    return int(x), int(y)


def find_dimensions(rocks_coordinates, verbose=False):
    zipped = list(zip(*rocks_coordinates))
    width_min = min(zipped[0])
    width_max = max(zipped[0])
    height_max = max(zipped[1])
    if verbose:
        print(f'Cave dimensions: {width_min} -> {width_max} , 0 -> {height_max}')
    return width_min, width_max, 0, height_max


def read_input(verbose=False):
    def _coords():
        for line in open('input.txt', 'r').read().split('\n'):
            coords = line.split(' -> ')
            for pair in zip(coords[:-1], coords[1:]):
                x1, y1 = parse_coords(pair[0])
                x2, y2 = parse_coords(pair[1])
                xs = min(x1, x2)
                xe = max(x1, x2)
                ys = min(y1, y2)
                ye = max(y1, y2)
                if verbose:
                    print('--===--')
                    print(pair)
                    print(xs, ys)
                    print(xe, ye)
                    print('Generator:')
                for x in range(xs, xe + 1):
                    for y in range(ys, ye + 1):
                        if verbose:
                            print(x, y)
                        yield x, y

    rocks = list(_coords())
    height_max = find_dimensions(rocks)[3] + 2
    for x in range(1000):
        rocks.append((x, height_max))
    return rocks

def generate_grid(rocks_coordinates, width_min, width_max, height_min, height_max):
    def get_structure(x, y):
        return ROCK if (x, y) in rocks_coordinates else AIR

    return [[get_structure(x, y) for x in range(width_min, width_max + 1)] for y in range(height_min, height_max + 1)]


def print_grid(grid, sand_position):
    height_fill = len(str(len(grid) - 1))
    width = len(grid[0])
    for index_line in zip(*[str(i).rjust(len(str(width - 1))) for i in range(width)]):
        print(' ' * (height_fill + 1) + ' '.join(index_line))
    for li, line in enumerate(grid):
        print(str(li).rjust(height_fill), end=' ')
        for si, structure in enumerate(line):
            if (si, li) == sand_position:
                print(SAND, end=' ')
                continue
            print(structure, end=' ')
        print()


def solution(grid, width_min, width_max, verbose=False):
    rest_sand_count = 0
    finished = False
    x, y = SAND_START_POINT

    def _print():
        print_grid(grid, (x, y))
        print('=====================')

    if verbose:
        print('=== Initial state ===')
        _print()

    iteration = 0
    while not finished:
        iteration += 1
        # print(iteration)
        if x < 0 or x > width_max - width_min or y >= len(grid) - 1:
            finished = True
            break
        if grid[y + 1][x] == AIR:
            y += 1
        elif grid[y + 1][x - 1] == AIR:
            x -= 1
            y += 1
        elif grid[y + 1][x + 1] == AIR:
            x += 1
            y += 1
        else:
            grid[y][x] = SAND_REST
            rest_sand_count += 1
            if (x, y) == SAND_START_POINT:
                break
            x, y = SAND_START_POINT
        if verbose:
            _print()
    if verbose:
        _print()
    return rest_sand_count


if __name__ == '__main__':
    rocks_coordinates = read_input()
    dimensions = find_dimensions(rocks_coordinates)
    grid = generate_grid(rocks_coordinates, *dimensions)
    print(solution(grid, dimensions[0], dimensions[1]))
