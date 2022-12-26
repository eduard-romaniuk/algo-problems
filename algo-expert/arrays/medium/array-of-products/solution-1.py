import tests


# Time O(n)
# Space O(n)
def array_of_products(array):
    suffix = [1] * len(array)
    prefix = [1] * len(array)

    for i in range(1, len(array)):
        prefix[i] = prefix[i - 1] * array[i - 1]
        suffix[-1 - i] = suffix[-i] * array[-i]

    result = []
    for i in range(len(array)):
        result.append(suffix[i] * prefix[i])
    return result


tests.test(array_of_products)
