import tests


# Time O(n)
# Space O(1)
def is_palindrome(string):
    start = 0
    end = len(string) - 1
    while start < end:
        if string[start] != string[end]:
            return False
        start += 1
        end -= 1
    return True


tests.test(is_palindrome)
