from collections import Counter
from functools import reduce
from math import factorial


def list_position(word):
    count = Counter(word)
    idx = 1
    for i in range(len(word)):
        possible = factorial(len(word) - i) // reduce(
            lambda x, y: x * y, [factorial(entry) for entry in count.values()]
        )
        for entry in set(word):
            if entry < word[i]:
                idx += possible * count[entry] // (len(word) - i)
        count[word[i]] -= 1
    return idx
