def dbl_linear(n):
    output = [1] * (n + 1)
    pt1 = pt2 = 0
    for i in range(1, n + 1):
        output[i] = min(2 * output[pt1] + 1, 3 * output[pt2] + 1)
        if output[i] == 2 * output[pt1] + 1:
            pt1 += 1
        if output[i] == 3 * output[pt2] + 1:
            pt2 += 1
    return output[n]
