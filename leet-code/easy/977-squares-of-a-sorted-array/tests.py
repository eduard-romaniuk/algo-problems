from utils import testing


def test(func):
    testing.test(name='all positive', func=func, args=[[1, 2, 3, 5, 6, 8, 9]], expected=[1, 4, 9, 25, 36, 64, 81])
    testing.test(name='all negative', func=func, args=[[-5, -4, -3, -2, -1]], expected=[1, 4, 9, 16, 25])
    testing.test(name='positive and negative', func=func, args=[[-10, -5, 0, 5, 10]], expected=[0, 25, 25, 100, 100])
