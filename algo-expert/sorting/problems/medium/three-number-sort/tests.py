from utils import testing


def test(func):
    testing.test(name='#1', func=func, args=([1, 0, 0, -1, -1, 0, 1, 1], [0, 1, -1]),
                 expected=[0, 0, 0, 1, 1, 1, -1, -1])
    testing.test(name='#2', func=func, args=([9, 9, 9, 7, 9, 7, 9, 9, 7, 9], [11, 7, 9]),
                 expected=[7, 7, 7, 9, 9, 9, 9, 9, 9, 9])
