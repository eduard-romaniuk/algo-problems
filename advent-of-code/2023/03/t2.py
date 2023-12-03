import math

matrix = open('input.txt', 'r').read().split('\n')


def adjacent_cells(ri, ci):
    return [
        (ri + 1, ci - 1), (ri + 1, ci), (ri + 1, ci + 1),
        (ri, ci - 1), (ri, ci), (ri, ci + 1),
        (ri - 1, ci - 1), (ri - 1, ci), (ri - 1, ci + 1)
    ]


def check_for_part(ri, ci):
    if ri < 0 or ri > len(matrix) or ci < 0 or ci > len(matrix[ri]) or not matrix[ri][ci].isdigit():
        return 0, 0, 0
    num = ''

    cci = ci
    while cci >= 0 and matrix[ri][cci].isdigit():
        num = matrix[ri][cci] + num
        cci -= 1

    sci = cci + 1

    cci = ci + 1
    while cci < len(matrix[ri]) and matrix[ri][cci].isdigit():
        num += matrix[ri][cci]
        cci += 1
    return ri, sci, int(num)


result = 0
for ri, row in enumerate(matrix):
    for ci, char in enumerate(row):
        if not char.isalnum() and char == '*':
            parts = set(
                filter(
                    lambda part: part != (0, 0, 0),
                    [check_for_part(*cell) for cell in adjacent_cells(ri, ci)]
                )
            )
            if len(parts) == 2:
                result += math.prod(map(lambda part: part[2], parts))

print(result)
