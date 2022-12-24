import tests


# Space O(1)
# Time O(n*log(n))
def sorted_squared_array(array):
    return sorted([i ** 2 for i in array])


tests.test(sorted_squared_array)
