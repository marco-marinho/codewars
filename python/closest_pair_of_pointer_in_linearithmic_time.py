import numpy as np
from numpy.typing import NDArray


def brute_force(points: NDArray):
    d = np.inf
    pair = None
    for i in range(points.shape[0]):
        for j in range(i + 1, points.shape[0]):
            if (nd := np.linalg.norm(points[i, :] - points[j, :])) < d:
                pair = (points[i, :], points[j, :])
                d = nd
    return pair, d


def strip_closest(points: NDArray, d):
    points_temp = points[np.argsort(points[:, 1])]
    res = d
    pair = None
    for i in range(points.shape[0]):
        for j in range(i + 1, points.shape[0]):
            if points_temp[j, 1] - points_temp[i, 1] >= d:
                break
            if (nres := np.linalg.norm(points_temp[j, :] - points_temp[i, :])) < res:
                pair = (points_temp[i, :], points_temp[j, :])
                res = nres
    if pair is None:
        return None, np.inf
    return pair, res


def closest_recurse(points: NDArray, p, d):
    if points.shape[0] <= 3:
        p0, d0 = brute_force(points)
        if d0 < d:
            return p0, d0
        return p, d
    p1, d1 = closest_recurse(points[: points.shape[0] // 2], p, d)
    p2, d2 = closest_recurse(points[points.shape[0] // 2 :], p, d)
    if d1 < d:
        p, d = p1, d1
    if d2 < d:
        p, d = p2, d2
    strip = points[np.abs(points[:, 0] - points[points.shape[0] // 2, 0]) < d]
    p3, d3 = strip_closest(strip, d)
    if d3 < d:
        p, d = p3, d3
    return p, d


def closest_pair(points):
    points = np.array(points, dtype=np.float128)
    points = points[np.argsort(points[:, 0]), :]
    p, d = closest_recurse(points, None, np.inf)
    return tuple(p[0]), tuple(p[1])
