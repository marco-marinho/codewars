def ips_between(start, end):
    parts_start = [int(part) for part in start.split(".")][::-1]
    parts_end = [int(part) for part in end.split(".")][::-1]
    diff = 0
    multiplier = 1
    for end, start in zip(parts_end, parts_start):
        diff += (end - start) * multiplier
        multiplier *= 256
    return diff
