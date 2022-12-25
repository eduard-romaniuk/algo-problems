from collections import deque

area_map = [[c for c in line] for line in open('input.txt', 'r').read().split('\n')]


def find_position(char):
    for row in range(len(area_map)):
        for column in range(len(area_map[row])):
            if area_map[row][column] == char:
                return row, column


height = len(area_map)
width = len(area_map[0])
start = start_row, start_column = find_position('S')
destination = destination_row, destination_column = find_position('E')

area_map[start_row][start_column] = 'a'
area_map[destination_row][destination_column] = 'z'


# Solution
def find_all_possible_routes(from_row, from_column):
    possible_routes = [
        (from_row - 1, from_column),
        (from_row + 1, from_column),
        (from_row, from_column + 1),
        (from_row, from_column - 1)
    ]
    for _row, _column in possible_routes:
        if 0 <= _row < height and 0 <= _column < width:
            if ord(area_map[_row][_column]) <= ord(area_map[from_row][from_column]) + 1:
                yield _row, _column


def solution(start_point):
    queue = deque([start_point])
    visited = set()
    distance = {start_point: 0}

    while queue:
        current_position = queue.popleft()

        if current_position == destination:
            return distance[current_position]

        if current_position in visited:
            continue

        visited.add(current_position)
        for possible_route in find_all_possible_routes(*current_position):
            _row, _column = possible_route

            if possible_route in visited:
                continue

            queue.append(possible_route)
            distance[possible_route] = distance[current_position] + 1

    return -1


result1 = solution(start)
print(f'Task 1: {result1}')


def solution2():
    for _row in range(height):
        for _column in range(width):
            if area_map[_row][_column] == 'a':
                distance = solution((_row, _column))
                if distance != -1:
                    yield distance


result2 = min(solution2())
print(f'Task 2: {result2}')
