from utils import testing


def test(func):
    testing.test(name='#1', func=func,
                 args=[[1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]],
                 expected=6)
    testing.test(name='#2', func=func,
                 args=[[]],
                 expected=0)
    testing.test(name='#3', func=func,
                 args=[[1, 2]],
                 expected=0)
    testing.test(name='#4', func=func,
                 args=[[1, 3, 2]],
                 expected=3)
    testing.test(name='#5', func=func,
                 args=[[5, 4, 3, 2, 1, 2, 1]],
                 expected=3)
    testing.test(name='#6', func=func,
                 args=[[1, 2, 3, 3, 2, 1]],
                 expected=0)
    testing.test(name='#7', func=func,
                 args=[[1, 1, 3, 2, 1]],
                 expected=4)




