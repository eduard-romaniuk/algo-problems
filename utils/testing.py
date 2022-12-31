def test(name, func, args, expected):
    result = func(*args)
    if type(result) is list:
        result.sort()
        expected.sort()
    assert result == expected, f'\nExpected: {expected}, Actual: {result}\nArguments: {args}'
    print(f"Test case '{name}' passed")
