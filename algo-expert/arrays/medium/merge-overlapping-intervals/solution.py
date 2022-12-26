import tests


# Time O(n*log(n))
# Space O(n)
def merge_overlapping_intervals(intervals):
    intervals.sort()
    result = [intervals[0]]
    for interval in intervals[1:]:
        if result[-1][1] >= interval[0]:
            if result[-1][1] < interval[1]:
                result[-1][1] = interval[1]
        else:
            result.append(interval)
    return result


tests.test(merge_overlapping_intervals)
