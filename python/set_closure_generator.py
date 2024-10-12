import heapq


def closure_gen(*s):
    if 1 in s:
        yield 1
    h = []
    s = list(filter(lambda x: x != 1, s))
    for element in s:
        heapq.heappush(h, element)
    last = None
    while True:
        if not h:
            return
        next_val = heapq.heappop(h)
        if next_val != last:
            last = next_val
            for element in s:
                heapq.heappush(h, next_val * element)
            yield next_val
