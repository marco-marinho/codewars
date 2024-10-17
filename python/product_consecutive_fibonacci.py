def product_fib(_prod):
    def aux(n, m, t):
        if n * m == t:
            return [n, m, True]
        elif n * m > t:
            return [n, m, False]
        return aux(m, n+m, t)
    return aux(0, 1, _prod)