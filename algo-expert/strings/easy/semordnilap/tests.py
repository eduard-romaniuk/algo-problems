from utils import testing


def test(func):
    testing.test(name='#1', func=func, args=[["aaa", "bbbb"]], expected=[])
    testing.test(name='#2', func=func, args=[["dog", "hello", "god"]], expected=[["dog", "god"]])
    testing.test(name='#3', func=func, args=[["dog", "desserts", "god", "stressed"]], expected=[["dog", "god"], ["desserts", "stressed"]])
