from utils import testing


def test(func):
    testing.test(name='#1', func=func, args=["A man, a plan, a canal: Panama"], expected=True)
    testing.test(name='#2', func=func, args=["race a car"], expected=False)
    testing.test(name='#3', func=func, args=[" "], expected=True)
    testing.test(name='#4', func=func, args=["0P"], expected=False)
