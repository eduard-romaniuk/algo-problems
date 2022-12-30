from utils import testing


def test(func):
    testing.test(name='#1', func=func, args=[[5, 2, [7, -1], 3, [6, [-13, 8], 4]]], expected=12)
    testing.test(name='#2', func=func, args=[[1, 2, [3], 4, 5]], expected=18)
    testing.test(name='#3', func=func, args=[[[[[[5]]]]]], expected=600)
    testing.test(name='#4', func=func, args=[[[1, 2], 3, [4, 5]]], expected=27)
