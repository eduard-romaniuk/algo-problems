from utils import testing


def test(func):
    testing.test(name='#1', func=func,
                 args=[[0, 1, 1]],
                 expected=[])
    testing.test(name='#2', func=func,
                 args=[[0, 0, 0]],
                 expected=[[0, 0, 0]])
    testing.test(name='#3', func=func,
                 args=[[-1, 0, 1, 2, -1, -4]],
                 expected=[[-1, -1, 2], [-1, 0, 1]])
