def recurse(entries, cur):
    if all(v == 0 for v in entries.values()):
        return [cur]
    output = []
    for c, num in entries.items():
        if num == 0:
            continue
        entries[c] -= 1
        if ans := recurse(entries, cur + c):
            output.extend(ans)
        entries[c] += 1
    return output


def permutations(s):
    entries = {}
    for c in s:
        entries[c] = entries.get(c, 0) + 1
    return recurse(entries, "")
