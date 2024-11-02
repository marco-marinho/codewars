def height(n, m):
    if n == 0 or m == 0:
        return 0
    if n > m:
        return height(m, m)
    c = 1
    b = 1
    a = 0
    while c <= n:
        b = (m + 1 - c) * b // c
        c += 1
        a += b
    return a
