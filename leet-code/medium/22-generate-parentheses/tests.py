from utils import testing


def test(func):
    testing.test(name='#1', func=func, args=[3], expected=["((()))", "(()())", "(())()", "()(())", "()()()"])
    testing.test(name='#2', func=func, args=[1], expected=["()"])
