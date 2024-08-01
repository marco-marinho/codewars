def pick_peaks(arr):
    output = {"pos": [], "peaks": []}
    if len(arr) < 3:
        return output
    idx = 1
    while idx < len(arr) - 1:
        idx_next = idx + 1
        while idx_next < len(arr) - 1 and arr[idx] == arr[idx_next]:
            idx_next += 1
        if arr[idx - 1] < arr[idx] > arr[idx_next]:
            output["pos"].append(idx)
            output["peaks"].append(arr[idx])
        idx = idx_next
    return output
