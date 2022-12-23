from utils import testing


def test(func):
    testing.test(name='#1', func=func, args=([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10]), expected=True)
    testing.test(name='#2', func=func, args=([5, 1, 22, 25, 6, -1, 8, 10], [5, 1, 22, 25, 6, -1, 8, 10]), expected=True)
    testing.test(name='#3', func=func, args=([5, 1, 22, 25, 6, -1, 8, 10], [25]), expected=True)
    testing.test(name='#4', func=func, args=([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, -1]), expected=False)
    testing.test(name='#5', func=func, args=([5, 1, 22, 25, 6, -1, 8, 10], [26]), expected=False)
