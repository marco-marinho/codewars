def rule30(list_, n):
    output = "".join([str(entry) for entry in list_])

    for _ in range(n):
        output = "00" + output + "00"
        buffer = ""
        for i in range(1, len(output) - 1):
            print(output[i - 1 : i + 2])
            if output[i - 1 : i + 2] in ("001", "010", "011", "100"):
                buffer += "1"
            else:
                buffer += "0"
        output = buffer
    return [int(c) for c in output]
