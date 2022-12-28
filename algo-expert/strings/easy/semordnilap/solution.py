import tests


# Time O(n*m)
# Space O(n*m)
# Where n is the number of words and m is the length of the longest word
def semordnilap(words):
    words_set = set(words)
    pairs = []
    for word in words:
        reversed_word = word[::-1]
        if reversed_word in words_set and reversed_word != word:
            pairs.append([word, reversed_word])
            words_set.remove(word)
            words_set.remove(reversed_word)
    return pairs


tests.test(semordnilap)
