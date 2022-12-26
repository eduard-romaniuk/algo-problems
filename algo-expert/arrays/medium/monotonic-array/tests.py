from utils import testing


def test(func):
    testing.test(name='#1', func=func,
                 args=[[1, 1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 11]],
                 expected=True)
    testing.test(name='#2', func=func,
                 args=[[1, 2, -1, -2, -5]],
                 expected=False)
    testing.test(name='#3', func=func,
                 args=[[]],
                 expected=True)
    testing.test(name='#3', func=func,
                 args=[[1]],
                 expected=True)
    testing.test(name='#5', func=func,
                 args=[[1, 2]],
                 expected=True)
