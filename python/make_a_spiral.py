import numpy as np


def spiral(field):
    field[0, :] = 1
    field[:, -1] = 1
    if field.shape[0] > 2:
        field[-1, :] = 1
        field[2:, 0] = 1
        next_field = field[2:-2, 2:-2]
        if next_field.shape[0] == 0:
            return
        field[2, 1] = 1
        spiral(next_field)
    return


def spiralize(size):
    snake = np.zeros((size, size), dtype=int)
    spiral(snake)
    return snake.tolist()
