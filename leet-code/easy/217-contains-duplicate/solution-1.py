import tests


# Time O(n*log(n))
# Space O(1)
def contains_duplicate(array):
    array.sort()
    for i in range(len(array) - 1):
        if array[i] == array[i + 1]:
            return True
    return False


tests.test(contains_duplicate)
