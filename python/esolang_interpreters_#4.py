def boolfuck(code, input=""):
    input = [entry == "1" for num in input for entry in format(ord(num), "08b")[::-1]]
    mem = {}
    output = []
    ptr, iptr = 0, 0

    jumps, stack = {}, []
    for idx, c in enumerate(code):
        if c == "[":
            stack.append(idx)
        elif c == "]":
            jumps[stack[-1]] = idx
            jumps[idx] = stack.pop()

    while iptr < len(code):
        inst = code[iptr]
        if inst == "+":
            mem[ptr] = not mem.get(ptr, False)
        elif inst == ",":
            mem[ptr] = input.pop() if input else False
        elif inst == ";":
            output.append(mem.get(ptr, False))
        elif inst == "<":
            ptr -= 1
        elif inst == ">":
            ptr += 1
        elif inst == "[" and not mem.get(ptr, False):
            iptr = jumps[iptr]
        elif inst == "]" and mem.get(ptr, False):
            iptr = jumps[iptr]
        iptr += 1
    if len(output) % 8 != 0:
        output.extend([False] * (8 - (len(output) % 8)))
    x = sum(map(lambda x: x[1] << x[0], enumerate(output))).to_bytes(
        len(output) // 8, "little"
    )
    return "".join([chr(a) for a in x])
