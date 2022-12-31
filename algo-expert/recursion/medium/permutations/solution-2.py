import tests


def helper(i, array, permutations):
    if i == len(array) - 1:
        permutations.append(array[:])
    else:
        for j in range(i, len(array)):
            array[i], array[j] = array[j], array[i]
            helper(i + 1, array, permutations)
            array[i], array[j] = array[j], array[i]


# Time O(n*n!)
# Space O(n*n!)
def get_permutations(array):
    permutations = []
    helper(0, array, permutations)
    return permutations


tests.test(get_permutations)
