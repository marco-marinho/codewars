def rot13(message):
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower = upper.lower()
    output = ""
    for i in message:
        if i in upper:
            output += upper[(upper.index(i) + 13) % 26]
        elif i in lower:
            output += lower[(lower.index(i) + 13) % 26]
        else:
            output += i
    return output
