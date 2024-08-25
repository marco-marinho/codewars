def my_first_interpreter(code):
    mem = 0
    output = ""
    for entry in code:
        if entry == "+":
            mem += 1
            if mem == 256:
                mem = 0
        elif entry == ".":
            output += chr(mem)
    return output
