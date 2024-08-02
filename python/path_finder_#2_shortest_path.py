from collections import deque


def path_finder(maze):
    data = [list(line) for line in maze.split('\n')]
    data[0][0] = 0
    queue = deque()
    queue.appendleft((0, 0))
    while queue:
        x, y = queue.popleft()
        if x == len(data) - 1 and y == len(data[0]) - 1:
            return data[x][y]
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(data) and 0 <= ny < len(data[0]) and data[nx][ny] == '.':
                data[nx][ny] = data[x][y] + 1
                queue.append((nx, ny))
    return False
