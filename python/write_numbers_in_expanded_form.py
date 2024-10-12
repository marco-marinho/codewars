def expanded_form(num):
    num = str(num)
    output = [
        entry + "0" * (len(num) - idx - 1)
        for idx, entry in enumerate(num)
        if entry != "0"
    ]
    return " + ".join(output)
