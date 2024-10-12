from collections import Counter


def first_non_repeating_letter(s):
    if not s:
        return ""
    count = Counter(s.lower())
    for c in s:
        if count[c.lower()] == 1:
            return c
    return ""
