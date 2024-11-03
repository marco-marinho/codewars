def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return b

def perimeter(n):
    return (fibonacci(n + 2) - 1)*4