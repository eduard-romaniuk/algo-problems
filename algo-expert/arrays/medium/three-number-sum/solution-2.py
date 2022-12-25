import tests


# Time O(n^2)
# Space O(n)
def three_number_sum(array, target_sum):
    array.sort()
    results = []
    for i, n in enumerate(array[:-2]):
        start = i + 1
        end = len(array) - 1
        while start < end:
            current_sum = n + array[start] + array[end]
            if current_sum == target_sum:
                results.append([n, array[start], array[end]])
                end -= 1
                start += 1
            elif current_sum > target_sum:
                end -= 1
            else:
                start += 1
    return results


tests.test(three_number_sum)
