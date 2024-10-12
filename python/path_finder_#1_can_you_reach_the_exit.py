def path_finder(maze):
    maze = [list(line) for line in maze.split("\n")]
    rows, cols = len(maze), len(maze[0])
    visited = set()
    queue = [(0, 0)]
    while len(queue) > 0:
        x, y = queue.pop()
        if (x, y) in visited:
            continue
        if x == rows - 1 and y == cols - 1:
            return True
        visited.add((x, y))
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] != "W":
                queue.append((nx, ny))
    return False
