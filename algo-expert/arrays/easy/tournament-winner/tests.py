from utils import testing


def test(func):
    testing.test(
        name='#1',
        func=func,
        args=([["HTML", "C#"], ["C#", "Python"], ["Python", "HTML"]], [0, 0, 1]),
        expected='Python'
    )
