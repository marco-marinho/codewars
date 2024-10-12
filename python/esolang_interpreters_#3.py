def interpreter(code, iterations, width, height):
    code = list(filter(lambda x: x in ("*", "n", "s", "w", "e", "[", "]"), code))
    mem = [[0] * width for _ in range(height)]
    ptr = [0, 0]
    jumps, stack = {}, []
    for idx, c in enumerate(code):
        if c == "[":
            stack.append(idx)
        elif c == "]":
            jumps[stack[-1]] = idx
            jumps[idx] = stack.pop()
    iptr = -1
    while iptr < len(code) - 1 and iterations > 0:
        iterations -= 1
        iptr += 1
        inst = code[iptr]
        if inst == "*":
            mem[ptr[0]][ptr[1]] = not mem[ptr[0]][ptr[1]]
        elif inst == "n":
            ptr[0] = (ptr[0] - 1) % height
        elif inst == "s":
            ptr[0] = (ptr[0] + 1) % height
        elif inst == "w":
            ptr[1] = (ptr[1] - 1) % width
        elif inst == "e":
            ptr[1] = (ptr[1] + 1) % width
        elif inst == "[" and not mem[ptr[0]][ptr[1]]:
            iptr = jumps[iptr]
        elif inst == "]" and mem[ptr[0]][ptr[1]]:
            iptr = jumps[iptr]
    return "\r\n".join(
        ["".join(["1" if entry else "0" for entry in row]) for row in mem]
    )
