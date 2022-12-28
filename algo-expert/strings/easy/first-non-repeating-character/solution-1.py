import tests


# Time O(n^2)
# Space O(1)
def first_non_repeating_character(string):
    for i, c1 in enumerate(string):
        all_ne = True
        for j, c2 in enumerate(string):
            if i == j:
                continue
            if c1 == c2:
                all_ne = False
                break
        if all_ne:
            return i
    return -1


tests.test(first_non_repeating_character)
