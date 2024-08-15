def fib(n):
    if n < 0:
        if n % 2 == 0:
            return -fib_recursive(1, 0, 0, 1, abs(n))
        else:
            return fib_recursive(1, 0, 0, 1, abs(n))
    return fib_recursive(1, 0, 0, 1, n)


def fib_recursive(a, b, p, q, count):
    if count == 0:
        return b
    if count % 2 == 0:
        return fib_recursive(a, b, p ** 2 + q ** 2, 2 * p * q + q ** 2, count / 2)
    else:
        return fib_recursive(b * q + a * q + a * p, b * p + a * q, p, q, count - 1)
