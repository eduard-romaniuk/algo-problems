import tests


# Time O(n)
# Space O(n)
def run_length_encoding(string):
    result = []
    current_char = string[0]
    length = 1
    for c in string[1:]:
        if c != current_char or length == 9:
            result.append(str(length))
            result.append(current_char)
            current_char = c
            length = 0
        length += 1
    else:
        result.append(str(length))
        result.append(current_char)
    return ''.join(result)


tests.test(run_length_encoding)
