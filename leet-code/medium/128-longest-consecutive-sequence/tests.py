from utils import testing


def test(func):
    testing.test(name='#1', func=func, args=[[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]], expected=9)
    testing.test(name='#2', func=func, args=[[100, 4, 200, 1, 3, 2]], expected=4)
    testing.test(name='#3', func=func, args=[[]], expected=0)
