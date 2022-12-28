import tests


# Time O(n)
# Space O(n)
def caesar_cipher_encryptor(string, key):
    a_ord = ord('a')
    return ''.join(chr((ord(c) - a_ord + key) % 26 + a_ord) for c in string)


tests.test(caesar_cipher_encryptor)
