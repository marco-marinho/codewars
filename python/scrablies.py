from collections import Counter


def scramble(s1, s2):
    counts = Counter(s1)
    for c in s2:
        if c not in counts or counts[c] == 0:
            return False
        counts[c] -= 1
    return True
