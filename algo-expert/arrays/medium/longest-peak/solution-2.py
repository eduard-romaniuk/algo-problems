import tests


# Time O(n)
# Space O(1)
def longest_peak(array):
    highest_peak = 0
    i = 1

    while i < len(array) - 1:
        if not (array[i] > array[i - 1] and array[i] > array[i + 1]):
            i += 1
            continue

        left = i - 1
        while left > 0 and array[left - 1] < array[left]:
            left -= 1

        right = i + 1
        while right < len(array) - 1 and array[right] > array[right + 1]:
            right += 1

        highest_peak = max(highest_peak, right - left + 1)
        i = right

    return highest_peak


tests.test(longest_peak)
