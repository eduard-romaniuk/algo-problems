from utils import testing


def test(func):
    testing.test(name='#1', func=func,
                 args=[[5, 1, 4, 2]],
                 expected=[8, 40, 10, 20])
