def interpreter(code, iterations, width, height):
    mem = [[0] * width for _ in range(height)]
    iptr = 0
    ptr = [0, 0]
    while iptr < len(code) and iterations > 0:
        inst = code[iptr]
        if inst not in ("*", "n", "s", "w", "e", "[", "]"):
            iptr += 1
            continue
        iterations -= 1
        if inst == "*":
            mem[ptr[0]][ptr[1]] = not mem[ptr[0]][ptr[1]]
        elif inst == "n":
            ptr[0] -= 1
            if ptr[0] < 0:
                ptr[0] = height - 1
        elif inst == "s":
            ptr[0] += 1
            if ptr[0] >= height:
                ptr[0] = 0
        elif inst == "w":
            ptr[1] -= 1
            if ptr[1] < 0:
                ptr[1] = width - 1
        elif inst == "e":
            ptr[1] += 1
            if ptr[1] >= width:
                ptr[1] = 0
        elif inst == "[" and not mem[ptr[0]][ptr[1]]:
            temp = 1
            iptr += 1
            while temp:
                if code[iptr] == "[":
                    temp += 1
                elif code[iptr] == "]":
                    temp -= 1
                iptr += 1
            iptr -= 1
        elif inst == "]" and mem[ptr[0]][ptr[1]]:
            temp = 1
            iptr -= 1
            while temp:
                if code[iptr] == "]":
                    temp += 1
                elif code[iptr] == "[":
                    temp -= 1
                iptr -= 1
            iptr += 1
        iptr += 1
    return "\r\n".join(["".join(["1" if entry else "0" for entry in row]) for row in mem])