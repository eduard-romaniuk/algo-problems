from utils import testing


def test(func):
    testing.test(name='#1', func=func, args=([2, 7, 11, 15], 9), expected=[0, 1])
    testing.test(name='#2', func=func, args=([3, 2, 4], 6), expected=[1, 2])
    testing.test(name='#3', func=func, args=([3, 3], 6), expected=[0, 1])
