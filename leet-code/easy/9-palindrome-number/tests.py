from utils import testing


def test(func):
    testing.test(name='#1', func=func, args=[121], expected=True)
    testing.test(name='#2', func=func, args=[-121], expected=False)
    testing.test(name='#3', func=func, args=[10], expected=False)
    testing.test(name='#4', func=func, args=[100005], expected=False)
