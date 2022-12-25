import tests


# Time O(n*log(n))
# Space O(1)
def non_constructible_change(coins):
    coins.sort()
    result = 0
    for coin in coins:
        if result + 1 < coin:
            return result + 1
        result += coin
    return result + 1


tests.test(non_constructible_change)
