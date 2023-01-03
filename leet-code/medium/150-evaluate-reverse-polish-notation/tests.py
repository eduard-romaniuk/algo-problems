from utils import testing


def test(func):
    testing.test(name='#1', func=func, args=[["2", "1", "+", "3", "*"]], expected=9)
    testing.test(name='#2', func=func, args=[["4", "13", "5", "/", "+"]], expected=6)
    testing.test(name='#3', func=func, args=[["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]],
                 expected=22)
