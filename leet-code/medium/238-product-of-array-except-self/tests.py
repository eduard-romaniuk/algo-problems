from utils import testing


def test(func):
    testing.test(name='all positive', func=func, args=[[1, 2, 3, 4]], expected=[24, 12, 8, 6])
    testing.test(name='all negative', func=func, args=[[-1, -2, -3, -4]], expected=[-24, -12, -8, - 6])
    testing.test(name='contains one zero', func=func, args=[[-1, -2, 0, 2, 1]], expected=[0, 0, 4, 0, 0])
    testing.test(name='contains few zeros', func=func, args=[[-1, -2, 0, 2, 1, 0]], expected=[0, 0, 0, 0, 0, 0])
