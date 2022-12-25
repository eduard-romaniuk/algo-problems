def parse_movements(data: str) -> list[str]:
    directions = 'LR'
    result = []
    i = 0
    while i < len(data):
        if data[i] in directions:
            result.append(data[i])
            i += 1
            continue
        tmp = ""
        while i < len(data) and data[i] not in directions:
            tmp += data[i]
            i += 1
        result.append(tmp)
    return result


def parse_grid(grid: str) -> list[str]:
    grid = grid.split('\n')
    width = max(map(len, grid))
    # return list(map(lambda x: x.ljust(width), grid))
    return [line.ljust(width) for line in grid]


def read_input(filename):
    grid, movements = open(filename, 'r').read().split('\n\n')
    return parse_grid(grid), parse_movements(movements)
