from utils import testing


def test(func):
    testing.test(name='#1', func=func,
                 args=[[2, 1, 5, 2, 3, 3, 4]],
                 expected=2)
