from collections import Counter
from decimal import Decimal
from functools import reduce
from math import factorial


def list_position(word):
    count = Counter(word)
    idx = 1
    for i in range(len(word)):
        possible = Decimal(factorial(len(word) - i)) / reduce(lambda x, y: x * y,
                                                              [Decimal(factorial(entry)) for entry in count.values()])
        for entry in set(word):
            if entry < word[i]:
                idx += Decimal(possible) / (len(word) - i) * count[entry]
        count[word[i]] -= 1
    return idx
