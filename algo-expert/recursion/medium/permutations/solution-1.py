import tests


# Time O(n^2*n!)
#     | n calls to get_permutations method
#     | O(n) to create new permutation
#     | n! times new permutation will be created
# Space O(n*n!)
#     | n! permutations
#     | n for array slices
def get_permutations(array):
    return array if not array else \
        [array] if len(array) == 1 else \
        [
            permutation[:i] + [array[0]] + permutation[i:]
            for permutation in get_permutations(array[1:])
            for i in range(len(permutation) + 1)
        ]


tests.test(get_permutations)
