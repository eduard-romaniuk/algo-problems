import tests


# Time O(n)
# Space O(n)
def first_duplicate_value(array):
    seen = set()
    for n in array:
        if n in seen:
            return n
        seen.add(n)
    return -1


tests.test(first_duplicate_value)
