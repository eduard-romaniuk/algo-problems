import tests


# Indices generator function to split data collection and traverse logic
def spiral_indices(height, width):
    row_start = 0
    row_end = height - 1
    column_start = 0
    column_end = width - 1

    while row_start <= row_end and column_start <= column_end:
        for column in range(column_start, column_end + 1):
            yield row_start, column

        for row in range(row_start + 1, row_end + 1):
            yield row, column_end

        if row_start != row_end:
            for column in range(column_end - 1, column_start - 1, -1):
                yield row_end, column

        if column_start != column_end:
            for row in range(row_end - 1, row_start, -1):
                yield row, column_start

        row_start += 1
        column_start += 1
        row_end -= 1
        column_end -= 1


# Time O(n)
# Space O(1)
def spiral_traverse(array):
    return [array[row][column] for row, column in spiral_indices(len(array), len(array[0]))]


tests.test(spiral_traverse)
