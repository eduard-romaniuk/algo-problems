import tests


# Time O(log(n))
# Space O(1)
def palindrome_number(x):
    if x < 0 or x != 0 and x % 10 == 0:
        return False
    rev_x = 0
    while x > rev_x:
        rev_x = rev_x * 10 + x % 10
        x //= 10
    return x == rev_x or x == rev_x // 10


tests.test(palindrome_number)
