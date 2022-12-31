from utils import testing


def test(func):
    testing.test(name='#1', func=func, args=[[1, 2, 3, 1]], expected=True)
    testing.test(name='#2', func=func, args=[[1, 2, 3, 4]], expected=False)
