def alphabet_position(text):
    return " ".join([str(ord(entry) - ord("a") + 1) for entry in filter(lambda x: x.isalpha(), text.lower())])