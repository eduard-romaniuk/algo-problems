def test(name, func, args, expected):
    result = func(*args)
    assert result == expected, f'Expected: {expected}, Actual: {result}'
    print(f"Test case '{name}' passed")
