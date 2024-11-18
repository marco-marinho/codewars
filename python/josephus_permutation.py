def josephus(items, k):
    idx = -1
    taken = [1] * len(items)
    acc = []
    while any(taken):
        x = k
        while x > 0:
            idx = (idx + 1) % len(items)
            x -= taken[idx]
        taken[idx] = 0
        acc.append(items[idx])
    return acc
