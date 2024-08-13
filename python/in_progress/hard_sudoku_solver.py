import numpy as np


def get_valid(puzzle, row, col):
    valid = set(range(1, 10))
    valid -= set(puzzle[row, :].flatten())
    valid -= set(puzzle[:, col].flatten())
    x_offset = (row // 3) * 3
    y_offset = (col // 3) * 3
    valid -= set(puzzle[x_offset:x_offset + 3, y_offset:y_offset + 3].flatten())
    return valid


def solve(puzzle, unfilled_pos, idx, results):
    if idx >= len(unfilled_pos):
        return True
    x, y = unfilled_pos[idx]
    for num in get_valid(puzzle, x, y):
        puzzle[x, y] = num
        if solve(puzzle, unfilled_pos, idx + 1, results):
            return True
        puzzle[x, y] = 0
    return False


def sudoku_solver(puzzle):
    puzzle = np.array(puzzle)
    unfilled_pos = list(zip(*np.where(puzzle == 0)))
    results = []
    solve(puzzle, unfilled_pos, 0, results)
    return puzzle.tolist()


puzzle = [
  [0,8,0, 0,0,9, 7,4,3],
  [0,5,0, 0,0,8, 0,1,0],
  [0,1,0, 0,0,0, 0,0,0],

  [8,0,0, 0,0,5, 0,0,0],
  [0,0,0, 8,0,4, 0,0,0],
  [0,0,0, 3,0,0, 0,0,6],

  [0,0,0, 0,0,0, 0,7,0],
  [0,3,0, 5,0,0, 0,8,0],
  [9,7,2, 4,0,0, 0,5,0]
]

print(sudoku_solver(puzzle))
