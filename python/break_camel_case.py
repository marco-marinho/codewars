import re


def solution(s):
    words = re.findall(r"^[a-z]+|[A-Z][^A-Z]*", s)
    return " ".join(words)
