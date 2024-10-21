def hamming(n):
    h = [1] * n
    i, j, k = 0, 0, 0
    x, y, z = 2, 3, 5
    for p in range(1, n):
        h[p] = min(x, y, z)
        if h[p] == x:
            i += 1
            x *= 2
        elif h[p] == y:
            j += 1
            y *= 3
        else:
            k += 1
            z *= 5
    return h[-1]
