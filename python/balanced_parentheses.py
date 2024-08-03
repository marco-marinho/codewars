def balanced_recurse(current, opened, closed, target, solutions):
    if opened == target and closed == target:
        solutions.append(current)
    if closed < opened:
        balanced_recurse(current + ")", opened, closed + 1, target, solutions)
    if opened < target:
        balanced_recurse(current + "(", opened + 1, closed, target, solutions)


def balanced_parens(n):
    solutions = []
    balanced_recurse("", 0, 0, n, solutions)
    return solutions
