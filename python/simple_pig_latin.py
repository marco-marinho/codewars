def pig_it(text):
    output = [x[1:] + x[0] + "ay" if x.isalpha() else x for x in text.split(" ")]
    return " ".join(output)
