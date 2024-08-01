def count(s):
    output = {}
    for entry in s:
        output[entry] = output.get(entry, 0) + 1
    return output
