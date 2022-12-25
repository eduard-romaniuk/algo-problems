import sys

VARIABLES = {}
EXPRESSIONS = {}

for line in open('input.txt', 'r').read().split('\n'):
    [monkey, command] = line.split(': ')
    if command.isnumeric():
        if monkey == 'humn':
            VARIABLES[monkey] = 0
            continue
        VARIABLES[monkey] = int(command)
    else:
        if monkey == 'root':
            command = command.split()
            command[1] = '='
            EXPRESSIONS[monkey] = tuple(command)
            continue
        EXPRESSIONS[monkey] = tuple(command.split())


# print(EXPRESSIONS)
# print(VARIABLES)


def evaluate_expression(expression: str = 'root') -> float:
    if expression in VARIABLES:
        return VARIABLES[expression]
    left_operand, sign, right_operand = EXPRESSIONS[expression]
    left_operand = evaluate_expression(left_operand)
    right_operand = evaluate_expression(right_operand)
    if sign == '+':
        return left_operand + right_operand
    if sign == '-':
        return left_operand - right_operand
    if sign == '*':
        return left_operand * right_operand
    if sign == '/':
        return left_operand / right_operand


def is_contains_human(expression: str) -> bool:
    if expression in VARIABLES:
        return False
    left_operand, sign, right_operand = EXPRESSIONS[expression]
    if left_operand == 'humn' or right_operand == 'humn':
        return True
    return is_contains_human(left_operand) or is_contains_human(right_operand)


left_operand, sign, right_operand = EXPRESSIONS['root']
numeric_operand = None
human_operand = None
if is_contains_human(left_operand):
    human_operand = left_operand
    numeric_operand = right_operand
else:
    human_operand = right_operand
    numeric_operand = left_operand

numeric_operand = evaluate_expression(numeric_operand)


# print(numeric_operand)


# binary search
def evaluate_human_expression(expression, target_value):
    VARIABLES['humn'] = 0
    result0 = evaluate_expression(expression)
    VARIABLES['humn'] = 1
    result1 = evaluate_expression(expression)
    is_ascending = result0 < result1
    compare_func = (lambda r, t: r < t) if is_ascending else (lambda r, t: r > t)

    _to = sys.maxsize
    _from = -sys.maxsize - 1
    while _from < _to:
        center = (_from + _to) // 2
        VARIABLES['humn'] = center
        result = evaluate_expression(expression)
        if result == target_value:
            return center
        if compare_func(result, target_value):
            _from = center
        else:
            _to = center
    print("Can't find solution")
    exit()


print(evaluate_human_expression(human_operand, numeric_operand))
