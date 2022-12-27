from utils import testing


def test(func):
    testing.test(name='#1', func=func,
                 args=[[7, 6, 4, -1, 1, 2], 16],
                 expected=[[7, 6, 4, -1], [7, 6, 1, 2]])
    testing.test(name='#2', func=func,
                 args=[[-10, -3, -5, 2, 15, -7, 28, -6, 12, 8, 11, 5], 20],
                 expected=[[-5, 2, 15, 8], [-3, 2, -7, 28], [-10, -3, 28, 5],
                           [-10, 28, -6, 8], [-7, 28, -6, 5], [-5, 2, 12, 11],
                           [-5, 12, 8, 5]])
