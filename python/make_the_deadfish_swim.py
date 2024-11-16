def parse(data):
    v = 0
    output = []
    for c in data:
        if c == "i":
            v += 1
        elif c == "d":
            v -= 1
        elif c == "o":
            output.append(v)
        elif c == "s":
            v *= v
    return output
