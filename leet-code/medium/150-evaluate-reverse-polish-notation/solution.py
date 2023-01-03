import tests


# Time O(n)
# Space O(n)
def eval_rpn(tokens):
    stack = []
    for token in tokens:
        if token.lstrip('-').isnumeric():
            stack.append(int(token))
        else:
            right = stack.pop()
            left = stack.pop()
            if token == '+':
                stack.append(left + right)
            elif token == '-':
                stack.append(left - right)
            elif token == '*':
                stack.append(left * right)
            elif token == '/':
                stack.append(int(left / right))
    return stack.pop()


tests.test(eval_rpn)
