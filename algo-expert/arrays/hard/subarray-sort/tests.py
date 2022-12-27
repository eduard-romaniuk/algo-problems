from utils import testing


def test(func):
    testing.test(name='#1', func=func,
                 args=[[1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]],
                 expected=[3, 9])
    testing.test(name='#2', func=func,
                 args=[[2, 1]],
                 expected=[0, 1])
    testing.test(name='#3', func=func,
                 args=[[4, 8, 7, 12, 11, 9, -1, 3, 9, 16, -15, 51, 7]],
                 expected=[0, 12])
