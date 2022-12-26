import tests


def find_peak_size(peak_center, array):
    left = peak_center - 1
    while left > 0 and array[left - 1] < array[left]:
        left -= 1

    right = peak_center + 1
    while right < len(array) - 1 and array[right] > array[right + 1]:
        right += 1

    return right - left + 1


# Time O(n)
# Space O(1)
def longest_peak(array):
    if len(array) < 3:
        return 0
    highest_peak = 0
    for i in range(1, len(array) - 1):
        if array[i] > array[i - 1] and array[i] > array[i + 1]:
            highest_peak = max(find_peak_size(i, array), highest_peak)
    return highest_peak


tests.test(longest_peak)
