def last_digit(lst):
    if not lst:
        return 1
    output = 1
    for exponent in lst[::-1]:
        output = exponent ** (output if output < 4 else (output % 4) + 4)
    return output % 10
