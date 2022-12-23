def execute_test_case(func, args, expected):
    result = func(*args)
    assert result == expected, f'Expected: {expected}, Actual: {result}'


def test(two_sum_func):
    test_cases = [
        (([2, 7, 11, 15], 9), [0, 1]),
        (([3, 2, 4], 6), [1, 2]),
        (([3, 3], 6), [0, 1])
    ]
    for i, args in enumerate(test_cases, start=1):
        execute_test_case(two_sum_func, *args)
        print(f'Test case #{i} passed')
    print('All tests passed!')
