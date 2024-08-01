import re


def to_camel_case(text):
    words = [word for word in re.split("[-_]", text)]
    return "".join([words[0], *map(lambda x: x.capitalize(), words[1:])])
