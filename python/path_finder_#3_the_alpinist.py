from heapq import heappush, heappop


def path_finder(area):
    area = [list(map(int, list(line))) for line in area.split("\n")]
    rows, cols = len(area), len(area[0])
    queue = []
    visited = set()
    heappush(queue, (0, (0, 0)))
    delta = ((1, 0), (-1, 0), (0, 1), (0, -1))
    while len(queue) > 0:
        dist, (x, y) = heappop(queue)
        if (x, y) in visited:
            continue
        if x == rows - 1 and y == cols - 1:
            return dist
        visited.add((x, y))
        for dx, dy in delta:
            if 0 <= x + dx < rows and 0 <= y + dy < cols:
                new_dist = dist + abs(area[x][y] - area[x + dx][y + dy])
                heappush(queue, (new_dist, (x + dx, y + dy)))
    return -1
