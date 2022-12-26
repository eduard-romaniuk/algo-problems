from utils import testing


def test(func):
    testing.test(name='#1', func=func,
                 args=([2, 1, 2, 2, 2, 3, 4, 2], 2),
                 expected=[1, 3, 4, 2, 2, 2, 2, 2])
