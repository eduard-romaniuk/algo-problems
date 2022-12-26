from utils import testing


def test(func):
    testing.test(name='#1', func=func,
                 args=[[[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]],
                 expected=[[1, 2], [3, 8], [9, 10]])
