from utils import testing


def test(func):
    testing.test(name='#1', func=func,
                 args=([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]),
                 expected=[28, 26])
    testing.test(name='#1', func=func,
                 args=([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]),
                 expected=[28, 26])
