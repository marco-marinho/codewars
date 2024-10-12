import re


def generate_hashtag(s):
    ans = "#" + "".join(
        entry.title() for entry in re.sub(r" +", " ", s.strip()).split(" ")
    )
    if len(ans) > 140 or not s:
        return False
    return ans
