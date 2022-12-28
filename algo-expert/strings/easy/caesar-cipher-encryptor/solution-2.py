import tests
import string


# Time O(n)
# Space O(n)
def caesar_cipher_encryptor(text, key):
    alphabet = list(string.ascii_lowercase)
    return ''.join(alphabet[(alphabet.index(c) + key) % 26] for c in text)


tests.test(caesar_cipher_encryptor)
