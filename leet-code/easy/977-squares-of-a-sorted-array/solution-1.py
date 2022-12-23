import tests


# Space O(n) - Could be O(1) if we modify existing list
# Time O(n*log n) - O(n) to square each element + O(nlogn) to sort array
def sorted_squared_array(array):
    return sorted([i ** 2 for i in array])


tests.test(sorted_squared_array)
