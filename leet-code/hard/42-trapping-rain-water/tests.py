from utils import testing


def test(func):
    testing.test(name='#1', func=func, args=[[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]], expected=6)
    testing.test(name='#2', func=func, args=[[4, 2, 0, 3, 2, 5]], expected=9)
