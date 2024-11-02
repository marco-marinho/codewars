from collections import Counter

scores = {1: 1000, 6: 600, 5: 500, 4: 400, 3: 300, 2: 200}


def score(dice):
    score = 0
    counts = Counter(dice)
    for entry, value in scores.items():
        if entry in counts and counts[entry] >= 3:
            score += value
            counts[entry] -= 3
    if 1 in counts:
        score += counts[1] * 100
    if 5 in counts:
        score += counts[5] * 50
    return score
