import tests


def product_sum(array, depth_level=1):
    total = 0
    for element in array:
        if type(element) is list:
            total += product_sum(element, depth_level + 1)
        else:
            total += element
    return depth_level * total


tests.test(product_sum)
