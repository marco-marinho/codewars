def sum_for_list(lst):
    original = [i for i in lst]
    lst = [abs(i) for i in lst]
    output = {}
    for idx in range(len(lst)):
        divided = False
        while lst[idx] != 0 and lst[idx] % 2 == 0:
            divided = True
            lst[idx] //= 2
        if divided:
            output[2] = output.get(2, 0) + original[idx]
        for i in range(3, lst[idx], 2):
            if lst[idx] == 1:
                break
            divided = False
            while lst[idx] % i == 0:
                lst[idx] //= i
                divided = True
            if divided:
                output[i] = output.get(i, 0) + original[idx]
        if lst[idx] != 1:
            output[lst[idx]] = output.get(lst[idx], 0) + original[idx]
    return sorted([[key, value] for key, value in output.items()], key=lambda x: x[0])
