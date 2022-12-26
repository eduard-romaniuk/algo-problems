import tests


# Time O(n)
# Space O(n)
def array_of_products(array):
    result = [1] * len(array)
    prefix = 1
    suffix = 1

    for i in range(len(array)):
        result[i] *= prefix
        prefix *= array[i]
        result[-1 - i] *= suffix
        suffix *= array[-1 - i]

    return result


tests.test(array_of_products)
