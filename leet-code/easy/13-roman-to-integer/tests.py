from utils import testing


def test(func):
    testing.test(name='#1', func=func, args=['III'], expected=3)
    testing.test(name='#2', func=func, args=['LVIII'], expected=58)
    testing.test(name='#3', func=func, args=['MCMXCIV'], expected=1994)
