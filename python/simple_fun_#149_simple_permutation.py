import math


def middle_permutation(string):
    string = sorted(list(string))
    output = ""
    target = math.factorial(len(string)) // 2 - 1
    for idx in range(1, len(string)):
        inner_permutations = math.factorial(len(string) - 1)
        target_idx = target // inner_permutations
        output += string.pop(target_idx)
        target -= inner_permutations * target_idx
    output += string[0]
    return output
