def sum_of_intervals(intervals):
    intervals = sorted(intervals)
    merged_intervals = [list(intervals[0])]
    for interval in intervals[1:]:
        if interval[0] <= merged_intervals[-1][1]:
            merged_intervals[-1][1] = max(merged_intervals[-1][1], interval[1])
        else:
            merged_intervals.append(list(interval))
    return sum(map(lambda x: x[1] - x[0], merged_intervals))
