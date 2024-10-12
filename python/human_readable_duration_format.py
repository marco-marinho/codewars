def format_duration(seconds):
    if seconds == 0:
        return "now"
    output = []
    name_seconds = (
        ("year", 31536000),
        ("day", 86400),
        ("hour", 3600),
        ("minute", 60),
        ("second", 1),
    )
    for name, value in name_seconds:
        if (count := seconds // value) > 0:
            output.append(f"{count} {name}" + ("s" if count > 1 else ""))
        seconds %= value
    if len(output) == 1:
        return output[0]
    return ", ".join(output[:-1]) + " and " + output[-1]
