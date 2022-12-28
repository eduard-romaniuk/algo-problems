from utils import testing


def test(func):
    testing.test(name='#1', func=func, args=('Bste!hetsi ogEAxpelrt x ', 'AlgoExpert is the Best!'), expected=True)
    testing.test(name='#2', func=func, args=('abc', ''), expected=True)
    testing.test(name='#3', func=func, args=('aheaollabbhb', 'hello'), expected=True)
    testing.test(name='#4', func=func, args=('helloworld ', 'hello wOrld'), expected=False)
