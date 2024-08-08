def check_contact(row, col, field):
    delta = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
    for dx, dy in delta:
        x, y = row + dx, col + dy
        if 0 <= x < len(field) and 0 <= y < len(field[0]) and field[x][y] == 2:
            return True
    return False


def visit(row, col, field):
    if check_contact(row, col, field):
        return 0
    visited = 1
    field[row][col] = 2
    while field[row + 1][col] == 1:
        visited += 1
        row += 1
        field[row][col] = 2
    if visited == 1:
        while field[row][col + 1] == 1:
            visited += 1
            col += 1
            field[row][col] = 2
    return visited


def validate_battlefield(field):
    field = [[0] * 10] + field + [[0] * 10]
    for i, row in enumerate(field):
        field[i] = [0] + row + [0]
    ships = {4: 0, 3: 0, 2: 0, 1: 0}
    for row in range(1, 11):
        for col in range(1, 11):
            if field[row][col] == 1:
                visited = visit(row, col, field)
                if visited == 0:
                    return False
                else:
                    if visited not in ships:
                        return False
                    ships[visited] += 1
    valid_ships = [ships[i] == 5 - i for i in range(1, 5)]
    if all(valid_ships):
        return True
