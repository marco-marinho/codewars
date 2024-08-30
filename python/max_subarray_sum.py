def max_sequence(arr):
    if not arr:
        return 0
    output = [0] * (len(arr) + 1)
    output[0] = arr[0]
    for idx in range(1, len(arr)):
        output[idx] = max(arr[idx], arr[idx] + output[idx - 1])
    return max(output)