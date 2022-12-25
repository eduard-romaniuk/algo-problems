from utils import testing


def test(func):
    testing.test(name='#1', func=func,
                 args=([2, 7, 11, 15], 20),
                 expected=[[2, 7, 11]])
    testing.test(name='#2', func=func,
                 args=([12, 3, 1, 2, -6, 5, -8, 6], 0),
                 expected=[[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]])
