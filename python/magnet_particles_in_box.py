import numpy as np


def doubles(maxk, maxn):
    total = 0
    for k in range(1, maxk + 1):
        row = (1 / (k * np.arange(2, maxn + 2) ** (2 * k)))
        total += np.ma.masked_invalid(row).sum()
    return total
