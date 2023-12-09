import re

digit_regex = re.compile(r'-?\d+')
matrix = [[int(cell) for cell in digit_regex.findall(line)] for line in open('input.txt', 'r').read().split('\n')]


def get_next_seq_value(seq):
    diff_matrix = [seq]
    while not all(x == 0 for x in diff_matrix[-1]):
        diff_matrix.append([diff_matrix[-1][i + 1] - diff_matrix[-1][i] for i in range(len(diff_matrix[-1]) - 1)])
    return sum(map(lambda seq: seq[-1], diff_matrix))


print('Result:', sum(map(get_next_seq_value, matrix)))
