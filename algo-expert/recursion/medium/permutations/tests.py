from utils import testing


def test(func):
    testing.test(name='empty array', func=func, args=[[]], expected=[])
    testing.test(name='one element', func=func, args=[[1]], expected=[[1]])
    testing.test(name='three elements', func=func, args=[[1, 2, 3]],
                 expected=[[1, 2, 3], [2, 1, 3], [2, 3, 1], [1, 3, 2], [3, 1, 2], [3, 2, 1]])
