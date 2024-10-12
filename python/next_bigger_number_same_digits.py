def next_bigger(n):
    buff = [int(i) for i in str(n)]
    for i in range(len(buff) - 2, -1, -1):
        if buff[i] < buff[i + 1]:
            for j in range(len(buff) - 1, -1, -1):
                if buff[j] > buff[i]:
                    buff[i], buff[j] = buff[j], buff[i]
                    return int(
                        "".join(map(str, buff[: i + 1]))
                        + "".join(map(str, buff[i + 1 :][::-1]))
                    )
    return -1
