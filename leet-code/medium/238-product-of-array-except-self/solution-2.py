import tests


# Time O(n)
# Space O(1)
def product_array(array):
    result = [1] * len(array)
    suffix = 1
    for i in range(1, len(array)):
        result[i] = result[i - 1] * array[i - 1]
    for i in range(1, len(array)):
        suffix *= array[-i]
        result[-1 - i] *= suffix
    return result


tests.test(product_array)
