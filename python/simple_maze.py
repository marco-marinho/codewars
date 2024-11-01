def has_exit(maze):
    maze = [list(entry) for entry in maze]
    rows = len(maze)
    cols = len(maze[0])
    kates = [(i, j) for i in range(rows) for j in range(cols) if maze[i][j] == "k"]
    if len(kates) != 1:
        return False
    stack = [kates[0]]
    steps = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while stack:
        i, j = stack.pop()
        if i == 0 or j == 0 or i == rows - 1 or j == cols - 1:
            return True
        for dx, dy in steps:
            x, y = i + dx, j + dy
            if 0 <= x < rows and 0 <= y < cols and maze[x][y] == " ":
                maze[x][y] = "v"
                stack.append((x, y))
    return False
