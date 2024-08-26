def stream(x):
    for i in x[::-1]:
        yield i
    while True:
        yield "0"


def sum_strings(x, y):
    carry_on = 0
    output = []
    size = max(len(x), len(y))
    stream_x = stream(x)
    stream_y = stream(y)
    for i in range(size):
        a, b = next(stream_x), next(stream_y)
        res = int(a) + int(b) + carry_on
        output.append((res % 10))
        carry_on = res // 10
    if carry_on != 0:
        output.append(carry_on)
    output = "".join(map(str, output))[::-1].lstrip("0")
    if not output:
        return "0"
    return output
