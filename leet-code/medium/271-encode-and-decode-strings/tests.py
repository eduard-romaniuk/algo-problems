from utils import testing


def test(encode_func, decode_func):
    def func(string_list):
        return decode_func(encode_func(string_list))

    testing.test(name='#1', func=func, args=[["eat", "tea", "tan", "ate", "nat", "bat"]],
                 expected=["eat", "tea", "tan", "ate", "nat", "bat"])
    testing.test(name='#2', func=func, args=[[';some;', ';test;', ';string;']],
                 expected=[';some;', ';test;', ';string;'])
