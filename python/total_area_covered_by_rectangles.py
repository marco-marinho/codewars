import bisect
def calculate(rectangles):
    events = []

    for (x0, y0, x1, y1) in rectangles:
        events.append((x0, y0, y1, 1))  # Start event
        events.append((x1, y0, y1, -1))  # End event

    events.sort()

    prev_x = events[0][0]
    active_intervals = []
    total_area = 0

    def compute_y_length():
        y_length = 0
        prev_y = -1
        for (start, end) in active_intervals:
            prev_y = max(prev_y, start)
            y_length += max(0, end - prev_y)
            prev_y = max(prev_y, end)
        return y_length

    for x, y0, y1, typ in events:
        y_length = compute_y_length()
        total_area += y_length * (x - prev_x)
        prev_x = x

        if typ == 1:
            bisect.insort(active_intervals, (y0, y1))
        else:
            del active_intervals[bisect.bisect_left(active_intervals, (y0, y1))]

    return total_area