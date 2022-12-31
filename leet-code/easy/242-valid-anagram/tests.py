from utils import testing


def test(func):
    testing.test(name='#1', func=func, args=['ac', 'bb'], expected=False)
    testing.test(name='#2', func=func, args=['abc', 'cab'], expected=True)
