def next_smaller(n):
    digits = [int(i) for i in str(n)]
    end = len(digits) - 1
    index_1 = end - 1
    while index_1 >= 0:
        index_2 = end
        while index_2 > index_1:
            if digits[index_2] < digits[index_1]:
                digits[index_2], digits[index_1] = digits[index_1], digits[index_2]
                head = digits[0 : index_1 + 1]
                tail = digits[index_1 + 1 :]
                tail.sort(reverse=True)
                digits = head + tail
                if digits[0] == 0:
                    return -1
                return int("".join(str(i) for i in digits))
            else:
                index_2 -= 1
        index_1 -= 1
    return -1
