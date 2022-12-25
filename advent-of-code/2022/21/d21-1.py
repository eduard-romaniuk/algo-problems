VARIABLES = {}
EXPRESSIONS = {}

for line in open('input.txt', 'r').read().split('\n'):
    [monkey, command] = line.split(': ')
    if command.isnumeric():
        VARIABLES[monkey] = int(command)
    else:
        EXPRESSIONS[monkey] = tuple(command.split())

print(EXPRESSIONS)
print(VARIABLES)


def evaluate_expression(expression: str = 'root') -> int:
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
        return left_operand // right_operand
    print('Unknown sign', sign)
    exit()


print(evaluate_expression('root'))
