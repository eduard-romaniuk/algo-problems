from utils import testing


def test(func):
    testing.test(name='#1', func=func,
                 args=[[
                     [1, 2, 3, 4],
                     [12, 13, 14, 5],
                     [11, 16, 15, 6],
                     [10, 9, 8, 7]
                 ]],
                 expected=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
    testing.test(name='#2', func=func,
                 args=[[
                     [1, 2, 3, 4],
                     [10, 11, 12, 5],
                     [9, 8, 7, 6]
                 ]],
                 expected=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
