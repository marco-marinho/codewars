import re


def solve_runes(runes):
    if not "0" in runes:
        zero_case = runes.replace("?", "0").replace("=", "==")
        if not re.findall("(?<!\d)0\d", zero_case) and eval(zero_case):
            return 0
    for i in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        if i in runes:
            continue
        if eval(runes.replace("?", i).replace("=", "==")):
            return int(i)
    return -1
