import tests


# Time O(n)
# Space O(n)
def palindrome_number(x):
    return str(x) == str(x)[::-1]


tests.test(palindrome_number)
