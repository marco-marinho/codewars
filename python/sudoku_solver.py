def is_valid(puzzle, row, col, num):
    for x in range(9):
        if puzzle[x][col] == num:
            return False
        if puzzle[row][x] == num:
            return False
    x_offset = (row // 3) * 3
    y_offset = (col // 3) * 3
    for x in range(3):
        for y in range(3):
            if puzzle[x_offset + x][y_offset + y] == num:
                return False
    return True


def solve(puzzle, unfilled_pos):
    if not unfilled_pos:
        return puzzle
    x, y = unfilled_pos.pop()
    for num in range(1, 10):
        if is_valid(puzzle, x, y, num):
            puzzle[x][y] = num
            if solve(puzzle, unfilled_pos):
                return puzzle
            puzzle[x][y] = 0
    unfilled_pos.append((x, y))
    return None


def sudoku(puzzle):
    unfilled_pos = [(x, y) for x, line in enumerate(puzzle) for y, entry in enumerate(line) if entry == 0]
    return solve(puzzle, unfilled_pos)


puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
          [6, 0, 0, 1, 9, 5, 0, 0, 0],
          [0, 9, 8, 0, 0, 0, 0, 6, 0],
          [8, 0, 0, 0, 6, 0, 0, 0, 3],
          [4, 0, 0, 8, 0, 3, 0, 0, 1],
          [7, 0, 0, 0, 2, 0, 0, 0, 6],
          [0, 6, 0, 0, 0, 0, 2, 8, 0],
          [0, 0, 0, 4, 1, 9, 0, 0, 5],
          [0, 0, 0, 0, 8, 0, 0, 7, 9]]

print(sudoku(puzzle))