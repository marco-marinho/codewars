def solution(args):
    output = []
    idx1 = idx2 = 0
    while idx2 < len(args):
        if idx2 < len(args) - 1 and args[idx2 + 1] - args[idx2] == 1:
            idx2 += 1
        else:
            if idx2 - idx1 == 1:
                output.extend([f"{args[idx1]}", f"{args[idx2]}"])
            elif idx1 != idx2:
                output.append(f"{args[idx1]}-{args[idx2]}")
            else:
                output.append(f"{args[idx1]}")
            idx2 += 1
            idx1 = idx2
    return ",".join(output)
