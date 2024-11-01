import numpy as np


def generate_primes(n):
    prime = np.full(n, True)
    prime[0:2] = False
    for i in range(int(np.sqrt(n)) + 1):
        if prime[i]:
            prime[range(i * 2, n, i)] = False
    return np.argwhere(prime).flatten()


def prime_factors(n):
    primes = generate_primes(int(np.sqrt(n)))
    factors = []
    for prime in primes:
        i = 0
        if n % prime == 0:
            while n % prime == 0:
                n = n // prime
                i += 1
            if i > 0:
                factors.append((prime, i))
        if n == 1:
            break
    if n != 1:
        factors.append((n, 1))
    return "".join(
        [
            f"({factor[0]}**{factor[1]})" if factor[1] > 1 else f"({factor[0]})"
            for factor in factors
        ]
    )
