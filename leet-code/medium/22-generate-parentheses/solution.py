import tests


# Time n-th Catalan number
# Space n-th Catalan number
def generate_parentheses(n):
    result = []
    stack = []

    def generator(opened=0, closed=0):
        if opened == closed == n:
            result.append(''.join(stack))
            return
        if opened < n:
            stack.append('(')
            generator(opened + 1, closed)
            stack.pop()
        if closed < opened:
            stack.append(')')
            generator(opened, closed + 1)
            stack.pop()

    generator()
    return result


tests.test(generate_parentheses)
