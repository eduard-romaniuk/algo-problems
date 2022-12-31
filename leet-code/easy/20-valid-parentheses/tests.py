from utils import testing


def test(func):
    testing.test(name='#1', func=func, args=['()'], expected=True)
    testing.test(name='#2', func=func, args=['()[]{}'], expected=True)
    testing.test(name='#3', func=func, args=['(]'], expected=False)
