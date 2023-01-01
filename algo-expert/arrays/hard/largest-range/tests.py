from utils import testing


def test(func):
    testing.test(name='#1', func=func,
                 args=[[1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]],
                 expected=[0, 7])
    testing.test(name='#2', func=func,
                 args=[[4, 2, 1, 3]],
                 expected=[1, 4])
    testing.test(name='#3', func=func,
                 args=[[8, 4, 2, 10, 3, 6, 7, 9, 1]],
                 expected=[6, 10])
