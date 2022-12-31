import tests

EMPTY = '.'


# Time O(9^2) ~ O(1)
# Space O(3 * 9^2) ~ O(1)
def is_valid_sudoku(board: list[list[str]]) -> bool:
    rows = [set() for _ in range(9)]
    columns = [set() for _ in range(9)]
    squares = [set() for _ in range(9)]

    for row in range(9):
        for column in range(9):
            cell_value = board[row][column]
            if cell_value == EMPTY:
                continue

            square_index = column // 3 + (row // 3) * 3
            if cell_value in rows[row] or \
                    cell_value in columns[column] or \
                    cell_value in squares[square_index]:
                return False
            rows[row].add(cell_value)
            columns[column].add(cell_value)
            squares[square_index].add(cell_value)
    return True


tests.test(is_valid_sudoku)
