def decode_bits(bits):
    ibits = bits.strip("0")
    prev, count, buff = ibits[0], 1, []
    for bit in [*ibits[1:], "e"]:
        if bit == prev:
            count += 1
        else:
            buff.append((prev, count))
            prev = bit
            count = 1
    time_unit = min([count for _, count in buff])
    output = ""
    for entry, count in buff:
        if entry == "1" and count / time_unit == 1:
            output += "."
        elif entry == "1" and count / time_unit == 3:
            output += "-"
        elif entry == "0" and count / time_unit == 3:
            output += " "
        elif entry == "0" and count / time_unit == 7:
            output += "   "
    return output


def decode_morse(morseCode):
    words = morseCode.split("   ")
    output = []
    for word in words:
        current = ""
        for char in word.split(" "):
            current += MORSE_CODE[char]
        output.append(current)
    return " ".join(output)
