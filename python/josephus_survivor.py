import sys

sys.setrecursionlimit(5000)


def josephus_survivor(items, k):
    if items == 1:
        return 1
    return ((josephus_survivor(items - 1, k) + k - 1) % items) + 1
