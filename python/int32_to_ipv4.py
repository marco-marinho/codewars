def int32_to_ip(int32):
    return f"{int32 >> 24 & 255}.{int32 >> 16 & 255}.{int32 >> 8 & 255}.{int32 & 255}"