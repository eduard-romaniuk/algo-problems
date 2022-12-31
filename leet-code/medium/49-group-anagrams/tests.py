from utils import testing


def test(func):
    testing.test(name='#1', func=func, args=[["eat", "tea", "tan", "ate", "nat", "bat"]],
                 expected=[['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']])
    testing.test(name='#2', func=func, args=[[""]], expected=[[""]])
    testing.test(name='#3', func=func, args=[["a"]], expected=[["a"]])
