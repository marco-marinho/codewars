from preloaded import MORSE_CODE


def decode_morse(morse_code):
    MORSE_CODE["|"] = " "
    components = morse_code.strip().replace("   ", " | ").split(" ")
    output = [MORSE_CODE[entry] for entry in components]
    return "".join(output)
