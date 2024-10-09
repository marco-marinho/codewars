def simple_assembler(program):
    iptr = 0
    register = {}
    while iptr < len(program):
        instruction = program[iptr]
        parts = instruction.split(" ")
        if parts[0] == "mov":
            if parts[2].isalpha():
                register[parts[1]] = register[parts[2]]
            else:
                register[parts[1]] = int(parts[2])
        elif parts[0] == "inc":
            register[parts[1]] += 1
        elif parts[0] == "dec":
            register[parts[1]] -= 1
        elif parts[0] == "jnz":
            if parts[1].isalpha():
                if register[parts[1]] != 0:
                    iptr += int(parts[2])
                    continue
            else:
                if parts[1] != 0:
                    iptr += int(parts[2])
                    continue
        iptr += 1
    return register
