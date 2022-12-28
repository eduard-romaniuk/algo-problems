import tests


# Time O(c + d)
# Space O(c)
def generate_document(characters, document):
    if document == '':
        return True
    charset = {}
    for c in characters:
        if c not in charset:
            charset[c] = 0
        charset[c] += 1
    for c in document:
        if c not in charset or charset[c] == 0:
            return False
        charset[c] -= 1
    return True


tests.test(generate_document)
