from functools import cmp_to_key


def sorter(a, b):
    a_sum = sum([ord(i) - ord("0") for i in a])
    b_sum = sum([ord(i) - ord("0") for i in b])
    if a_sum > b_sum:
        return 1
    if b_sum > a_sum:
        return -1
    if a > b:
        return 1
    return -1


def order_weight(strng):
    return " ".join(sorted(strng.strip().split(" "), key=cmp_to_key(sorter)))
