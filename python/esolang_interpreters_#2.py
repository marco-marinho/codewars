def interpreter(code, tape):
    mem = [c == "1" for c in tape]
    pointer = 0
    iptr = 0
    while iptr < len(code) and 0 <= pointer < len(mem):
        inst = code[iptr]
        if inst == "*":
            mem[pointer] = not mem[pointer]
        elif inst == ">":
            pointer += 1
        elif inst == "<":
            pointer -= 1
        elif inst == "[" and not mem[pointer]:
            temp = 1
            iptr += 1
            while temp:
                if code[iptr] == "[":
                    temp += 1
                elif code[iptr] == "]":
                    temp -= 1
                iptr += 1
            iptr -= 1
        elif inst == "]" and mem[pointer]:
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
    return "".join(["1" if entry else "0" for entry in mem])
