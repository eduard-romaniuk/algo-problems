import tests


# Time O(n)
# Space O(n)
def is_palindrome(string):
    return string == string[::-1]


tests.test(is_palindrome)
