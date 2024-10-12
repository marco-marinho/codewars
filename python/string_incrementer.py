import re


def increment_string(strng):
    match = re.search(r"\d+$", strng)
    if match is None:
        return strng + "1"
    return strng[: match.start()] + str(int(match.group(0)) + 1).zfill(
        len(match.group(0))
    )
