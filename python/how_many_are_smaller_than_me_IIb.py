def merge_sort(arr, counts):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid], counts)
    right = merge_sort(arr[mid:], counts)
    return merge(left, right, counts)


def merge(left, right, counts):
    result = [0] * (len(left) + len(right))
    l, r, i = 0, 0, 0
    while i < len(result):
        if r >= len(right) or (l < len(left) and left[l][0] <= right[r][0]):
            result[i] = left[l]
            counts[left[l][1]] += r
            l += 1
        else:
            result[i] = right[r]
            r += 1
        i += 1
    return result


def smaller(arr):
    ans = [0] * len(arr)
    arr = [(el, idx) for idx, el in enumerate(arr)]
    merge_sort(arr, ans)
    return ans
