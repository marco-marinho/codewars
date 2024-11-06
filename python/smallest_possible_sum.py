import math


def solution(lst):
    return math.gcd(*lst) * len(lst)
