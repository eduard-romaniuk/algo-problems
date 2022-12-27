import tests


# Time O(n^2)
# Space O(n^2)
def four_number_sum(array, target_sum):
    sums = {}
    result = []
    for i, n1 in enumerate(array[1:-1], start=1):
        for n2 in array[i + 1:]:
            current_sum = n1 + n2
            difference = target_sum - current_sum
            for pair in sums.get(difference, []):
                result.append(pair + [n1, n2])
        for n2 in array[:i]:
            current_sum = n1 + n2
            if current_sum not in sums:
                sums[current_sum] = []
            sums[current_sum].append([n2, n1])
    return result


tests.test(four_number_sum)
