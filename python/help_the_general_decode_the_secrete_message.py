def encode_idx(c, n):
    for i in range(n):
        c = ((c + 1) * 2 - 1) % 67
    return c


def decode(message):
    src = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,? *")
    set_src = set(src)
    output = [""] * len(message)
    for idx, entry in enumerate(message):
        if entry not in set_src:
            output[idx] = entry
            continue
        for i in range(67):
            idx_temp = encode_idx(i, idx + 1)
            if src[idx_temp] == entry:
                output[idx] = src[i]
                break
    return "".join(output)
