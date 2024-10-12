from collections import Counter


def find_it(seq):
    for key, val in Counter(seq).items():
        if val % 2 == 1:
            return key
    return None
