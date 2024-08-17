from itertools import zip_longest, chain


def helper(src, n):
    ar, br = range((n - 2) * 2 + 2, -1, -2), range(0, (n - 2) * 2 + 3, 2)
    output = []
    for i in range(min(n, len(src))):
        output.append(src[i])
        a, b = ar[i], br[i]
        first = src[i + a::a + b] if a > 0 else ""
        second = src[i + a + b::b + a] if b > 0 else ""
        output.extend(chain.from_iterable(zip_longest(first, second, fillvalue=None)))
    return [i for i in output if i is not None]


def encode_rail_fence_cipher(string, n):
    return "".join(helper(string, n))


def decode_rail_fence_cipher(string, n):
    output = [""] * len(string)
    for i, element in zip(helper(range(len(string)), n), string):
        output[i] = element
    return "".join(output)
