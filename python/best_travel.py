import itertools


def choose_best_sum(t, k, ls):
    sums = list(filter(lambda x: x <= t, [sum(combination) for combination in itertools.combinations(ls, k)]))
    return max(sums) if sums else None
