def check_rules(number, awesome_phrases):
    snumber = [int(i) for i in str(number)]
    if len(snumber) < 3:
        return False
    if all([i == 0 for i in snumber[1:]]):
        return True
    if all([snumber[i] == snumber[0] for i in range(1, len(snumber))]):
        return True
    if snumber == snumber[::-1]:
        return True
    if number in awesome_phrases:
        return True
    if all(
        [snumber[i + 1] % 10 == (snumber[i] + 1) % 10 for i in range(len(snumber) - 1)]
    ):
        return True
    if all([snumber[i + 1] == (snumber[i] - 1) for i in range(len(snumber) - 1)]):
        return True
    return False


def is_interesting(number, awesome_phrases):
    if check_rules(number, awesome_phrases):
        return 2
    if check_rules(number + 1, awesome_phrases) or check_rules(
        number + 2, awesome_phrases
    ):
        return 1
    return 0
