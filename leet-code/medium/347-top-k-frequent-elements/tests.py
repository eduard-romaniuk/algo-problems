from utils import testing


def test(func):
    testing.test(name='#1', func=func, args=[[1, 1, 1, 2, 2, 3], 2], expected=[1, 2])
    testing.test(name='#2', func=func, args=[[3, 0, 1, 0], 1], expected=[0])
    testing.test(name='#3', func=func, args=[[1], 1], expected=[1])
