def solution(array_a, array_b):
    return sum([(a - b) ** 2 for a, b in zip(array_a, array_b)]) / len(array_a)
