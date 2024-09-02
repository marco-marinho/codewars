import re
def generate_hashtag(s):
    if not s:
        return False
    ans = "#" + "".join(entry.title() for entry in re.sub(r" +", " ", s.strip()).split(" "))
    if len(ans) > 140:
        return False
    return ans