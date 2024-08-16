from itertools import zip_longest, chain


def helper(src, n):
    a, b = (n - 2) * 2 + 2, 0
    output = []
    for i in range(min(n, len(src))):
        output.append(src[i])
        first = src[i + a::a + b] if a > 0 else ""
        second = src[i + a + b::b + a] if b > 0 else ""
        output.extend(chain.from_iterable(zip_longest(first, second, fillvalue="")))
        a -= 2
        b += 2
    return [i for i in output if i != ""]


def encode_rail_fence_cipher(string, n):
    return "".join(helper(string, n))


def decode_rail_fence_cipher(string, n):
    idxs = helper(range(len(string)), n)
    output = [""] * len(string)
    for i, element in zip(idxs, string):
        output[i] = element
    return "".join(output)
