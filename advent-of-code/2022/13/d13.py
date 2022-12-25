from functools import cmp_to_key
from itertools import zip_longest


def read_packets():
    for pair in open('input.txt', 'r').read().split('\n\n'):
        packets = pair.split('\n')
        yield eval(packets[0]), eval(packets[1])


packets = list(read_packets())

EOF = -1


def is_in_right_order(left, right):
    for left_val, right_val in zip_longest(left, right, fillvalue=EOF):
        if type(right_val) is int and right_val == EOF:
            return False
        if type(left_val) is int and left_val == EOF:
            return True

        if type(left_val) is int and type(right_val) is int:
            if left_val != right_val:
                return left_val < right_val
        else:
            left_list = left_val if type(left_val) is list else [left_val]
            right_list = right_val if type(right_val) is list else [right_val]
            res = is_in_right_order(left_list, right_list)
            if res is not None:
                return res
    return None


results = {index + 1: is_in_right_order(*packet) for index, packet in enumerate(packets)}
result1 = 0
for i, is_right in results.items():
    if is_right:
        result1 += i
print(f'Task 1: {result1}')

# === Part 2 ===
packets.append(([[2]], [[6]]))


def compare(left, right):
    cmp_val = is_in_right_order(left, right)
    if cmp_val is None:
        return 0
    return -1 if cmp_val else 1


results = list(sorted([packet for pair in packets for packet in pair], key=cmp_to_key(compare)))
result2 = 1
for i, packet in enumerate(results):
    if packet == [[2]] or packet == [[6]]:
        result2 *= (i + 1)
print(f'Task 2: {result2}')
