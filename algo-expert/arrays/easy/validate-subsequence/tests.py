def decorator_maker_with_arguments(decorator_arg1, decorator_arg2, decorator_arg3):
    def decorator(func):
        def wrapper(function_arg1, function_arg2, function_arg3):
            "This is the wrapper function"
            print("The wrapper can access all the variables\n"
                  "\t- from the decorator maker: {0} {1} {2}\n"
                  "\t- from the function call: {3} {4} {5}\n"
                  "and pass them to the decorated function"
                  .format(decorator_arg1, decorator_arg2, decorator_arg3,
                          function_arg1, function_arg2, function_arg3))
            return func(function_arg1, function_arg2, function_arg3)

        return wrapper

    return decorator


def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper


def test_cases(test_data_list):
    def decorator(func):
        def wrapper(func_to_test):
            for i, args in enumerate(test_data_list, start=1):
                func(func_to_test, *args)
                print(f'Test case #{i} passed')

        return wrapper

    return decorator


@test_cases([
    (([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10]), True)
])
def say_hi(func_to_test):
    pass
# def execute_test_case(func, args, expected):
#     result = func(*args)
#     assert result == expected, f'Expected: {expected}, Actual: {result}'
#
#
# def test(validate_subsequence_func):
#     test_cases = [
#         (([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10]), True),
#         (([3, 2, 4], 6), [2, 4]),
#         (([3, 3], 6), [3, 3])
#     ]
#     for i, args in enumerate(test_cases, start=1):
#         execute_test_case(validate_subsequence_func, *args)
#         print(f'Test case #{i} passed')
#     print('All tests passed!')
