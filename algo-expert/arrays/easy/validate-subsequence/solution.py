import tests


# Time: O(n)
# Space: O(1)
def is_valid_subsequence(array, sequence):
    i = 0
    for number in array:
        if number == sequence[i]:
            i += 1
        if i == len(sequence):
            return True
    return False


tests.test(is_valid_subsequence)
