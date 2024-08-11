def strip_comments(strng, markers):
    marker_pos = [i for i, e in enumerate(strng) if e in markers]
    if not marker_pos:
        return strng
    break_pos = [i for i, e in enumerate(strng) if e == "\n"] + [len(strng)]
    output = ""
    midx = bidx = cidx = 0
    while cidx < len(strng) and midx < len(marker_pos):
        output += strng[cidx:marker_pos[midx]].rstrip(" \t")
        while break_pos[bidx] < marker_pos[midx]:
            bidx += 1
        cidx = break_pos[bidx]
        midx += 1
    output += strng[cidx:]
    return output

