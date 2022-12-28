from utils import testing


def test(func):
    testing.test(name='#1', func=func, args=["abcdcaf"], expected=1)
    testing.test(name='#2', func=func, args=["a"], expected=0)
    testing.test(name='#3', func=func, args=["faadabcbbebdf"], expected=6)
    testing.test(name='#4', func=func, args=["aabb"], expected=-1)
