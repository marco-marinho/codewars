def likes(names):
    if not names:
        return "no one likes this"
    if len(names) == 1:
        return f"{names[0]} likes this"
    if 1 < len(names) < 4:
        return f"{', '.join(names[:-1])} and {names[-1]} like this"
    return f"{', '.join(names[:2])} and {len(names) - 2} others like this"
