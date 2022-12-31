import tests

brackets = {
    '(': ')',
    '{': '}',
    '[': ']'
}


# Time O(n)
# Space O(n)
def valid_parentheses(s):
    stack = []
    for bracket in s:
        if bracket in brackets:
            stack.append(brackets[bracket])
        else:
            if len(stack) == 0 or stack.pop() != bracket:
                return False
    return len(stack) == 0


tests.test(valid_parentheses)
