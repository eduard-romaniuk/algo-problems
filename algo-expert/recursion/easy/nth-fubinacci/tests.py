from utils import testing


def test(func):
    testing.test(name='#1', func=func, args=[1], expected=0)
    testing.test(name='#2', func=func, args=[2], expected=1)
    testing.test(name='#3', func=func, args=[10], expected=34)
    testing.test(name='#4', func=func, args=[100], expected=218922995834555169026)
