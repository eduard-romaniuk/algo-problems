from utils import testing


def test(func):
    testing.test(name='#1', func=func, args=[[8, 5, 2, 9, 5, 6, 3]], expected=[2, 3, 5, 5, 6, 8, 9])
