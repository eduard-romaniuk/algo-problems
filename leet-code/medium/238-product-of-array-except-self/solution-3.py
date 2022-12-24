import tests


# Time O(n)
# Space O(1)
def product_array(array):
    result = [1] * len(array)
    suffix = 1
    prefix = 1
    for i in range(len(array)):
        result[i] *= prefix
        prefix *= array[i]
        result[-1 - i] *= suffix
        suffix *= array[-1 - i]
    return result


# print(product_array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

tests.test(product_array)
