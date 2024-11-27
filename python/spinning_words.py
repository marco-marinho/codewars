def spin_words(sentence):
    parts = [entry[::-1] if len(entry) > 4 else entry for entry in sentence.split(" ")]
    return " ".join(parts)
