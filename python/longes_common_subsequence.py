def lcs(x, y):
    memo = {}

    def aux(x, y):
        if (x, y) in memo:
            return memo[(x, y)]
        if not x or not y:
            return ""
        if x[-1] == y[-1]:
            result = aux(x[:-1], y[:-1]) + x[-1]
        else:
            a = aux(x[:-1], y)
            b = aux(x, y[:-1])
            result = a if len(a) > len(b) else b
        memo[(x, y)] = result
        return result

    return aux(x, y)
