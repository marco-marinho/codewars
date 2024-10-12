def rgb(r, g, b):
    return (
        f"{max(min(r, 255), 0):02x}"
        f"{max(min(g, 255), 0):02x}"
        f"{max(min(b, 255), 0):02x}"
    ).upper()
