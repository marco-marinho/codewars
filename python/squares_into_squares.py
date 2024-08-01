from math import isqrt


def decompose(n, left=None):
    if left is None:
        left = n * n
    if left == 0:
        return []
    for current in range(min(n - 1, isqrt(left)), 0, -1):
        nxt_elements = decompose(current, left - current * current)
        if nxt_elements is not None:
            return nxt_elements + [current]
