from utils import testing


def test(func):
    testing.test(name='#1', func=func,
                 args=[[
                     [1, 3, 4, 10],
                     [2, 5, 9, 11],
                     [6, 8, 12, 15],
                     [7, 13, 14, 16]
                 ]],
                 expected=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
    testing.test(name='#2', func=func,
                 args=[[
                     [1, 2, 3, 4, 5]
                 ]],
                 expected=[1, 2, 3, 4, 5])
    testing.test(name='#3', func=func,
                 args=[[
                     [1],
                     [2],
                     [3],
                     [4],
                     [5]
                 ]],
                 expected=[1, 2, 3, 4, 5])
