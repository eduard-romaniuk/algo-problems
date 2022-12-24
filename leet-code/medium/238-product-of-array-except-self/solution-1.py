import tests


# Time O(n)
# Space O(n)
def product_array(array):
    left = [1] * len(array)
    right = [1] * len(array)

    for i in range(1, len(array)):
        left[i] = left[i - 1] * array[i - 1]

    for i in range(len(array) - 2, -1, -1):
        right[i] = right[i + 1] * array[i + 1]

    for i in range(len(array)):
        array[i] = left[i] * right[i]

    return array


tests.test(product_array)
