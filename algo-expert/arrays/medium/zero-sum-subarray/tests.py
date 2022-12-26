from utils import testing


def test(func):
    testing.test(name='#1', func=func,
                 args=[[-5, -5, 2, 3, -2]],
                 expected=True)
    testing.test(name='#2', func=func,
                 args=[[]],
                 expected=False)
