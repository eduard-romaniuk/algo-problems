from utils import testing


def test(func):
    testing.test(name='#1', func=func, args=('xyz', 2), expected='zab')
    testing.test(name='#2', func=func, args=('abc', 0), expected='abc')
    testing.test(name='#3', func=func, args=('abc', 52), expected='abc')
