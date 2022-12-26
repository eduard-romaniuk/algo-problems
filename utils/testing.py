def test(name, func, args, expected):
    result = func(*args)
    assert result == expected, f'\nExpected: {expected}, Actual: {result}\nArguments: {args}'
    print(f"Test case '{name}' passed")
