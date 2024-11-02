def product_fib(prod):
    n, m = 0, 1
    while n * m < prod:
        n, m = m, n + m
    return [n, m, n * m == prod]
