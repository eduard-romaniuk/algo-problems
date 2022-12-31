import tests


# Time O(n)
# Space O(n)
def contains_duplicate(array):
    seen = set()
    for n in array:
        if n in seen:
            return True
        seen.add(n)
    return False


tests.test(contains_duplicate)
