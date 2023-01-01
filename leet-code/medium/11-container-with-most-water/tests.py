from utils import testing


def test(func):
    testing.test(name='#1', func=func,
                 args=[[1, 8, 6, 2, 5, 4, 8, 3, 7]],
                 expected=49)
    testing.test(name='#2', func=func,
                 args=[[1, 1]],
                 expected=1)
