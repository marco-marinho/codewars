def last_digit(n1, n2):
    if n2 == 0:
        return 1
    return ((n1 % 10) ** ((n2 % 4) + 4)) % 10
