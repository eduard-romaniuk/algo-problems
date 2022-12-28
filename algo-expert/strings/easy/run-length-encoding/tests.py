from utils import testing


def test(func):
    testing.test(name='#1', func=func, args=['AAAAAAAAAAAAABBCCCCDD'], expected='9A4A2B4C2D')
    testing.test(name='#2', func=func, args=['122333'], expected='112233')
    testing.test(name='#3', func=func, args=['************^^^^^^^$$$$$$%%%%%%%!!!!!!AAAAAAAAAAAAAAAAAAAA'], expected='9*3*7^6$7%6!9A9A2A')
