import numpy as np


def generate_primes(n):
    prime = np.full(n, True)
    prime[0:2] = False
    for i in range(int(np.sqrt(n)) + 1):
        if prime[i]:
            prime[range(i * 2, n, i)] = False
    return np.argwhere(prime)


class Primes:
    n = 16000000
    all_primes = generate_primes(n)

    @staticmethod
    def stream():
        yield from Primes.all_primes
