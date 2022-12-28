from utils import testing


def test(func):
    testing.test(name='is palindrome', func=func, args=["abcba"], expected=True)
    testing.test(name='one character', func=func, args=["a"], expected=True)
    testing.test(name="isn't palindrome", func=func, args=["abc"], expected=False)
