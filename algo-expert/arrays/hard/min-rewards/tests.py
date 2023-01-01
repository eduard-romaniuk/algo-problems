from utils import testing


def test(func):
    testing.test(name='#1', func=func,
                 args=[[8, 4, 2, 1, 3, 6, 7, 9, 5]],
                 expected=25)
    testing.test(name='#2', func=func,
                 args=[[0, 4, 2, 1, 3]],
                 expected=9)
    testing.test(name='#3', func=func,
                 args=[[2, 1, 4, 3, 6, 5, 8, 7, 10, 9]],
                 expected=15)
    testing.test(name='#4', func=func,
                 args=[[800, 400, 20, 10, 30, 61, 70, 90, 17, 21, 22, 13, 12, 11, 8, 4,
                        2, 1, 3, 6, 7, 9, 0, 68, 55, 67, 57, 60, 51, 661, 50, 65, 53]],
                 expected=93)
