import tests

DELIMITER = ';'


def encode(string_list):
    metadata = [str(len(string_list)), DELIMITER]
    for string in string_list:
        metadata.append(str(len(string)))
        metadata.append(DELIMITER)
    return ''.join(metadata + string_list)


def decode(string):
    i = 0

    def read_metadata_number():
        nonlocal i
        number = []
        while string[i] != DELIMITER:
            number.append(string[i])
            i += 1
        i += 1
        return int(''.join(number))

    # first read number of words
    # then read word lengths
    word_lengths = [read_metadata_number() for _ in range(read_metadata_number())]

    result = []
    for word_length in word_lengths:
        current_word = []
        for _ in range(word_length):
            current_word.append(string[i])
            i += 1
        result.append(''.join(current_word))
    return result


tests.test(encode, decode)
