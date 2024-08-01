def solution(number):
    output = sum(range(3, number, 3))
    output += sum([i for i in range(5, number, 5) if i % 3 != 0])
    return output
