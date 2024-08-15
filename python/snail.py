import numpy as np


def snail_step(snail_map):
    if snail_map.shape[0] == 0:
        return np.array([])
    if snail_map.shape[0] == 1:
        return snail_map[0]
    result = np.r_[snail_map[0, :], snail_map[1:-1, -1], snail_map[-1, ::-1], snail_map[1:-1, 0][::-1]]
    return np.r_[result, snail(snail_map[1:-1, 1:-1])]


def snail(snail_map):
    return snail_step(np.array(snail_map)).tolist()
