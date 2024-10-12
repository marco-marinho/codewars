from math import factorial
import re


def binomial_coefficient(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k)))


def parse_match(istring):
    if istring == "-":
        return -1
    if istring == "":
        return 1
    return int(istring)


def parse(istring):
    expr = re.compile(r"\((-?[0-9]*)?(\D)([+|-][0-9]*)\)\^([0-9]*)")
    match = expr.match(istring)
    return (
        parse_match(match.group(1)),
        match.group(2),
        int(match.group(3)),
        int(match.group(4)),
    )


def expand(expr):
    a, x, b, n = parse(expr)
    output = ""
    for i in range(n + 1):
        term = binomial_coefficient(n, i) * a ** (n - i) * b**i
        if n - i == 0 or abs(term) != 1:
            output += f"{term:+d}"
        else:
            output += "+" if term == 1 else "-"
        if n - i > 1:
            output += f"{x}^{n - i}"
        elif n - i == 1:
            output += f"{x}"
    return output if output[0] != "+" else output[1:]
