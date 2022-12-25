from utils import testing


def test(func):
    testing.test(name='#1', func=func, args=[[5, 7, 1, 1, 2, 3, 22]], expected=20)
    testing.test(name='#2', func=func, args=[[]], expected=1)
    testing.test(name='#3', func=func, args=[[87]], expected=1)
