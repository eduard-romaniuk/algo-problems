import tests


# Indices generator function to split data collection and traverse logic
def zigzag_indices(height, width):
    row_end = height - 1
    column_end = width - 1
    going_down = True

    row = column = 0
    while row <= row_end and column <= column_end:
        yield row, column

        if going_down:
            if column == 0 or row == row_end:
                going_down = False
                if row == row_end:
                    column += 1
                else:
                    row += 1
            else:
                row += 1
                column -= 1
        else:
            if row == 0 or column == column_end:
                going_down = True
                if column == column_end:
                    row += 1
                else:
                    column += 1
            else:
                row -= 1
                column += 1


# Time O(n)
# Space O(1)
def zigzag_traverse(array):
    return [array[row][column] for row, column in zigzag_indices(len(array), len(array[0]))]


tests.test(zigzag_traverse)
