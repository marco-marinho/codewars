def longest_slide_down(pyramid):
    def aux (pyramid, idx, level, memo):
        if (idx, level) in memo:
            return memo[(idx, level)]
        if level == len(pyramid) - 1:
            return pyramid[level][idx]
        left = aux(pyramid, idx, level + 1, memo)
        right = aux(pyramid, idx + 1, level + 1, memo)
        res = max(left, right) + pyramid[level][idx]
        memo[(idx, level)] = res
        return res
    return aux(pyramid, 0, 0, {})