def dfs(grid, current, left, memo):
    if (str(grid), current, left) in memo:
        return memo[(str(grid), current, left)]
    if left == 0:
        return 1
    count = 0
    coords = [(x, y) for x in range(3) for y in range(3)]
    for x, y in coords:
        if grid[x][y]:
            continue
        if (half_x := (current[0] + x) / 2).is_integer() and (half_y := (current[1] + y) / 2).is_integer():
            if not grid[int(half_x)][int(half_y)]:
                continue
        grid[x][y] = 1
        count += dfs(grid, (x, y), left - 1, memo)
        grid[x][y] = 0
    memo[(str(grid), current, left)] = count
    return count


def count_patterns_from(firstPoint, length):
    if length == 1:
        return 1
    if length == 0:
        return 0
    grid = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
    points = {"A": (0, 0), "B": (0, 1), "C": (0, 2),
              "D": (1, 0), "E": (1, 1), "F": (1, 2),
              "G": (2, 0), "H": (2, 1), "I": (2, 2)}
    x, y = points[firstPoint]
    grid[x][y] = 1
    return dfs(grid, (x, y), length - 1, points)
