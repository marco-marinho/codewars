def balanced_recurse(current, open, closed, target, solutions):
    if open == target and closed == target:
        solutions.append(current)
    if closed < open:
        balanced_recurse(current + ")", open, closed + 1, target, solutions)
    if open < target:
        balanced_recurse(current + "(", open + 1, closed, target, solutions)


def balanced_parens(n):
    solutions = []
    balanced_recurse("", 0, 0, n, solutions)
    return solutions
